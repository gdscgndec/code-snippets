#include <sqlite3.h>
#include <stdio.h>
#include <iostream>

using namespace std;

static int createDB(const char* s);
static int createTable(const char* s);
static int deleteData(const char* s);
static int insertData(const char* s);
static int updateData(const char* s);
static int selectData(const char* s);
static int callback(void* NotUsed, int argc, char** argv, char** azColName);

int main()
{
	const char* dir = R"(D:\DeleteMe\STUDENTS.db)";

	createDB(dir);
	createTable(dir);
	// deleteData(dir); // use prior to insert
	//insertData(dir); // uncomment the deleteData above to avoid duplicates
	// updateData(dir);
	selectData(dir);
	return 0;
}

static int createDB(const char* s)
{
	sqlite3* DB;

	int exit = 0;
	exit = sqlite3_open(s, &DB);

	sqlite3_close(DB);

	return 0;
}

static int createTable(const char* s)
{
	sqlite3* DB;
	char* messageError;

	string sql = "CREATE TABLE IF NOT EXISTS StudentData("
		"ROLLNO    INT NOT NULL, "
		"FNAME     TEXT NOT NULL, "
		"LNAME     TEXT NOT NULL); ";

	try
	{
		int exit = 0;
		exit = sqlite3_open(s, &DB);
		/* An open database, SQL to be evaluated, Callback function, 1st argument to callback, Error msg written here */
		exit = sqlite3_exec(DB, sql.c_str(), callback, 0, &messageError);
		if (exit != SQLITE_OK) {
			cerr << "Error in createTable function." << endl;
			sqlite3_free(messageError);
		}
		else {
			cout << "Table created Successfully" << endl;
		}
			sqlite3_close(DB);
	}
	catch (const exception& e)
	{
		cerr << e.what();
	}

	return 0;
}

static int insertData(const char* s)
{
	sqlite3* DB;
	char* messageError;

	string sql(
		"INSERT INTO StudentData(ROLLNO, FNAME, LNAME) VALUES(1915084, 'Varanpreet', 'Kaur');"
		"INSERT INTO StudentData (ROLLNO, FNAME, LNAME) VALUES(1915085, 'Vishal', 'Dutta');"
		"INSERT INTO StudentData (ROLLNO, FNAME, LNAME) VALUES(1915086, 'Vrishti', 'Gupta');"
		"INSERT INTO StudentData(ROLLNO, FNAME, LNAME) VALUES(1915087, 'Yuvraj', 'Khanna');"
		"INSERT INTO StudentData (ROLLNO, FNAME, LNAME) VALUES(1915103, 'Priyanka', 'Jhamb');"
		"INSERT INTO StudentData (ROLLNO, FNAME, LNAME) VALUES(1915105, 'Amanjot', 'Singh');"
	);

	int exit = sqlite3_open(s, &DB);
	/* An open database, SQL to be evaluated, Callback function, 1st argument to callback, Error msg written here */
	exit = sqlite3_exec(DB, sql.c_str(), NULL, 0, &messageError);
	if (exit != SQLITE_OK) {
		cerr << "Error in insertData function." << endl;
		sqlite3_free(messageError);
	}
	else
		cout << "Records inserted Successfully!" << endl;

	return 0;
}

static int updateData(const char* s)
{
	sqlite3* DB;
	char* messageError;

	string sql("UPDATE GRADES SET GRADE = 'A' WHERE LNAME = 'Cooper'");

	int exit = sqlite3_open(s, &DB);
	/* An open database, SQL to be evaluated, Callback function, 1st argument to callback, Error msg written here */
	exit = sqlite3_exec(DB, sql.c_str(), NULL, 0, &messageError);
	if (exit != SQLITE_OK) {
		cerr << "Error in updateData function." << endl;
		sqlite3_free(messageError);
	}
	else
		cout << "Records updated Successfully!" << endl;

	return 0;
}

static int deleteData(const char* s)
{
	sqlite3* DB;
	char* messageError;

	string sql = "DELETE FROM GRADES;";

	int exit = sqlite3_open(s, &DB);
	/* An open database, SQL to be evaluated, Callback function, 1st argument to callback, Error msg written here */
	exit = sqlite3_exec(DB, sql.c_str(), callback, NULL, &messageError);
	if (exit != SQLITE_OK) {
		cerr << "Error in deleteData function." << endl;
		sqlite3_free(messageError);
	}
	else
		cout << "Records deleted Successfully!" << endl;

	return 0;
}

static int selectData(const char* s)
{
	sqlite3* DB;
	char* messageError;

	string sql = "SELECT * FROM StudentData;";

	int exit = sqlite3_open(s, &DB);
	/* An open database, SQL to be evaluated, Callback function, 1st argument to callback, Error msg written here*/
	exit = sqlite3_exec(DB, sql.c_str(), callback, NULL, &messageError);

	if (exit != SQLITE_OK) {
		cerr << "Error in selectData function." << endl;
		sqlite3_free(messageError);
	}
	else
		cout << "Records selected Successfully!" << endl;

	return 0;
}

// retrieve contents of database used by selectData()
/* argc: holds the number of results, argv: holds each value in array, azColName: holds each column returned in array, */
static int callback(void* NotUsed, int argc, char** argv, char** azColName)
{for (int i = 0; i < argc; i++) {
		// column name and value
		cout << azColName[i] << ": " << argv[i] << endl;
	}

	cout << endl;

	return 0;
}
