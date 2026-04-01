# SQL Tutorial

This folder contains a comprehensive guide to **SQL (Structured Query Language)**, the standard language for managing relational databases.

## 📁 Contents

### Files
- **sql_tutorial.ipynb** - Complete SQL tutorial notebook with hands-on examples

## 🎯 What You'll Learn

### 1. **Database Fundamentals**
   - Setting up SQLite database
   - Creating and managing tables
   - Understanding primary keys and constraints

### 2. **Data Insertion**
   - INSERT statements for single rows
   - Batch inserting multiple rows
   - Understanding different insert methods

### 3. **SELECT Queries**
   - Retrieving all columns and specific columns
   - Using column aliases
   - DISTINCT keyword for unique values
   - COUNT, LIMIT operations

### 4. **Filtering Data**
   - WHERE clauses with various conditions
   - Comparison operators (=, >, <, >=, <=, !=)
   - Logical operators (AND, OR)
   - IN operator for list matching
   - BETWEEN for range queries
   - LIKE for pattern matching
   - IS NULL / IS NOT NULL checks

### 5. **Sorting and Pagination**
   - ORDER BY ascending/descending
   - Sorting by multiple columns
   - LIMIT for limiting results
   - OFFSET for pagination

### 6. **Functions**
   - **String Functions**: UPPER(), LOWER(), LENGTH(), SUBSTR(), Concatenation
   - **Numeric Functions**: ABS(), ROUND(), MIN(), MAX(), AVG(), SUM()
   - **Aggregate Functions**: COUNT(), AVG(), SUM(), MIN(), MAX()

### 7. **Grouping and Aggregation**
   - GROUP BY clause
   - Multiple aggregates in one query
   - HAVING clause for filtering grouped results
   - GROUP BY multiple columns

### 8. **JOIN Operations**
   - INNER JOIN - matching records from both tables
   - LEFT JOIN - all records from left table
   - Advanced JOINs with aggregation
   - Multiple table joins

### 9. **Subqueries**
   - Scalar subqueries in WHERE clause
   - IN subqueries
   - Correlated subqueries
   - Derived tables / Table subqueries
   - EXISTS clause

### 10. **Data Modification**
   - UPDATE statements (single and multiple columns)
   - UPDATE with WHERE conditions
   - UPDATE with calculations
   - DELETE statements with safety warnings

### 11. **Data Types and Constraints**
   - INTEGER, DECIMAL, TEXT, DATE, BOOLEAN, etc.
   - PRIMARY KEY - unique row identifier
   - UNIQUE - ensure uniqueness
   - NOT NULL - mandatory values
   - DEFAULT - default values
   - CHECK - conditional validation
   - FOREIGN KEY - table relationships
   - AUTO_INCREMENT - automatic numbering

## 📊 Sample Database

The tutorial uses three sample tables:

### **Employees Table**
- EmployeeID (Primary Key)
- FirstName, LastName
- Email (Unique)
- Department
- Salary
- HireDate
- IsActive (Boolean)

### **Departments Table**
- DepartmentID (Primary Key)
- DepartmentName
- Location
- Manager

### **Projects Table**
- ProjectID (Primary Key)
- ProjectName
- Department
- Budget
- StartDate, EndDate
- Status

## 🚀 Getting Started

### Prerequisites
- Python 3.6+
- pandas library (`pip install pandas`)
- sqlite3 (included with Python)
- Jupyter Notebook or Jupyter Lab

### Installation
```bash
pip install pandas jupyter
```

### Running the Notebook
1. Open Jupyter Notebook or Jupyter Lab
2. Navigate to the SQL folder
3. Open `sql_tutorial.ipynb`
4. Run cells sequentially to follow along

## 📝 Key SQL Concepts

### Query Execution Order
```sql
SELECT      -- 5. Final result columns
FROM        -- 1. Table to query
WHERE       -- 2. Filter rows
GROUP BY    -- 3. Group rows
HAVING      -- 4. Filter groups
ORDER BY    -- 6. Sort results
LIMIT       -- 7. Limit output
```

### Common Query Patterns

**Find records matching criteria:**
```sql
SELECT * FROM Employees 
WHERE Department = 'IT' AND Salary > 60000;
```

**Group and aggregate:**
```sql
SELECT Department, AVG(Salary), COUNT(*) 
FROM Employees 
GROUP BY Department;
```

**Join multiple tables:**
```sql
SELECT e.Name, d.DepartmentName 
FROM Employees e
INNER JOIN Departments d ON e.Department = d.DepartmentName;
```

