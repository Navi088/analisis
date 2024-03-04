from flask import Flask, render_template, request
from bd_reits import reits

app = Flask(__name__)

reit_list = []
year_list = []

# GET REIT NAMES
for r in reits:
    reit_list.append(r)

# GET YEARS AVAILABE
for x in reits.keys():
    y = list(reits[x].keys())
    for z in y:
        if z not in year_list:
            year_list.append(z)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method=='POST':
        try:
            try:
                get_reit = request.form['fibras']
                get_year = request.form['year']
                get_quarter = request.form['q']

                print (get_reit, get_year, get_quarter)
            except:
                get_reit = request.form['fibras']
                get_year = request.form['year']

                print (get_reit, get_year)
        except:
            get_first = request.form['fibras_1']
            get_second = request.form['fibras_2']

            print (get_first, get_second)

    return render_template('index.html',reit=reit_list,
                                        year=year_list)

if __name__=='__main__':
    app.run(debug=True)