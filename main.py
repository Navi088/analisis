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
        sel = request.form['selec']

        if sel == 'single_quarter':
            if request.form['fibras']=="" or request.form['year']=="" or request.form['q']=="":
                return render_template('index.html',reit=reit_list,
                                        year=year_list, error=True)

            else:
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
         
        if sel == 'check_all_quarters':
            if request.form['fibras']=="" or request.form['year']=="":
                return render_template('index.html',reit=reit_list,
                                        year=year_list, error=True)

            else:
                get_reit = request.form['fibras']
                get_year = int(request.form['year'])

                yearly_search = MainClass.reit_history(get_reit, get_year)
                get_quarter_list = yearly_search[0]

                return render_template('reit_history.html',reit=get_reit,
                                        year=get_year, qua=get_quarter_list,
                                                        ys=yearly_search)
        if sel == 'compare_quarters':
            if request.form['fibras_1']=="" or request.form['fibras_2']=="":
                return render_template('index.html',reit=reit_list,
                                        year=year_list, error=True)

            else:
                get_first = request.form['fibras_1']
                get_second = request.form['fibras_2']

                fibras = [get_first,get_second]

                if get_first == get_second:
                    return render_template('index.html',reit=reit_list,
                                        year=year_list, error=False)
                else:
                    lastq = []
                    firstq = []

                    for f in fibras:
                        lastq1_list = []
                        firstq1_list = []
                        
                        search_y1 = list(reits[f].keys())
                        y1 = search_y1[-1]
                        search_lastQ1 = list(reits[f][y1])
                        
                        if len(search_lastQ1) > 1:
                            lastQ1 = search_lastQ1[-1]
                            
                            search_elem1 = list(reits[f][y1][lastQ1].values())
                            for i in search_elem1:
                                for h in i:
                                    convert_h = float(h.replace(",",""))
                                    lastq1_list.append(convert_h)
                            lastq.append(lastq1_list)
                            
                            search_first_elem = list(reits[f][y1]["q1"].values())
                            for e in search_first_elem:
                                for t in e:
                                    convert_t = float(t.replace(",",""))
                                    firstq1_list.append(convert_t)
                            firstq.append(firstq1_list)
                                
                        else:
                            print ("Aun no es posible analizar debido a que ha comenzado el año")

                    get_class = MainClass.main_function(lastq, firstq, fibras)
                    fibra_list1 = list(get_class[fibras[0]])
                    fibra_list2 = list(get_class[fibras[1]])
                    
                    get_result = [fibra_list1, fibra_list2]
                    print (get_result)
                    elements = ['Ingresos Totales','NOI','FFO','AFFO','Ingresos MXN','Ingresos USD',
                        'Activos Totales','Total de Patrimonio','Tasa fija','Tasa variable','Servisio de deuda',
                        'Deuda en dolares','Deuda Total','ABR','Margen ABR','NAV','Precio de cierre','CFBIs circulantes']

                    return render_template('search_compare.html', first=get_first, second=get_second,
                                                            elem=elements, fib=get_result)

    return render_template('index.html',reit=reit_list,
                                        year=year_list)

if __name__=='__main__':
    app.run(debug=True)