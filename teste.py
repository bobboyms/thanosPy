from architecture.utils.util import find_widget
import json
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:123456789@localhost/thanos"
db = SQLAlchemy(app)

cars = json.loads(open('C:/Users/Thago Rodrigues/Desktop/thanosPy/ThanosView/public/assets/demo/data/cars-large.json').read())

for carJson in cars["data"]:
    #print(carJson)
    car = Car()
    car.vin = carJson["vin"]
    car.brand = carJson["brand"]
    car.year = int(carJson["year"])
    car.color = carJson["color"]
    #db.session.add(car)


#db.session.commit()