#include <iostream>
#include <fstream>
#include <filesystem>
#include <string>

using namespace std;
namespace fs = std::filesystem;

string getAuthFilePath(const string& project_id, const string& email) {
    return "DB_USER/projects/" + project_id + "/cret/"+ email + ".cfg";
}

bool userExists(const string& email, const string& project_id) {
    ifstream authFile(getAuthFilePath(project_id, email));
    string line;
    while (getline(authFile, line)) {
        if (line.find(email + ":") == 0) return true;
    }
    return false;
}

void createUser(const string& email, const string& password, const string& project_id) {
    if (userExists(email, project_id)) {
        cout << "User already exists!" << endl;
        return;
    }

    ofstream authFile(getAuthFilePath(project_id, email), ios::app);
    if (authFile.is_open()) {
        authFile << password << endl;
        cout << "User created successfully!" << endl;
    } else {
        cerr << "Error: Unable to open auth file!" << endl;
    }
}

void signInUser(const string& email, const string& password, const string& project_id) {
    string authPath = getAuthFilePath(project_id, email);

    if (!fs::exists(authPath)) {
        cout << "Email is invalid!" << endl;
        return;
    }

    ifstream authFile(authPath);
    if (!authFile.is_open()) {
        cerr << "Error: Unable to open auth file!" << endl;
        return;
    }

    string storedPassword;
    getline(authFile, storedPassword);
    authFile.close();

    if (storedPassword == password) {
        cout << "Logged in successfully!" << endl;
    } else {
        cout << "Wrong password!" << endl;
    }
}

void deleteUser(const string& email, const string& project_id) {
    string authPath = getAuthFilePath(project_id, email);
    {
        ifstream authFile(authPath);
        if (!authFile.is_open()) {
            cerr << "Error: Unable to open auth file!" << endl;
            return;
        }
    } 
    if (fs::remove(authPath)) {
        cout << "User deleted successfully!" << endl;
    } else {
        cerr << "Error: Unable to delete auth file!" << endl;
        return;
    }
}

int main(int argc, char* argv[]) {
    if (argc < 4) {
        cerr << "Usage:\n";
        cerr << "createUser <email> <password> <project_id>\n";
        cerr << "signInUser <email> <password> <project_id>\n";
        cerr << "deleteUser <email> <project_id>\n";
        return 1;
    }

    string command = argv[1];

    if (command == "createUser" && argc == 5) {
        createUser(argv[2], argv[3], argv[4]);
    } else if (command == "signInUser" && argc == 5) {
        signInUser(argv[2], argv[3], argv[4]);
    } else if (command == "deleteUser" && argc == 4) {
        deleteUser(argv[2], argv[3]);
    } else {
        cerr << "Invalid command or arguments!" << endl;
        return 1;
    }

    return 0;
}
