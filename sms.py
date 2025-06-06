from twilio.rest import Client
import redis

# Initialize Redis
r = redis.Redis()

account_sid = 'AC559e8847a1380949483fa026183666f1'
auth_token = '9db119708e52c9566ace3f576c9f9eab'
client = Client(account_sid, auth_token)

lat = r.get("lat")
lat = float(lat)
lng = r.get("lng")
lng = float(lng)
gps = f"Latitude: {lat} and Longitude: {lng}"
gMap = "https://www.google.com/maps?q="+str(lat)+','+str(lng)
print(gps, gMap)

message = client.messages.create(    
    from_='+12317585844',
    to='+917008714629',
    body='help! : '+ gMap
)
