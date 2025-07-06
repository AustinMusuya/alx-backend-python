## 🐍 MySQL Seeder and Row Streaming Generator

This project sets up a MySQL database, populates it with sample user data from a CSV file, and includes a Python generator that streams each row from the database one at a time.

### ✅ Features

- Connects to MySQL server using `mysql-connector-python`
- Creates a database `ALX_prodev` if it doesn't exist
- Creates a `user_data` table with:

  - `user_id` (UUID, Primary Key, Indexed)
  - `name` (VARCHAR, NOT NULL)
  - `email` (VARCHAR, NOT NULL)
  - `age` (DECIMAL, NOT NULL)

- Loads data from a `user_data.csv` file
- Streams user data row-by-row using a generator

---

### 📂 File Structure

```
.
├── seed.py           # Core logic for DB connection, table creation, data insert, and generator
├── 0-main.py         # Entry script that uses seed.py
└── user_data.csv     # Sample user data
```

---

### 📝 Function Prototypes

```python
def connect_db() -> connection
def create_database(connection) -> None
def connect_to_prodev() -> connection
def create_table(connection) -> None
def insert_data(connection, csv_file: str) -> None
def stream_user_data(connection) -> Generator[Dict, None, None]
```

---

### 📝 Example CSV Format

```csv
name,email,age
Alice Johnson,alice@example.com,30
Bob Smith,bob@example.com,45
Charlie Brown,charlie@example.com,27
```

---

### 🚀 Usage

```bash
# Run the script
chmod +x 0-main.py
./0-main.py
```

Sample output:

```
✅ Database ALX_prodev created or already exists.
✅ Table user_data created or already exists.
✅ CSV data inserted successfully.

Streaming rows from user_data:
{'user_id': '...', 'name': 'Alice Johnson', 'email': 'alice@example.com', 'age': Decimal('30')}
{'user_id': '...', 'name': 'Bob Smith', 'email': 'bob@example.com', 'age': Decimal('45')}
...
```

---

### 📦 Requirements

- Python 3.x
- `mysql-connector-python`
- MySQL Server 8.0+ (or 8.4 LTS)

Install dependencies:

```bash
pip install mysql-connector-python
```

---

Let me know if you want to extend this with pagination, search filters, or SQLAlchemy support.
