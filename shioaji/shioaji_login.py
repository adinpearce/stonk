import shioaji as sj


def login():
    api = sj.Shioaji()

    #login
    account = api.login("S125235872", "adin2427")

    api.activate_ca(
        ca_path="C:/ekey/551/S125235872/S/Sinopac.pfx",
        ca_passwd="S125235872",
        person_id="S125235872",
    )
