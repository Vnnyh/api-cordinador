
def api_request():
     
     url = "https://sipub.coordinador.cl/api/v2/recursos/costos_marginales_reales?fecha=2018-01-31&limit=200&offset=20"

     payload = {}
     headers = {
       'Authorization': 'Token rNcCMcGCgfVVRiCoTgo4MiMx'
     }

     response = requests.request("GET", url, headers=headers, data=payload)






