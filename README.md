Finance Tracker for Students
 Overview
Finance Tracker for Students is a web-based application designed to help students manage their finances effectively. The app allows users to log expenses, set financial goals, view expense history, and access resources for stress management. It also includes a community dashboard for engaging with other users.

 Features
User Authentication: Secure login and registration system.
Expense Logging: Keep track of daily expenses.
Financial Goals: Set and monitor financial goals.
Expense History: View past expense records.
Community Dashboard: Interact with other users for advice and tips.
Stress Management Resources: Access tips and techniques to manage stress related to finances.

Project Structure
The project contains the following main directories and files:
 1. Code File
app.py: Main application file to run the Flask app.
SQL Database: Stores user data, expenses, and goals.
2. Static Folder
Contains the static assets for the application:
script.js: Contains JavaScript code for dynamic behavior.
styles.css: Contains CSS for styling the application.
3. Templates Folder
Contains HTML templates used by the Flask application:
community.html: Community interaction page.
dashboard.html: User dashboard displaying key financial insights.
goals.html: Page for setting and viewing financial goals.
history.html: Page to view expense history.
log_expenses.html: Form to log daily expenses.
login.html: Login page.
register.html: Registration page.
stress_management.html: Financial tips for students.

Installation
1. Clone the Repository
git clone https://github.com/DhanviMohanraj/finance-tracker-students.git
cd finance-tracker-students
2. Set Up Virtual Environment
python -m venv venv
source venv/bin/activate   # On Windows, use venv\Scripts\activate
3. Set Up the Database
   Ensure the SQL database schema is created.
   Use a migration tool like Flask-Migrate or manually create tables.
4. Run the Application
   python app.py
5. Access the App
   Open your browser and go to http://127.0.0.1:5000.
(Apps preferred to run the code: VS Code, PyCharm)


 Usage
Register an account or log in if you already have one.
Navigate to the dashboard to view an overview of your finances.
Log your daily expenses via the Log Expenses page.
Set and track financial goals on the Goals page.
Review your past expenses on the History page.
Engage with the community via the Community page.

Contact
For questions or feedback, please contact:
Dhanvi Mohanraj (dhanvimohanraj00@gmail.com)
Gopika R (gopikasg07@gmail.com)                                                                                                                                                                                                        Consider the files under templates and static and also app.py, the other files are not the correct codes for the website as it was trial and error purpose.
