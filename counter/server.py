app.secret_key = 'ThisIsSecret'


@app.route('/')
def count_visits(): # session[key] = value
#session is a dictionary so check if count key exists in session
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 1
        # print session['count']
    return render_template('index.html')

@app.route('/reload')
def count_reloads():
    if 'count' in session:
        session['count'] += 2
    else:
        session['count'] = session['count']
    return render_template('reload.html')

@app.route('/reset')
def reset_counter():
    if 'count' in session:
        session['count'] = 0
    else:
        session['count'] = session['count']
    return render_template('reset.html')




app.run(debug=True) # run our server
