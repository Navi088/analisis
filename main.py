from flask import Flask, render_template, request
from bd_reits import reits
from process import MainClass

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
                get_year = int(request.form['year'])
                get_quarter = request.form['q']

                upper_q = get_quarter.upper()

                single_reit_process = MainClass.single_reit(get_reit,
                                                            get_year,
                                                            get_quarter)

                return render_template('search_reit.html', reit_name=get_reit,
                                       quarter=upper_q,
                                       process=single_reit_process)       
            except:
                get_reit = request.form['fibras']
                get_year = request.form['year']

                return render_template('reit_history.html',reit=get_reit,
                                                        year=get_year)
        except:
            get_first = request.form['fibras_1']
            get_second = request.form['fibras_2']

            return render_template('search_compare.html', first=get_first,
                                                        second=get_second)

    return render_template('index.html',reit=reit_list,
                                        year=year_list)

if __name__=='__main__':
    app.run(debug=True)