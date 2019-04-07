from flask import *
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('homepage.html')

@app.route('/new_bike', methods = ["GET", "POST"])
def new_bike():
    if request.method == "GET":
        return render_template('bike.html')
    elif request.method == "POST":
        form = request.form
        bike_model = form['input_model']
        bike_fee = form['input_fee']
        bike_image = form['input_image']
        bike_year = form['input_year']

        print(form)

        new_bike = {
          'model': bike_model,
          'fee': bike_fee,
          'image': bike_image,
          'year': bike_year,
        }
        bikes.insert_one(new_bike)
        return redirect('/new_bike')


if __name__ == '__main__':
  app.run(debug=True)
