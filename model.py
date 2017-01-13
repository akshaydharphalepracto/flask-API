import MySQLdb;

conn = MySQLdb.connect(host='localhost', user='root', passwd='', db='mdm_db');
cursor = conn.cursor();

def readDocument(docId):
	# query = "select * from documents where id = " + docId;
	# cursor.execute(query);
	# result = cursor.fetchall();
	# d = {};
	# d["document"] = result;
	sample = {};
	sample['one'] = 1;
	return sample;

# def createStudent(r_json):
# 	name = r_json["name"]
# 	sql = "insert into student (name) values ('%s')" % (name)
# 	try:
# 		cursor.execute(sql)
# 		conn.commit()
# 	except:
# 		conn.rollback()
# 	return

# def updateStudent(stId):
# 	name = r_json["name"]
# 	sql = "update student set name = '%s' where id = '%d'" % (name, stId)
# 	try:
# 		cursor.execute(sql)
# 		conn.commit()
# 	except:
# 	   conn.rollback()

# def deleteStudent(stId):
# 	sql = "delete from student where id = '%d'" % (stId)
# 	try:
# 		cursor.execute(sql)
# 		conn.commit()
# 	except:
# 	   conn.rollback()
# 	return






