import main
import kd_api


stonk_list = [2302, 2303, 2329, 2330, 2337,
              2338, 2342, 2351, 2363, 2369, 2379, 2388]

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
