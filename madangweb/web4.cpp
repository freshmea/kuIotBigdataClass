#include "Poco/Net/HTTPRequestHandler.h"
#include "Poco/Net/HTTPServer.h"
#include "Poco/Net/HTTPServerRequest.h"
#include "Poco/Net/HTTPServerResponse.h"
#include "Poco/Util/ServerApplication.h"

#include <mysql_driver.h>
#include <cppconn/statement.h>

#include <iostream>
#include <fstream>
#include <string>

using namespace std;
using namespace Poco::Net;
using namespace Poco::Util;

class FormRequestHandler: public HTTPRequestHandler
{
public:
	FormRequestHandler()
	{
	}

	void handleRequest(HTTPServerRequest& request, HTTPServerResponse& response)
	{
		Application& app = Application::instance();
		app.logger().information("Request from " + request.clientAddress().toString());

		response.setChunkedTransferEncoding(true);
		response.setContentType("text/html");
        std::ostream& ostr = response.send();
        std::ifstream file("/home/aa/kuIotBigdataClass/madangweb/templates/test.html");
        if (file.is_open()) {
            ostr << file.rdbuf();
            file.close();
        }

        sql::mysql::MySQL_Driver *driver;
        sql::Connection *con;

        string host = "localhost:3306";
        string user = "root";
        string password = "0000";
        try {
            driver = sql::mysql::get_mysql_driver_instance();
            con = driver->connect(host, user, password);
            con->setSchema("madangdb");
            sql::Statement *stmt = con->createStatement();
            sql::ResultSet *res = stmt->executeQuery("SELECT * FROM Book");
            while (res->next())
            {
                ostr << "<td>" + res->getString("bookname") + "</td>";
                ostr << "<td>" + res->getString("publisher") + "</td>";
                ostr << "<td>" + std::to_string(res->getInt("price")) + "</td></tr>";
            }
        } catch (sql::SQLException &e) {
            cout << "# ERR: SQLException in " << __FILE__;
            cout << "(" << __FUNCTION__ << ") on line " << __LINE__ << endl;
            cout << "# ERR: " << e.what();
            cout << " (MySQL error code: " << e.getErrorCode();
            cout << ", SQLState: " << e.getSQLState() << " )" << endl;
        }
        std::ifstream file1("/home/aa/kuIotBigdataClass/madangweb/templates/test_down.html");
        if (file1.is_open()) {
            ostr << file1.rdbuf();
            file1.close();
        }
    }
};


class FormRequestHandlerFactory: public HTTPRequestHandlerFactory
{
public:
	FormRequestHandlerFactory(){}
	HTTPRequestHandler* createRequestHandler(const HTTPServerRequest& request)
	{return new FormRequestHandler;}
};


class HTTPFormServer: public Poco::Util::ServerApplication
{
public:
	HTTPFormServer(){}

protected:
	int main(const std::vector<std::string>& args)
	{
        unsigned short port = (unsigned short) config().getInt("HTTPFormServer.port", 9980);
        ServerSocket svs(port);
        HTTPServer srv(new FormRequestHandlerFactory, svs, new HTTPServerParams);
        srv.start();
        waitForTerminationRequest();
        srv.stop();
		return Application::EXIT_OK;
	}
};


int main(int argc, char** argv)
{
	HTTPFormServer app;
	return app.run(argc, argv);
}
