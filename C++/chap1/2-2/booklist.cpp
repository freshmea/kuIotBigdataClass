#include <iostream>

#include <mysql_driver.h>
#include <mysql_connection.h>
#include <cppconn/driver.h>
#include <cppconn/exception.h>
#include <cppconn/resultset.h>
#include <cppconn/statement.h>

using namespace std;

int main() {
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

        while (res->next()) {
            cout << res->getInt("bookid") << "\t";
            cout << res->getString("bookname") << "\t";
            cout << res->getString("publisher") << "\t";
            cout << res->getInt("price") << endl;
        }

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

    return 0;
}