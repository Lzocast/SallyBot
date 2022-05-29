def Weather():

# NOTE: For this to work you need to have installed the 'requests' module for python:
# At admin level command line type:
#        python -m pip install requests

# importing requests and json
   import requests
   import json
   import time
   
   # base URL
   BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
   # City Name (You can replace this with your city if you wish)
   CITY = "St. John's"
   # API key (Needs to be a valid key, you can sign up for free to get one)
   API_KEY = "af3f11579680280547897fa6eb2352eb"
   # updating the URL (NOTE: if this doesn't work, go the website to check how
   # they denote your city ie: abbreviations etc)
   URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
   # HTTP request
   response = requests.get(URL)
   # checking the status code of the request
   if response.status_code == 200:
      # getting data in the json format
      data = response.json()
      # getting the main dict block
      main = data['main']
      # getting temperature
      temperature = main['temp']
      # getting the humidity
      humidity = main['humidity']
      # getting the pressure
      pressure = main['pressure']
      # weather report
      report = data['weather']
      print(f"{CITY:-^30}")
      print("Temperature (Celcius): {:0.1f}".format(temperature - 273.15))
      print(f"Humidity: {humidity}")
      print(f"Pressure: {pressure}")
      print(f"Weather Report: {report[0]['description']}")
      time.sleep(3)
      if "clouds" in str(data['weather']):
         print('\nSally: Hmm, bit cloudy today huh?')
      elif "sun" in str(data['weather']):
         print('\nSally: Hey, here comes the sun')
      elif "rain" in str(data['weather']):
         print('\nSally: Guess I\'ll need a brolly')
      elif "snow" in str(data['weather']):
         print('\nSally: Brr, better get my hat and coat')
      elif "windy" or "wind" or "breeze" in str(data['weather']):
         print('\nSally: Going to be a blowy one')
      elif "clear" in str(data['weather']):
         print('\nSally: Clear skies, beautiful!')
      elif "frost" or "ice" in str(data['weather']):
         print('\nSally: Slippery roads... fun...')

   else:
      # showing the error message
      print("Error in the HTTP request")
      time.sleep(2)
      print(
         "Sally: Oh... guess that's not working then. Just have to use the old, 'Stick"
         "your head out the window', method I guess lol"
      )

def main():
   Weather()

if __name__ == "__main__":
    main()
