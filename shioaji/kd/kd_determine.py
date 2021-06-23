import mysql.connector
import datetime



stonk_list = [2302, 2303, 2329, 2330, 2337, 2338, 2342, 2351, 2363, 2369, 2379, 2388, 2401, 2408, 2434, 2436, 2441, 2449, 2451, 2458, 2481, 3006, 3014, 3016, 3034, 3035, 3041, 3054, 3094, 3189, 3257, 3413, 3443, 3530, 3532, 3536, 3545, 3583, 3588, 3661, 3686, 3711, 4919, 4952, 4961, 4967, 4968, 5269, 5285, 5471, 6202, 6239, 6243, 6257, 6271, 6415, 6451, 6515, 6525, 6531, 6533, 6552, 6573, 6756, 8016, 8028, 8081, 8110, 8131, 8150, 8261, 8271]
#stonk_list = [2302]

mydb = mysql.connector.connect(
    host="220.135.176.190",
    user="k20",
    password="jona789521456",
    database="stonk",
    auth_plugin="mysql_native_password"
)

mycursor = mydb.cursor()

now = datetime.datetime.now()
today_date = str(now.strftime("%Y"))+"-" + \
        str(now.strftime("%m"))+"-"+str(now.strftime("%d"))


cross = []
cross_status = []
volume = []
volume_status = []

for data in stonk_list:
    sql = "SELECT `k`, `d` FROM `"+str(data)+"` ORDER BY `date` DESC LIMIT 5"

    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    print("="*50 + ">" + str(data))

    k_list = []
    d_list = [] 

    for item in myresult:
        k_list.append(item[0])
        d_list.append(item[1])

    if float(d_list[1]) > float(k_list[1]):  #如果昨天的d值大於昨天k值
        if float(k_list[0]) > float(d_list[0]): #如果今天k值大於今天d值
            print(str(data) + "黃金交叉")
            cross.append(str(data))
            cross_status.append("1")
    elif float(d_list[1]) < float(k_list[1]): #如果昨天的d值小於昨天k值
        if float(k_list[0]) < float(d_list[0]): #如果今天k值小於今天d值
            print(str(data) + "死亡交叉")
            cross.append(str(data))
            cross_status.append("0")


for item in cross:
    volume_status_layer1 = []

    sql = "SELECT `volume` FROM `"+str(item)+"` ORDER BY `date` DESC LIMIT 5"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    today_volume = int(myresult[0][0])
    volume.append(str(today_volume))

    pass_volume = int(myresult[1][0]) + int(myresult[2][0])+ int(myresult[3][0])+ int(myresult[4][0])
    pass_avg_volume = pass_volume / 4

    determination_point_for_volume = round(today_volume / pass_avg_volume, 2)

    volume_status_layer1.append(str(determination_point_for_volume))
    if determination_point_for_volume > 4:
        volume_status_layer1.append("4")
    elif determination_point_for_volume > 3:
        volume_status_layer1.append("3")
    elif determination_point_for_volume > 2:
        volume_status_layer1.append("2")
    elif determination_point_for_volume > 1:
        volume_status_layer1.append("1")
    elif determination_point_for_volume < 1:
        volume_status_layer1.append("0")

    volume_status.append(volume_status_layer1)



sql = "INSERT INTO `semi_kd_determine`(`date`, `stock_num`, `status`, `volume`, `volume_status`) VALUES (%s, %s, %s, %s, %s)"
val = today_date, str(cross), str(cross_status), str(volume), str(volume_status)
mycursor.execute(sql, val)
mydb.commit()

    