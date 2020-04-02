import time
import random
import requests
import forecastio

while(1):
   
        api_key="093ca5c03fad526cca6f7df53df58741"

        lat=35
        lng=128
        forecast=forecastio.load_forecast(api_key,lat,lng)
        weather=forecast.currently()
        value=weather.temperature
        requests.get ("http://ec2-54-84-89-237.compute-1.amazonaws.com:8080/log?value="+str(value))
        time.sleep(100)
