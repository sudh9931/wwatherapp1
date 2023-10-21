from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import requests
from urllib.request import urlopen as uReq

application = Flask(__name__) # initializing a flask app
app=application

@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/review',methods=['POST','GET']) # route to show the review comments in a web UI
@cross_origin()
def get_weather():
    if request.method == 'POST':
        api_key = 'b2f7276693524dc1283929277faa0eae' 
        base_url = 'https://api.openweathermap.org/data/2.5/weather'   
        params = {
            'q': request.form.get("content"),
            'appid': api_key,
            'units': 'metric'  # Use 'imperial' for Fahrenheit
        }

        try:
            response = requests.get(base_url, params=params)
            data = response.json()

            if response.status_code == 200:
                city = data['name']
                temperature = data['main']['temp']
                description = data['weather'][0]['description']

                print(f'City: {city}')
                print(f'Temperature: {temperature}°C')
                print(f'Weather: {description}')
            else:
                print(f'Error: {data["message"]}')

        except requests.exceptions.RequestException as e:
            print(f'Error: {e}')
        return f'City: {city} ,Temperature: {temperature}°C ,Weather: {description}'
    else:
        return render_template('index.html')

if __name__ == "__main__":
    #app.run(host='0.0.0.0', port=8000)
	app.run(debug=True)
