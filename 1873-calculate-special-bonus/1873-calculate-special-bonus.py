import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    bonus = []
    for i in range(len(employees)):
        if employees['employee_id'].loc[i] %2 and employees['name'].loc[i][0] != 'M':
            bonus.append(employees['salary'].loc[i])
        else:
            bonus.append(0)
    employees['bonus'] = bonus
    df = employees[['employee_id', 'bonus']]
    df = df.sort_values(by = ['employee_id'])
    return df