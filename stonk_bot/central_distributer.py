def center(data, userID):
    userid_text = "使用者ID=" + str(userID)
    #預設訊息處理
    if data == "測試":
        return "換行測試\n換行測試\n換行測試"
    else:
        #訊息消化
        data_seperator = []

        try:
            data_seperator = data.split(",") #指令切割 格式==>"縣市:高雄,日期:2021-07-19"
        except:
            data_seperator = data.append(data)

        for item in data_seperator:
            reply_text = ""
            command_tray= []
            data_tray = []
            try:
                command_type= (item.split(":"))[0] #指令類型
                config_data = (item.split(":"))[1] #資料

                command_tray.append(command_type)
                data_tray.append(config_data)
            except :
                command_type= "bypass" #沒按照格式或是單字(為NLP留缺口)
                config_data = item 


            #轉發包
            if command_type == "縣市":
                reply_text = reply_text + city(config_data)
            elif command_type == "日期":
                reply_text = reply_text + date(config_data)
            else:
                return "請稍待系統建置完成\n"+userid_text
    


def city(data):
    reply_text = "目前查詢的是" + str(data)

    return str(reply_text)

def date(data):
    reply_text = "日期查詢功能尚未建置完成"

    return str(reply_text)