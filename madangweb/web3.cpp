#include <Wt/WApplication.h>
#include <Wt/WContainerWidget.h>
#include <Wt/WText.h>
#include <Wt/WBreak.h>
#include <Wt/Http/Request.h>
#include <Wt/WPushButton.h>
#include <Wt/WLineEdit.h>
#include <Wt/WTemplate.h>

#include <mysql_driver.h>
#include <mysql_connection.h>
#include <cppconn/driver.h>
#include <cppconn/exception.h>
#include <cppconn/resultset.h>
#include <cppconn/statement.h>

#include <string>
#include <fstream>
using namespace Wt;
using namespace std;

std::string readFileToString(const std::string& fileName)
{
  std::fstream file(fileName.c_str(), std::ios::in | std::ios::binary | std::ios::ate);
  int length = file.tellg();
  file.seekg(0, std::ios::beg);

  std::unique_ptr<char[]> buf(new char[length]);
  file.read(buf.get(), length);
  file.close();

  return std::string(buf.get(), length);
}

class BookApplication : public WApplication
{
public:
    BookApplication(const WEnvironment& env)
        : WApplication(env)
    {
        setTitle("마당서점 도서목록");
        auto bookTemplate = std::make_unique<WTemplate>();
        string template_str = readFileToString("/home/aa/kuIotBigdataClass/madangweb/templates/test.html");
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
                template_str += "<tr><td>" + res->getString("bookname") + "</td>";
                template_str += "<td>" + res->getString("publisher") + "</td>";
                template_str += "<td>" + std::to_string(res->getInt("price")) + "</td></tr>";
            }
            template_str += readFileToString("/home/aa/kuIotBigdataClass/madangweb/templates/test_down.html");
            bookTemplate->setTemplateText(template_str, TextFormat::UnsafeXHTML);
            root()->addWidget(std::move(bookTemplate));
            delete res;
            delete stmt;
            delete con;
        } catch (sql::SQLException &e) {
            cout << "# ERR: SQLException in " << __FILE__;
            cout << "(" << __FUNCTION__ << ") on line " << __LINE__ << endl;
            cout << "# ERR: " << e.what();
            cout << " (MySQL error code: " << e.getErrorCode();
            cout << ", SQLState: " << e.getSQLState() << " )" << endl;
        }
        root()->addWidget(std::make_unique<WText>("end of book list"));
        root()->addWidget(std::make_unique<WBreak>());
    }

    ~BookApplication() override {} // Add the missing destructor declaration
private:
    Wt::WLineEdit *bookidEdit_;
    Wt::WText *greeting_;
};

int main(int argc, char **argv)
{
    return Wt::WRun(argc, argv, [](const Wt::WEnvironment &env)
                    { return std::make_unique<BookApplication>(env); });
}