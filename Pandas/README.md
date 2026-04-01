# Pandas Tutorial

This folder contains comprehensive tutorials and examples for learning **Pandas**, a powerful Python library for data manipulation and analysis.

## 📁 Contents

### Files
- **pandas_tutorial.ipynb** - Main Jupyter notebook with complete tutorials covering:
  - Creating DataFrames from different data sources
  - Exploring DataFrame structure
  - Accessing and retrieving data
  - Filtering and selecting data
  - Sorting, grouping, and aggregation
  - Data cleaning and handling missing values
  - Working with rows and columns

## 🎯 What You'll Learn

### 1. **DataFrame Creation**
   - From dictionaries
   - From lists
   - From random data (using NumPy)
   - Understanding different creation methods

### 2. **Data Exploration**
   - `.shape()` - Get dimensions
   - `.info()` - Data types and memory usage
   - `.head()` / `.tail()` - View first/last rows
   - `.describe()` - Statistical summary
   - `.dtypes` - Column data types

### 3. **Data Access**
   - Column selection using bracket notation `[]`
   - Row access using `.iloc[]` and `.loc[]`
   - Specific value retrieval
   - Series vs DataFrame distinction

### 4. **Data Filtering**
   - Boolean indexing
   - Simple conditions (`==`, `>`, `<`, etc.)
   - Compound conditions using `&` (AND) and `|` (OR)
   - `.isin()` method for multiple values
   - `.query()` method with SQL-like syntax

### 5. **Data Operations**
   - **Sorting**: `.sort_values()`
   - **Grouping**: `.groupby()`
   - **Aggregation**: `.agg()` with multiple functions
   - **Mathematical operations**: Creating new columns with calculations

### 6. **Data Cleaning**
   - Checking for missing values: `.isnull()` / `.isna()`
   - Filling missing values: `.fillna()`
   - Handling duplicates: `.duplicated()` / `.drop_duplicates()`
   - Type conversion: `.astype()`

### 7. **DataFrame Manipulation**
   - Adding new columns
   - Renaming columns: `.rename()`
   - Dropping columns: `.drop()`
   - Reordering columns
   - Adding/removing rows
   - Resetting index: `.reset_index()`

## 🚀 Getting Started

### Prerequisites
- Python 3.7+
- pandas library (`pip install pandas`)
- numpy library (`pip install numpy`)
- Jupyter/Jupyter Lab

### Installation
```bash
pip install pandas numpy jupyter
```

### Running the Notebook
1. Open Jupyter Notebook or Jupyter Lab
2. Navigate to the Pandas folder
3. Open `pandas_tutorial.ipynb`
4. Run cells sequentially to follow along

## 💡 Key Concepts

### DataFrame vs Series
- **DataFrame**: 2D table with rows and columns
- **Series**: 1D array with a single column

### Indexing vs Selection
- **iloc[]**: Index location (position-based) - 0-indexed
- **loc[]**: Label location (label-based)

### Important Methods
| Method | Purpose |
|--------|---------|
| `.shape` | Get DataFrame dimensions |
| `.info()` | Information about DataFrame |
| `.head()` | View first rows |
| `.describe()` | Statistical summary |
| `.groupby()` | Group data by column values |
| `.sort_values()` | Sort by column |
| `.fillna()` | Fill missing values |
| `.drop()` | Remove rows/columns |

## 📚 Practice Exercises

Try these exercises to reinforce your learning:

1. **Create Sample Data**: Create a DataFrame with 10+ rows representing students with columns for name, age, grade, and marks.

2. **Filter and Aggregate**: 
   - Find students with marks > 75
   - Calculate average marks by grade

3. **Data Cleaning**: Remove duplicate entries and handle missing values

4. **DataFrame Operations**:
   - Add a column for percentage
   - Sort by marks in descending order
   - Group students by grade and find the best performer in each grade

## 🔗 Additional Resources

- [Pandas Official Documentation](https://pandas.pydata.org/)
- [Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
- [Data Analysis with Pandas](https://www.datacamp.com/courses/intro-to-python-for-data-science)

## 📝 Notes

- All examples use dummy/sample data for learning purposes
- Comments are included in the notebook to explain each operation
- Examples progress from basic to more advanced concepts
- Code is well-documented and easy to follow

## ✅ Checklist

As you progress through the tutorial, mark these off:

- [ ] Understand DataFrame creation methods
- [ ] Master data access techniques
- [ ] Can filter data with multiple conditions
- [ ] Comfortable with grouping and aggregation
- [ ] Know how to handle missing values
- [ ] Can manipulate rows and columns effectively
- [ ] Can combine multiple operations for data analysis

---

**Happy Learning!** 🎓

Feel free to modify the examples and experiment with your own data as you work through the tutorial.
