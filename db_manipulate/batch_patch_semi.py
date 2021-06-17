import mysql.connector

mydb = mysql.connector.connect(
    host="220.135.176.190",
    user="k20",
    password="jona789521456",
    database="stonk",
    auth_plugin="mysql_native_password"
)

mycursor = mydb.cursor()

stonk_list = [2303, 2329, 2337, 2338, 2342, 2351, 2363, 2369, 2379, 2388, 2401, 2408, 2434, 2436, 2441, 2449, 2451, 2458, 2481, 3006, 3014, 3016, 3034, 3035, 3041, 3054, 3094, 3189, 3257, 3413, 3443, 3530, 3532, 3536, 3545, 3583, 3588, 3661, 3686, 3711, 4919, 4952, 4961, 4967, 4968, 5269, 5285, 5471, 6202, 6239, 6243, 6257, 6271, 6415, 6451, 6515, 6525, 6531, 6533, 6552, 6573, 6756, 8016, 8028, 8081, 8110, 8131, 8150, 8261, 8271]


for data in stonk_list:
    sql = "ALTER TABLE `"+str(data)+"` ADD `avg_price` TEXT NOT NULL AFTER `low`;"
    mycursor.execute(sql)
    