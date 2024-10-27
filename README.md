
# Personal Budget Analyzer (PBA)

## Overview

Personal Budget Analyzer (PBA) is a Python application that allows users to manage their monthly budget, analyze expenditures, and view historical data. Users can sign up, log in, and compare their actual expenditures against predefined budgets. This project uses MySQL as the database to store user accounts, budget plans, and expenditure data.

## Features

- User sign-up and login system.
- Create and manage budget plans.
- Compare monthly expenses with budgeted amounts.
- View past budget and expenditure reports.
- Visual analysis with bar graphs (using Matplotlib).

## Requirements

- **Python 3.x**
- **MySQL** (MySQL server)
- **MySQL Connector for Python**
- **Matplotlib** (for graphs)
- **Numpy** (for data manipulation)

---

## Installation

### Ubuntu

#### 1. Clone the Repository

```bash
git clone <repository-url>
cd <repository-folder>
```

#### 2. Install Dependencies

Before running the project, ensure you have the required dependencies:

```bash
sudo apt update
sudo apt install python3-pip
pip3 install mysql-connector-python numpy matplotlib
```

#### 3. Install MySQL Server

If you don't have MySQL installed, use the following command to install it:

```bash
sudo apt install mysql-server
```

Once installed, secure the MySQL installation:

```bash
sudo mysql_secure_installation
```

#### 4. Set Up the MySQL Database

Open the MySQL terminal and create the necessary database and user:

```bash
sudo mysql -u root -p
```

In the MySQL terminal, run the following commands to create the `PBA` database and set the root password (if not done already):

```sql
CREATE DATABASE IF NOT EXISTS PBA;
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '5100';
```

#### 5. Configure MySQL for Your Project

Ensure the MySQL server is running:

```bash
sudo systemctl start mysql
```

If you need to restart the MySQL service:

```bash
sudo systemctl restart mysql
```

#### 6. Running the Application

After setting up the MySQL database, you can run the Python script. Ensure you’re in the project directory, then execute:

```bash
python3 pba.py
```

The script will prompt you to sign up or log in and guide you through managing your budgets.

---

### Windows

#### 1. Download and Install Python 3

Download the latest version of Python 3 from the official website: [Python Downloads](https://www.python.org/downloads/)

Ensure that you check the option **Add Python to PATH** during installation.

#### 2. Install MySQL

Download and install MySQL for Windows from the official MySQL website: [MySQL Installer for Windows](https://dev.mysql.com/downloads/installer/)

During installation, ensure that you set up MySQL with the following credentials (or modify these in your script later):
- **Username**: `root`
- **Password**: `5100`

#### 3. Set Up MySQL Database

Once MySQL is installed, open the **MySQL Command Line Client** and run the following commands to create the database and set the password:

```sql
CREATE DATABASE IF NOT EXISTS PBA;
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '5100';
```

#### 4. Install Python Libraries

Open **Command Prompt** and install the required Python libraries:

```bash
pip install mysql-connector-python numpy matplotlib
```

#### 5. Running the Application

After setting up the database and installing dependencies, navigate to the project folder and run the script:

```bash
python pba.py
```

The script will prompt you to sign up or log in and guide you through managing your budgets.

---

## Usage

1. **Sign Up**: Create an account by providing a username, password, and email.
2. **Budget Plan**: Set up budget plans for different areas (groceries, utilities, etc.).
3. **Monthly Analysis**: Compare your expenses to your set budget and visualize the data with charts.
4. **Account Settings**: Change your account details such as username, password, and salary.

---

## File Structure

- `pba.py`: The main Python script that contains the logic for the PBA application.
- `README.md`: Documentation file.

---

## Troubleshooting

### Ubuntu

- **MySQL Connection Issues**: Ensure that the MySQL service is running. You can check the status with:

  ```bash
  sudo systemctl status mysql
  ```

- **Python Module Issues**: If you encounter issues with missing Python modules, ensure all dependencies are installed via pip.

### Windows

- **PATH Issues**: Ensure Python is added to the system PATH. You can check this by running `python --version` in the Command Prompt.
  
- **MySQL Connection Issues**: Ensure that the MySQL service is running. If it’s not, you can start it via the **MySQL Workbench** or from the Windows Services menu.

---

## Dependencies

- `mysql-connector-python`: For connecting Python to MySQL.
- `numpy`: For array handling.
- `matplotlib`: For creating graphs.
- `statistics`: Built-in Python library for statistical calculations.

---

## License

This project is open-source. Feel free to use, modify, and distribute it as per your needs.

---
