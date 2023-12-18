import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee.drop_duplicates(subset = ['salary'], inplace = True)
    if len(employee) < N:
        val = None
    else:
        df = employee.sort_values( by = ['salary'], ascending = False)
        val = df.iloc[N-1]['salary']
    name = 'getNthHighestSalary(' + str(N) + ')'
    return pd.DataFrame({name: [val,]})

