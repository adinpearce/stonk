'''
DELETE FROM `2302` WHERE `2302`.`date` = '2021-05-11';
DELETE FROM `2302` WHERE `2302`.`date` = '2021-05-12';
DELETE FROM `2302` WHERE `2302`.`date` = '2021-05-13';
DELETE FROM `2302` WHERE `2302`.`date` = '2021-05-14';
DELETE FROM `2302` WHERE `2302`.`date` = '2021-05-17';
DELETE FROM `2302` WHERE `2302`.`date` = '2021-05-18';
DELETE FROM `2302` WHERE `2302`.`date` = '2021-05-19';
DELETE FROM `2302` WHERE `2302`.`date` = '2021-05-20';
DELETE FROM `2302` WHERE `2302`.`date` = '2021-05-21';
DELETE FROM `2302` WHERE `2302`.`date` = '2021-05-24';
DELETE FROM `2302` WHERE `2302`.`date` = '2021-05-25';
DELETE FROM `2302` WHERE `2302`.`date` = '2021-05-26';
DELETE FROM `2302` WHERE `2302`.`date` = '2021-05-27';
DELETE FROM `2302` WHERE `2302`.`date` = '2021-05-28';
DELETE FROM `2302` WHERE `2302`.`date` = '2021-05-31';
DELETE FROM `2302` WHERE `2302`.`date` = '2021-06-01';
DELETE FROM `2302` WHERE `2302`.`date` = '2021-06-02';
DELETE FROM `2302` WHERE `2302`.`date` = '2021-06-03';
DELETE FROM `2302` WHERE `2302`.`date` = '2021-06-04';
DELETE FROM `2302` WHERE `2302`.`date` = '2021-06-07';
DELETE FROM `2302` WHERE `2302`.`date` = '2021-06-08';
DELETE FROM `2302` WHERE `2302`.`date` = '2021-06-09';
DELETE FROM `2302` WHERE `2302`.`date` = '2021-06-11';
DELETE FROM `2302` WHERE `2302`.`date` = '2021-06-13';
'''
import mysql.connector

#date_array = ['2021-05-11','2021-05-12','2021-05-13','2021-05-14','2021-05-17','2021-05-18','2021-05-19','2021-05-20','2021-05-21','2021-05-24','2021-05-25','2021-05-26','2021-05-27','2021-05-28','2021-05-31','2021-06-01','2021-06-02','2021-06-03','2021-06-04','2021-06-07','2021-06-08','2021-06-09','2021-06-10','2021-06-11','2021-06-13']
date_array = ['2021-06-11']
stonk_list = [2302, 2303, 2329, 2330, 2337, 2338, 2342, 2351, 2363, 2369, 2379, 2388, 2401, 2408, 2434, 2436, 2441, 2449, 2451, 2458, 2481, 3006, 3014, 3016, 3034, 3035, 3041, 3054, 3094, 3189, 3257, 3413, 3443, 3530, 3532, 3536, 3545, 3583, 3588, 3661, 3686, 3711, 4919, 4952, 4961, 4967, 4968, 5269, 5285, 5471, 6202, 6239, 6243, 6257, 6271, 6415, 6451, 6515, 6525, 6531, 6533, 6552, 6573, 6756, 8016, 8028, 8081, 8110, 8131, 8150, 8261, 8271]

mydb = mysql.connector.connect(
    host="220.135.176.190",
    user="k20",
    password="jona789521456",
    database="stonk",
    auth_plugin="mysql_native_password"
)

mycursor = mydb.cursor()

for data in stonk_list:
    for date in date_array:
        try:
            sql = "DELETE FROM `"+str(data)+"` WHERE `"+str(data)+"`.`date` = '"+str(date)+"';"
            mycursor.execute(sql)
            mydb.commit()
        except Exception as error:
            print(error)