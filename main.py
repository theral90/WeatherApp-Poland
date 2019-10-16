#!/usr/bin/env python
from pprint import pprint as pp
from flask import Flask, flash, redirect, render_template, request, url_for
from weather import query_api

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('weather.html',
    data=[{'name':'Warsaw'}, {'name':'Krakow'}, {'name':'Katowice'},
    {'name':'Lublin'}, {'name':'Lodz'}, {'name':'Gdansk'},
    {'name':'Szczecin'}, {'name':'Suwalki'}, {'name':'Torun'},
    {'name':'Rzeszow'}, {'name':'Zakopane'}, {'name':'Poznan'},
    {'name':'Hel'}, {'name':'Wroclaw'}, {'name':'Olsztyn'}])


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
