import pandas as pd
import sqlite3


def convert_to_rubles(row):
    if pd.notna(row['salary_from']):
        if row['salary_currency'] == 'RUR':
            return row['salary_from']
        else:
            exchange_rate_column = row['salary_currency']
            rubles_salary = row['salary_from'] * exchange_rates_df.iloc[0][
                exchange_rate_column]
            return rubles_salary
    else:
        return None


database_name = input()
csv_file = input()
table_name = input()
currency_table = input()

con = sqlite3.connect(database_name)
cur = con.cursor()

vacancies_df = pd.read_csv(csv_file)
exchange_rates_df = pd.read_sql(f'SELECT * FROM {currency_table};', con)

vacancies_df['published_at'] = pd.to_datetime(vacancies_df['published_at'])

# Применение функции для преобразования зарплаты в рубли
vacancies_df['salary_from'] = vacancies_df.apply(convert_to_rubles, axis=1)

# Расчет средней зарплаты
average_salary = vacancies_df['salary_from'].mean()
if pd.notna(average_salary):
    average_salary = round(average_salary)

vacancies_df.rename(columns={'salary_from': 'salary'})
vacancies_df.drop(
    ['description', 'key_skills', 'experience_id', 'employer_name', 'premium',
     'salary_to', 'salary_gross', 'salary_currency'], axis=1)
vacancies_df.to_sql(name=table_name, con=con, if_exists='fail', index=False)

con.close()