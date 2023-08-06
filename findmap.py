import requests
import json
import sys

amapkey = '6c94abaf35129e8e4d367a48d58861ff' # 高德api key
count = 10  # 要搜索的数量

def find_center_point(coordinates):
    total_longitude = 0.0
    total_latitude = 0.0
    num_points = len(coordinates)

    for coord in coordinates:
        longitude, latitude = float(coord[0]), float(coord[1])
        total_longitude += longitude
        total_latitude += latitude

    center_longitude = total_longitude / num_points
    center_latitude = total_latitude / num_points

    return center_longitude, center_latitude



getlocationurl = "https://restapi.amap.com/v3/place/text"
# locationrequest = requests.get(getlocationurl,locationpayload)
# # if locationrequest.status_code != 200:
# #     print("坐标获取失败")
# #     sys.exit(1)
# locationcontent = locationrequest1.json()

locat = []

for i in range(0,len(sys.argv)-1):
    locationpayload = {
        'key': amapkey,
        'page_size': '1',
        'keywords': sys.argv[i+1]
    }
    locationrequest = requests.get(getlocationurl,locationpayload)
    locationcontent = locationrequest.json()
    locat.append(locationcontent['pois'][0]['location'].split(','))

# print(find_center_point(locat))
endlocat = str(find_center_point(locat)).strip('() ').replace(" ","")

getaddressurl = "https://restapi.amap.com/v3/place/around"
addresspayload = {
    'key': amapkey,
    'page_size': count,
    'types': '100000',
    'location': endlocat
}
addressrequest = requests.get(getaddressurl,addresspayload)
addresscontent = addressrequest.json()

for i in range(0,count):
    addressname = addresscontent['pois'][i]['name']
    print(addressname)

