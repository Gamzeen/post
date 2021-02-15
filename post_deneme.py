#post ve token ı sorunsuz yapıyor
import requests

url = "http://asdadasd.com/public/login"
url1 = "http://adsasdasd.com/secured/card/control"

#url1 = "http://213.155.103.168:19080/secured/card/control"

def request_token():
    #liste=kullanici_giris()
    #username=liste[0]
    #password=liste[1]
    username="xxxxx"
    password="xxxxx"
    
    payload = "{ \n    \"username\": \""+username+"\",\n    \"password\": \""+password+"\"\n}"
    headers = {
        'Application-Name': 'Xxxxx',
        'Content-Type': 'application/json'
        }
    response = requests.request("POST", url, headers=headers, data = payload)
    response_utf =response.text.encode('utf8')
    #print("response_utf: ",response_utf)
    #print("")

    sresponse=str(response_utf) 
    #print("String str response ",sresponse)
    #print("")
    split_sresponse=sresponse.split('"')
    response_token=split_sresponse[5]
    #print(response_token)
    return response_token
tekrar=1
while tekrar<3:
       
    response_token=request_token()#token basvurusu yap  
    #print("ze response_token : ",response_token)


    #print("a tipi : ",type(a))
    #print("Barcode reader.read().strip()",a)
    #data=a[0:13]
    data="8690637972751"
    print("tip",type(data))
    print("data",data)
        #payload = "{\n    \"cardId\": ,data,\n    \"clientId\": \"RPI1\"\n}"
    payload1 = "{\n    \"cardId\": \""+data+"\",\n    \"clientId\": \"RPI1\"\n}"
    headers1 = {
        'Authorization': 'a',
        'Content-Type': 'application/json'
        }
    response_token="Bearer "+response_token
    headers1['Authorization']=response_token
        #print("response_token",response_token)
        #print("headers1",headers1['Authorization'])

    response = requests.request("POST", url1, headers=headers1, data = payload1)
    #print("response",response)
    uresponse= str(response.text.encode('utf8'))
    #print("uresponse:",uresponse)
    reuresponse=uresponse.find("true")
    #print("reuresponse :",reuresponse)
        
    if reuresponse==-1:
        print("Barcode verisi yok")
            
    if reuresponse !=-1:
        print("Barcode verisi var")
        for i in range(0,2):
            blink(12)        
    tekrar+=1
