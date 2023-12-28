import pandas as pd
import sqlite3


database_name = input()
table_name = input()
vac_name = input()

con = sqlite3.connect(database_name)
cur = con.cursor()

'''Динамика уровня зарплат по годам (для решения рекомендуется использовать следующие SQL-операторы: ROUND, AVG, GROUP BY, а также функцию SQLite для работы с датой и временем - strftime). Переменную необходимо назвать df_years_salary. Столбцы:

Год - год публикации
Средняя з/п - средняя зарплата'''
df_years_salary = pd.read_sql(
		f"""SELECT strftime('%Y', published_at) AS `Год`, ROUND(AVG(salary), 2) AS `Средняя з/п` 
		FROM {table_name}		
		GROUP BY 1
		ORDER BY 1;""",
	con)

'''Динамика количества вакансий по годам. Переменная df_years_count. Столбцы:

Год - год публикации
Количество вакансий - количество вакансий за этот год'''
df_years_count = pd.read_sql(
		f"""SELECT strftime('%Y', published_at) AS `Год`, COUNT(DISTINCT name) AS `Количество вакансий` 
		FROM {table_name}		
		GROUP BY 1
		ORDER BY 1;""",
	con)

'''
Динамика уровня зарплат по годам для выбранной профессии (для решения рекомендуется использовать следующие SQL-операторы: ROUND, AVG, WHERE, LIKE, GROUP BY, а также функцию strftime). Переменная df_years_salary_vac. Столбцы:

Год - год публикации
Средняя з/п - *название вакансии* - средняя зарплата выбранной вакансии'''
df_years_salary_vac = pd.read_sql(
		f"""SELECT strftime('%Y', published_at) AS `Год`, ROUND(AVG(salary), 2) AS `Средняя з/п - {vac_name}` 
		FROM {table_name}	
		WHERE name='{vac_name}'	
		GROUP BY 1
		ORDER BY 1;""",
	con)

'''Динамика количества вакансий по годам для выбранной профессии. Переменная df_years_count_vac. Столбцы:

Год - год публикации
Количество вакансий - *название вакансии* - количество вакансий выбранной вакансии'''
df_years_count_vac = pd.read_sql(
		f"""SELECT strftime('%Y', published_at) AS `Год`, COUNT(DISTINCT name) AS `Количество вакансий - {vac_name}` 
		FROM {table_name}		
		WHERE name='{vac_name}'
		GROUP BY 1
		ORDER BY 1;""",
	con)

'''Уровень зарплат по городам (в порядке убывания) - только первые 10 значений (для решения рекомендуется использовать вложенные запросы, SQL-операторы: ROUND, AVG, GROUP BY, HAVING, а также функцию strftime). Переменная df_area_salary. Столбцы:

Город - название города
Уровень зарплат по городам - среднее значение зарплаты. Округлить до двух символов после запятой.'''
df_area_salary = pd.read_sql(
		f"""SELECT area_name AS `Город`, ROUND(AVG(salary)) AS `Уровень зарплат по городам` 
		FROM {table_name}		
		GROUP BY area_name
		ORDER BY 1 DESC
		LIMIT 10;""",
	con)

'''Доля вакансий по городам (в порядке убывания) - только первые 10 значений. Переменная df_area_count. Столбцы:

Город - название города
Доля вакансий - доля вакансий города среди всех вакансий. Не округлять значение.'''
df_area_count = pd.read_sql(
		f"""SELECT area_name AS `Город`, COUNT(name) / COUNT(*) AS `Доля вакансий` 
		FROM {table_name}		
		GROUP BY area_name
		ORDER BY 2 DESC
		LIMIT 10;""",
	con)