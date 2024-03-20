import pandas as pd

employees_df = pd.DataFrame(
    {'employee_id': [101, 102, 103, 104, 105], 'name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma'],
     'department_id': [1, 2, 1, 2, 3]})

departments_df = pd.DataFrame(
    {'department_id': [1, 2, 3], 'department_name': ['HR', 'IT', 'Finance'],
     'location': ['New York', 'San Francisco', 'Chicago']})

merged_df = employees_df.merge(departments_df, on="department_id")
print(merged_df)

merged_df = pd.merge(left=departments_df,right=employees_df,  on="department_id")
print(merged_df)

employees_df.set_index("department_id", inplace=True)
departments_df.set_index("department_id", inplace=True)
join = employees_df.join(departments_df)
print(join)

print(join[:1])
print(merged_df[:1])
