# 📦 Inventory Management System
**By Manveer Makkar **

A Python-based command-line Inventory Management System integrated with a MySQL database. This project allows employees to **view, insert, update, and delete** inventory records across multiple product categories in real time.

---

## 🗂️ Project Structure

```
Inventory Management System/
│
├── Manveer.py          # Database setup script (run once to initialize DB)
└── program.py            # Main application file (run to use the system)
```

---

## 🛠️ Technologies Used

| Technology     | Purpose                          |
|----------------|----------------------------------|
| Python 3.x     | Core programming language        |
| MySQL          | Relational database management   |
| mysql-connector-python | Python–MySQL bridge     |

---

## ⚙️ Setup & Installation

### Prerequisites
- Python 3.x installed
- MySQL Server installed and running
- `mysql-connector-python` library installed

### Install the required library
```bash
pip install mysql-connector-python
```

### Step 1: Configure Database Credentials
Open both `Manveer.py` and `func2.py` and update the connection settings to match your MySQL credentials:
```python
m = ms.connect(
    host="localhost",
    user="root",
    password="your_password",   # ← change this
    database="INVENTORY__ITEMS1"
)
```

### Step 2: Initialize the Database
Run `Manveer.py` **once** to create the database, all tables, and populate them with sample data:
```bash
python Manveer.py
```
> ⚠️ Run this script only once. Re-running it will throw errors since the database and tables already exist.

### Step 3: Launch the Application
```bash
python func2.py
```

---

## 🚀 Features

### 👤 User Authentication (Employee Entry)
- Prompts the user to enter their **Name** and **Employee ID** before accessing the system.
- Asks for **confirmation** before proceeding — re-entry is requested if details are incorrect.
- Ensures only verified personnel interact with inventory data.

### 📋 View Inventory
- Displays all available **inventory categories** (tables) from the database.
- Allows the user to select a category by its **ID** to view all items in it.
- Shows complete records including SID, Product Name, Quantity, and Price.

### ➕ Insert Items
- Lets the user choose a category to add a new product.
- Accepts inputs for **SID, Product Name, Quantity, and Price**.
- Validates that the data types and format are correct before inserting.
- Confirms successful insertion or displays a detailed error message on failure.

### ✏️ Update Items
- Allows updating an existing record in any inventory category.
- User selects the category, then provides the **SID** of the item to update.
- Accepts new values for **Product Name, Quantity, and Price**.
- Changes are committed to the database upon success.

### 🗑️ Delete Items
- Enables deletion of a specific record from any inventory category.
- User selects the table and then the **SID** of the item to remove.
- Permanently deletes the record from the database after confirmation.

### 🔁 Input Validation & Error Handling
- All operations include **try-except** error handling.
- On invalid input (wrong ID, wrong data type, etc.), the system prints a clear error message and **prompts the user to try again** — no crashes.
- Recursive re-prompting ensures the program keeps running until a valid action is completed.

---

## 🗄️ Database Schema

### Database Name: `INVENTORY__ITEMS1`

#### CATEGORY (Master Table)
| Column     | Type        | Description              |
|------------|-------------|--------------------------|
| ID         | VARCHAR(5)  | Primary Key (e.g., ID1)  |
| TABLE_NAME | VARCHAR(50) | Name of the linked table |

#### sports_inventory
| Column       | Type           |
|--------------|----------------|
| SID          | VARCHAR(5) PK  |
| product_name | VARCHAR(255)   |
| quantity     | INT            |
| price        | DECIMAL(10,2)  |

> The same schema applies to: `clothing_inventory`, `techdevices_inventory`, `furniture_inventory`, `groceries_inventory`

---

## 📁 Inventory Categories

| Category ID | Table Name              | Sample Items                        |
|-------------|-------------------------|-------------------------------------|
| ID1         | sports_inventory        | Football, Cricket Bat, Golf Clubs   |
| ID2         | clothing_inventory      | T-Shirt, Jeans, Jacket              |
| ID3         | techdevices_inventory   | Laptop, Smartphone, Gaming Console  |
| ID4         | furniture_inventory     | Sofa, Bed, Wardrobe                 |
| ID5         | groceries_inventory     | Rice, Milk, Fresh Fruits            |

Each category contains **10 pre-loaded sample records**.

---

## 🖥️ How to Use

```
Welcome to INVENTORY MANAGEMENT SYSTEM by Manveer Makkar (12th A, FAS)!!!

ENTER USER DETAILS BELOW:
ENTER YOUR NAME: John
ENTER EMPLOYEE ID: E101

NAME- John
EmployeeID- E101
Please confirm your details (Y/N): Y

1 - VIEW ITEMS OF AN INVENTORY
2 - INSERT ITEMS OF AN INVENTORY
3 - UPDATE ITEMS OF AN INVENTORY
4 - DELETE ITEMS OF AN INVENTORY

SELECT THE RESPECTIVE NUMBER FOR PERFORMING THE TASK: _
```

---

## 📌 Important Notes

- **SID format** must match the category prefix (e.g., `S1`–`S10` for Sports, `C1`–`C10` for Clothing).
- **Price** must be a decimal number with up to 2 decimal places (e.g., `29.99`).
- **Quantity** must be a whole number (integer).
- **Product names** are alphanumeric strings.

---

## 🔮 Possible Future Enhancements

- Add a GUI using Tkinter or a web interface using Flask.
- Implement login/authentication with hashed passwords.
- Add search and filter functionality by product name or price range.
- Generate inventory reports (PDF/Excel export).
- Add low-stock alerts when quantity falls below a threshold.

---

## 👨‍💻 Author

**Manveer Makkar**
Class 12th A, FAS
