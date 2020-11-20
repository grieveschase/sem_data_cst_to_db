import sqlite3 

def sqlite_query(sql_input):
	db_file = "C://Python3//cd_data_db//sem_data.db"

	conn = sqlite3.connect(db_file, detect_types = sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
	cur = conn.cursor()
	cur.execute(sql_input)
	data_out = [row for row in cur]
	return data_out


sql_input = "select * from sem_data where recipe like '%5x5x5_50_VERA%' and Tool_ID like 'vsem402%'"

data_out = sqlite_query(sql_input)

print(len(data_out))