**Subquery in WHERE:**
```sql
SELECT * FROM Employees 
WHERE Salary > (SELECT AVG(Salary) FROM Employees);
```

## 💡 Best Practices

### Do's ✓
- Always use WHERE clause with UPDATE/DELETE
- Use meaningful names for databases, tables, columns
- Use constraints to ensure data integrity
- Use proper data types for efficiency
- Test queries before running on production data
- Use LIMIT when testing queries on large datasets
- Use indexing on frequently queried columns

### Don'ts ✗
- Don't use `SELECT *` in production without specific need
- Don't forget WHERE clause in DELETE/UPDATE
- Don't mix data types in comparisons
- Don't create overly complex queries (break into simpler ones)
- Never delete data without backing it up first
- Avoid using SQL keywords as column names

## 🔗 Important Commands Quick Reference

| Command | Purpose | Example |
|---------|---------|---------|
| CREATE TABLE | Create new table | `CREATE TABLE Users (ID INT, Name TEXT)` |
| INSERT | Add data | `INSERT INTO Users VALUES (1, 'Alice')` |
| SELECT | Retrieve data | `SELECT * FROM Users` |
| WHERE | Filter rows | `SELECT * FROM Users WHERE Age > 18` |
| UPDATE | Modify data | `UPDATE Users SET Age=30 WHERE ID=1` |
| DELETE | Remove data | `DELETE FROM Users WHERE ID=1` |
| GROUP BY | Group rows | `SELECT Department, COUNT(*) FROM Employees GROUP BY Department` |
| JOIN | Combine tables | `SELECT * FROM A JOIN B ON A.ID = B.ID` |
| ORDER BY | Sort data | `SELECT * FROM Users ORDER BY Name DESC` |
| LIMIT | Limit results | `SELECT * FROM Users LIMIT 10` |

## 🎓 Learning Path

1. Start with **Section 1-2**: Understand database setup and table creation
2. Progress to **Section 3-5**: Learn CRUD operations (Create, Read, Update, Delete)
3. Move to **Section 6-7**: Master sorting and functions
4. Study **Section 8-9**: Understand data aggregation and grouping
5. Learn **Section 10-11**: Master JOINs and subqueries
6. Review **Section 12-13**: Practice updates, deletes, and understand constraints

## 🔍 SQL vs Pandas Comparison

| Operation | SQL | Pandas |
|-----------|-----|--------|
| Load data | SELECT * | df.read_csv() |
| Filter | WHERE | df[df['col'] > value] |
| Group & Aggregate | GROUP BY | df.groupby() |
| Sort | ORDER BY | df.sort_values() |
| Merge tables | JOIN | pd.merge() |
| Get unique | DISTINCT | df.unique() |

## ✅ Expected Learning Outcomes

After completing this tutorial, you'll be able to:
- ✓ Create and design relational databases
- ✓ Write efficient SELECT queries with complex filtering
- ✓ Use JOINs to combine data from multiple tables
- ✓ Perform aggregations and statistical calculations
- ✓ Use subqueries for advanced data retrieval
- ✓ Update and delete data safely
- ✓ Understand and apply database constraints
- ✓ Optimize queries and understand execution order
- ✓ Write clean, readable SQL code

## 🤔 Common Questions

**Q: What's the difference between WHERE and HAVING?**
A: WHERE filters individual rows before grouping, HAVING filters groups after aggregation.

**Q: When should I use subqueries vs JOINs?**
A: JOINs are usually faster, but subqueries are sometimes more readable. Test both.

**Q: How do I avoid deleting wrong data?**
A: Always test your WHERE clause with a SELECT first to see which rows match.

**Q: Is SQL the same across all databases?**
A: Core SQL is similar, but syntax varies (PostgreSQL, MySQL, SQL Server, SQLite differ).

## 📚 Additional Resources

- [SQLite Official Documentation](https://sqlite.org/docs.html)
- [SQL Tutorial by W3Schools](https://www.w3schools.com/sql/)
- [Mode Analytics SQL Tutorial](https://mode.com/sql-tutorial/)
- [LeetCode Database Problems](https://leetcode.com/problemset/database/)

## 📝 Practice Challenges

Try these exercises to reinforce your learning:

1. **Beginner**: Find all employees in the IT department with salary > 50000
2. **Intermediate**: Find the department with the highest average salary
3. **Advanced**: Find employees who work on projects with budget > 60000 AND earn more than department average
4. **Expert**: Create a query showing each employee, their department, projects assigned, and project budget percentage of total department budget

---

**Happy Learning!** 🎉

Feel free to modify the data and experiment with different queries as you work through the tutorial. SQL is best learned by doing!
