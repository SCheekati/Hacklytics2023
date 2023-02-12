import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import dask.dataframe as dd
import scipy.stats as stats
from flask import Flask, render_template, url_for, flash, redirect, request
from input import Form


app = Flask(__name__, template_folder='templates', static_folder='static')
pd.set_option('display.max_columns', None)

app.config['SECRET_KEY'] = '1ed85cead2c5f2876601b299232255f1'

dtypes = {
    "ID": "int64",
    "Name": "string",
    "Sex": "string",
    "Age": "string",
    "Height": "string",
    "Weight": "string",
    "Team": "string",
    "NOC": "string",
    "Games": "string",
    "Year": "string",
    "Season": "string",
    "City": "string",
    "Sport": "string",
    "Event": "string",
    "Medal": "string"

}

rtype = {
    "NOC": "string",
    "region": "string",
    "notes": "string"
}


data = pd.read_csv("../../dataset/athlete_events.csv", dtype=dtypes)

regions = pd.read_csv("../../dataset/noc_regions.csv", dtype=rtype)


data = data.dropna(subset=['Age', "Weight", "Height"])
data = data.astype({"Age": "int", "Weight": "float", "Height": "float"})

dataF = data.loc[data['Sex'] == "F"]
dataM = data.loc[data['Sex'] == "M"]



name = ""
sex = ""
age = 0
height = 0.0
weight = 0.0
country = ""

dataC = None



'''@app.route("/", methods=['GET', 'POST'])
def sportsStandard():
    if request.method == 'POST':
        age = request.form.get("inputboxage")
        sex = request.form.get("inputboxsex")
        height = request.form.get("inputboxheight")
        weight = request.form.get("inputboxweight")
        country = request.form.get("inputboxcountry")
        print(age, sex, height, weight, country)
        print(percentileAge(age, sex, False, False))
        return render_template('index.html')
    return render_template('index.html')

@app.route("/background")
def background():
    return render_template('background.html')

if __name__ == '__main__':
    app.run(debug=True)'''



def input_sex(inputsex):
    global sex
    sex = inputsex

def input_age(inputage):
    global age
    age = inputage


def input_height(inputheight):
    global height
    height = inputheight

def input_weight(inputweight):
    global weight
    weight = inputweight

def input_country(inputcountry):
    global country
    global dataC
    country = inputcountry
    dataC = data.loc[data['NOC'] == regions.loc[regions['region'] == country, 'NOC'].item()]


def percentileAge(age, sex, considSex=False, considCountry=False):
    if not considSex and not considCountry:
        return stats.percentileofscore(data['Age'], age)
    elif not considSex:
        return stats.percentileofscore(dataC['Age'], age)
    elif not considCountry:
        if sex == 'F':
            return stats.percentileofscore(dataF['Age'], age)
        else:
            return stats.percentileofscore(dataM['Age'], age)
    else:
        if sex == 'F':
            dataFC = dataC.loc[dataC['Sex'] == "F"]
            return stats.percentileofscore(dataFC['Age'], age)
        else:
            dataMC = dataC.loc[dataC['Sex'] == "M"]
            return stats.percentileofscore(dataMC['Age'], age)

def percentileHeight(height, sex, considSex=False, considCountry=False):

    if not considSex and not considCountry:
        return stats.percentileofscore(data['Height'], height)
    elif not considSex:
        return stats.percentileofscore(dataC['Height'], height)
    elif not considCountry:
        if sex == 'F':
            return stats.percentileofscore(dataF['Height'], height)
        else:
            return stats.percentileofscore(dataM['Height'], height)
    else:
        if sex == 'F':
            dataFC = dataC.loc[dataC['Sex'] == "F"]
            return stats.percentileofscore(dataFC['Height'], height)
        else:
            dataMC = dataC.loc[dataC['Sex'] == "M"]
            return stats.percentileofscore(dataMC['Height'], height)


def percentileWeight(weight, sex, considSex=False, considCountry=False):
    if not considSex and not considCountry:
        return stats.percentileofscore(data['Weight'], weight)
    elif not considSex:
        return stats.percentileofscore(dataC['Weight'], weight)
    elif not considCountry:
        if sex == 'F':
            return stats.percentileofscore(dataF['Weight'], weight)
        else:
            return stats.percentileofscore(dataM['Weight'], weight)
    else:
        if sex == 'F':
            dataFC = dataC.loc[dataC['Sex'] == "F"]
            return stats.percentileofscore(dataFC['Weight'], weight)
        else:
            dataMC = dataC.loc[dataC['Sex'] == "M"]
            return stats.percentileofscore(dataMC['Weight'], weight)


input_country("USA")
print("Percentile of 20 year old", percentileAge(20, 'F', False, False))
print("Percentile of 20 year old women", percentileAge(20, 'F', True, False))
print("Percentile of 20 year old from USA", percentileAge(20, 'F', False, True))
print("Percentile of 20 year old women from USA", percentileAge(20, 'F', True, True))
print()

print("Percentile of 170 cm men from USA", percentileHeight(170, "M", True, True))
print("Percentile of 180 cm men from USA", percentileHeight(180, "M", True, True))
print("Percentile of 190 cm men from USA", percentileHeight(190, "M", True, True))
print()

print("Percentile of 60kg men from USA", percentileWeight(60, "M", True, True))
print("Percentile of 70kg men from USA", percentileWeight(60, "M", True, True))
print("Percentile of 80kg men from USA", percentileWeight(60, "M", True, True))
print()

input_country("Japan")
print("Percentile of 20 year old", percentileAge(20, 'F', False, False))
print("Percentile of 20 year old women", percentileAge(20, 'F', True, False))
print("Percentile of 20 year old from Japan", percentileAge(20, 'F', False, True))
print("Percentile of 20 year old women from Japan", percentileAge(20, 'F', True, True))
print()

print("Percentile of 170 cm men from Japan", percentileHeight(170, "M", True, True))
print("Percentile of 180 cm men from Japan", percentileHeight(180, "M", True, True))
print("Percentile of 190 cm men from USA", percentileHeight(190, "M", True, True))
print()

print("Percentile of 60kg men from Japan", percentileWeight(60, "M", True, True))
print("Percentile of 70kg men from Japan", percentileWeight(60, "M", True, True))
print("Percentile of 80kg men from Japan", percentileWeight(60, "M", True, True))
print()


print("Percentile of 20 year old", percentileAge(20, 'F', False, False))
print("Percentile of 20 year old women", percentileAge(20, 'F', True, False))
print("Percentile of 20 year old from Japan", percentileAge(20, 'F', False, True))
print("Percentile of 20 year old women from Japan", percentileAge(20, 'F', True, True))



