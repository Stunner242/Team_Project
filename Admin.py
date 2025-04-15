import mysql.connector
def  check_Admin(uname,passw,id1):
    uname= uname.strip()
    passw= passw.strip()
    id1= id1.strip()
    try:
        conn=mysql.connector.connect(host='localhost',user='root',password='Golu123',database='garvit')
        cursor=conn.cursor()
        select_query="SELECT * FROM admin WHERE username=%s AND password=%s AND id=%s"
        cursor.execute(select_query,(uname,passw,id1))
        result=cursor.fetchall()
        conn.close()
        return len(result)>0
    except mysql.connector.Error as err:
        print("Error: ", err)
        return False