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

using namespace Wt;
using namespace std;

class BookApplication : public WApplication
{
public:
    BookApplication(const WEnvironment& env)
        : WApplication(env)
    {
        setTitle("마당서점 도서목록");
        auto bookTemplate = std::make_unique<WTemplate>();
        bookTemplate->setTemplateText("<h2>마당서점 도서목록</h2>", TextFormat::UnsafeXHTML);
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
            bookTemplate->setTemplateText("<p>Book ID: ${bookid}<br>Book Name: ${bookname}</p>", TextFormat::UnsafeXHTML);
            while (res->next())
            {
                auto bookTemplate = std::make_unique<WTemplate>();
                bookTemplate->setTemplateText("<p>Book ID: ${bookid}<br>Book Name: ${bookname}</p>", TextFormat::UnsafeXHTML);

                bookTemplate->bindString("bookid", WString::fromUTF8(std::to_string(res->getInt("bookid"))));
                bookTemplate->bindString("bookname", WString::fromUTF8(res->getString("bookname")));

                root()->addWidget(std::move(bookTemplate));
            }
            // while (res->next()) {
            //     root()->addWidget(std::make_unique<WText>(WString::fromUTF8(std::to_string(res->getInt("bookid")))));
            //     root()->addWidget(std::make_unique<WText>("   "));
            //     root()->addWidget(std::make_unique<WText>(WString::fromUTF8(res->getString("bookname"))));
            //     root()->addWidget(std::make_unique<WText>("   "));
            //     root()->addWidget(std::make_unique<WText>(WString::fromUTF8(res->getString("publisher"))));
            //     root()->addWidget(std::make_unique<WText>("   "));
            //     root()->addWidget(std::make_unique<WText>(WString::fromUTF8(std::to_string(res->getInt("price")))));
            //     root()->addWidget(std::make_unique<WBreak>());
            // }
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