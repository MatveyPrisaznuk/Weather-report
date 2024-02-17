from flask import Flask, render_template, request
import requests 

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city_name = request.form['name']
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=3ce97c0c8057c10ede90e13ffcb5189e'
        response = requests.get(url.format(city_name)).json()

        if 'main' in response:
            temp = response['main'].get('temp')
            weather = response['weather'][0]['description']
            min_temp = response['main'].get('temp_min')
            max_temp = response['main'].get('temp_max')
            icon = response['weather'][0]['icon']
            
            return render_template('index.html', temp=temp, weather=weather, min_temp=min_temp, max_temp=max_temp, icon=icon, city_name=city_name)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
