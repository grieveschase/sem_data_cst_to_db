import sqlite3

def sqlite_query(sql_input):
	db_file = "C://Python3//cd_data_db//sem_data.db"

	conn = sqlite3.connect(db_file)
	cur = conn.cursor()
	cur.execute(sql_input)
	data_out = [row for row in cur]
	return data_out


sql_input = "select * from sem_data where recipe like '%8000%'"

data_out = sqlite_query(sql_input)

print(len(data_out))
