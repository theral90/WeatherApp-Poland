#!/usr/bin/env python
from pprint import pprint as pp
from flask import Flask, flash, redirect, render_template, request, url_for
from weather import query_api

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('weather.html',
    data=[{'name':'Bialystok'}, {'name':'Czestochowa'},
    {'name':'Gdansk'}, {'name':'Hel'},{'name':'Katowice'},{'name':'Krakow'},
    {'name':'Lodz'}, {'name':'Lublin'},{'name':'Olsztyn'},
    {'name':'Poznan'},{'name':'Rzeszow'},{'name':'Suwalki'},
    {'name':'Szczecin'},{'name':'Torun'},{'name':'Warsaw'},
    {'name':'Wroclaw'},{'name':'Zakopane'}])


@app.route("/result" , methods=['GET', 'POST'])
def result():
    data = []
    error = None
    select = request.form.get('comp_select')
    resp = query_api(select)
    pp(resp)
    if resp:
        data.append(resp)
        if len(data) != 2:
            error = 'Bad Response from Weather API'
    return render_template('result.html', data=data, error=error)


if __name__=='__main__':
    app.run(debug=True)
