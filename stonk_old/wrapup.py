import main
import kd_api


stonk_list = [2302, 2303, 2329, 2330, 2337, 2338, 2342, 2351, 2363, 2369, 2379, 2388, 2401, 2408, 2434, 2436, 2441, 2449, 2451, 2458, 2481, 3006, 3014, 3016, 3034, 3035, 3041, 3054, 3094, 3189, 3257, 3413, 3443, 3530, 3532, 3536, 3545, 3583, 3588, 3661, 3686, 3711, 4919, 4952, 4961, 4967, 4968, 5269, 5285, 5471, 6202, 6239, 6243, 6257, 6271, 6415, 6451, 6515, 6525, 6531, 6533, 6552, 6573, 6756, 8016, 8028, 8081, 8110, 8131, 8150, 8261, 8271]



for data in stonk_list:
    status = main.catcher(data)
    if status == "success":
        final_stat = kd_api.kd_counter(data, "yes")
        print(final_stat)
    else:
        print(str(data)+"->"+str(status))

'''
CREATE TABLE `stonk`.`2401` ( `date` VARCHAR(255) NOT NULL , `open` TEXT NOT NULL , `close` TEXT NOT NULL , `high` TEXT NOT NULL , `low` TEXT NOT NULL , `volume` TEXT NOT NULL , `k` TEXT NULL , `d` TEXT NULL , `14k` TEXT NULL , `14d` TEXT NULL , PRIMARY KEY (`date`)) ENGINE = InnoDB;
'''
