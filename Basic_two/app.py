# build a basic flask app with multiple routes and redirecting based on conditions


from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def welcome():
   return 'welcome to basic two'


@app.route('/pass/<int:marks>')
def pass_result(marks):
  return 'pass and marks are ' + str(marks)


@app.route('/fail/<int:marks>')
def fail_result(marks):
  return "fail and marks are " + str(marks)

@app.route('/results/<int:marks>')
def results(marks):
      result= ""
      if marks >= 35:
        result = "pass_result"
      else:
        result = "fail_result"
      return redirect(url_for(result, marks=marks))

if __name__ == '__main__':
   app.run(debug=True)