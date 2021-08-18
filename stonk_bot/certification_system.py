import mysql.connector

mydb = mysql.connector.connect(
    host="220.135.176.190",
    user="retr0",
    password="jona789521456",
    database="stonk",
    auth_plugin="mysql_native_password"
)

mycursor = mydb.cursor()


def certification(user_id):
    sql = "SELECT * FROM `user_allow` WHERE `user_ID` = '"+str(user_id)+"'"

    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    if myresult == [] :
        sql_insert = "INSERT INTO `user_allow`(`user_ID`, `status`) VALUES ('"+str(user_id)+"', 0)"
        mycursor.execute(sql_insert)

        mydb.commit()

        return 3
    elif myresult != []:
        status = myresult[0][1]

        return int(status)

