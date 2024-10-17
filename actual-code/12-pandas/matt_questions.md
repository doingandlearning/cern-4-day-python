### **1. Reading data without column names and assigning names on read**
You can specify column names during reading using the `names` parameter in `pandas.read_csv()` if your file doesn't have a header row.

```python
import pandas as pd

# Assign column names while reading the CSV
column_names = ['Column1', 'Column2', 'Column3']
df = pd.read_csv('data.csv', header=None, names=column_names)

# Display the DataFrame
print(df)
```

### **2. Handling a file with intro text and unnamed CSV data**
You can skip the introductory lines using the `skiprows` parameter, and then manually assign column names to the CSV data.

```python
import pandas as pd

# Example: Skip the first 'x' lines of the file to reach the CSV data
column_names = ['Column1', 'Column2', 'Column3']
df = pd.read_csv('data_with_intro.csv', skiprows=5, header=None, names=column_names)

# Display the DataFrame
print(df)
```

In both examples, `header=None` ensures that pandas doesn't treat the first row as column headers, and `names` allows you to manually specify the column names.