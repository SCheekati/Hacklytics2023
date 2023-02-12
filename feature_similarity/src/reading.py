import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import dask.dataframe as dd
import scipy.stats as stats
from flask import Flask, render_template, url_for, flash, redirect
from input import Form


app = Flask(__name__)

app.config['SECRET_KEY'] = '1ed85cead2c5f2876601b299232255f1'

@app.route("/", methods=['GET', 'POST'])
def sportsStandard():
    sportsForm = Form()
    if sportsForm.validate_on_submit():
        flash(f'Data accepted', 'success')
        #return redirect()
    return render_template('.html', form=sportsForm)

if __name__ == '__main__':
    app.run(debug=True)


pd.set_option('display.max_columns', None)

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

data = pd.read_csv("../../dataset/athlete_events.csv", dtype=dtypes)

#print("Train size:", data.shape)

#print(data.head())

data = data.dropna(subset=['Age', "Weight", "Height"])
data = data.astype({"Age": "int", "Weight": "float", "Height": "float"})

dataF = data.loc[data['Sex'] == "F"]
dataM = data.loc[data['Sex'] == "M"]

#print("mean", np.mean(dataF["Age"]))

#print(stats.percentileofscore(dataF['Age'], 19, kind='rank'))

name = ""
sex = ""
age = 0
height = 0.0
weight = 0.0
country = ""

dataC = None

def input_name(inputname):
    global name
    name = inputname

def input_sex(inputsex):
    global sex
    sex = inputsex

def input_age(inputage):
    global age
    age = inputage


def input_height(inputheight):
    global height
    height = inputheight


def input_country(inputcountry):
    global country
    global dataC
    country = inputcountry
    dataC = data


def percentileAge(considSex=False, considCountry=False):
    if not considSex and not considCountry:
        stats.percentileofscore(data['Age'], age)
    elif not considSex:
        stats.percentileofscore(data['Age'], age)




'''df_mean = np.mean(dataF["Age"])
df_std = np.std(dataF["Age"])

# Calculating probability density function (PDF)
pdf = stats.norm.pdf(dataF["Age"].sort_values(), df_mean, df_std)

# Drawing a graph
plt.plot(dataF["Age"].sort_values(), pdf)
plt.xlim([0, 100])
plt.xlabel("Age", size=12)
plt.ylabel("Frequency", size=12)
plt.grid(True, alpha=0.3, linestyle="--")
plt.show()'''
