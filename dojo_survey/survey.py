from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def survey():
  return render_template("survey.html")
#
# @app.route('/process', methods=['post'])
# def survey_info():
#    print request.form['name']
#    return redirect('/results')

@app.route('/results', methods = ['POST'])
def results():
    return render_template("results.html", name = request.form['name'], location = request.form['location'], language = request.form['language'], comment = request.form['comment'])




app.run(debug=True) # run our server
