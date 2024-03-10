from bd_reits import reits
import pandas as pd
import numpy as np

class MainClass:
    def single_reit(a, b, c):
        # BUSCAR FIBRAS
        debt_margin_list = []
        ffo_margin_list = []

        income_list = reits[a][b][c]['income']
        income = list(income_list)

        debt_list = reits[a][b][c]['debt']
        debt = list(debt_list)

        occupancy_list = reits[a][b][c]['occupancy']
        occupancy = list(occupancy_list)

        analysis_list = reits[a][b][c]['analysis']
        analysis = list(analysis_list)

        # CALCULATE DEBT MARGIN
        w = float(debt[4].replace(",",""))
        x = float(income[6].replace(",",""))
        debt_margin = round((w / x) * 100, 2)

        if debt_margin < 35.00:
            m = "Deuda saludable"
            t = 100.00 - debt_margin
            debt_margin_list.append(t)
            debt_margin_list.append(debt_margin)
            debt_margin_list.append(m)

        if debt_margin > 35.00 and debt_margin < 45.00:
            m = "Deuda tolerable"
            t = 100.00 - debt_margin
            debt_margin_list.append(t)
            debt_margin_list.append(debt_margin)
            debt_margin_list.append(m)

        if debt_margin > 45.00 and debt_margin < 50.00:
            m = "Deuda de riesgo moderado"
            t = 100.00 - debt_margin
            debt_margin_list.append(t)
            debt_margin_list.append(debt_margin)
            debt_margin_list.append(m)

        if debt_margin > 50.00:
            m = "Deuda de alto riesgo"
            t = 100.00 - debt_margin
            debt_margin_list.append(t)
            debt_margin_list.append(debt_margin)
            debt_margin_list.append(m)

        # CALCULATE FFO MARGIN
        y = float(income[2].replace(",",""))
        z = float(income[0].replace(",",""))
        ffo_margin = round((y / z) * 100, 2)
        if ffo_margin > 60.00:
            n = "Riesgo minimo"
            ffo_margin_list.append(ffo_margin)
            ffo_margin_list.append(n)

        if ffo_margin > 35.00 and ffo_margin < 60.00:
            n = "Riesgo modesto"
            ffo_margin_list.append(ffo_margin)
            ffo_margin_list.append(n)

        if ffo_margin > 12.00 and ffo_margin < 35.00:
            n = "Riesgo significativo"
            ffo_margin_list.append(ffo_margin)
            ffo_margin_list.append(n)

        if ffo_margin < 12.00:
            n = "Riesgo maximo"
            ffo_margin_list.append(ffo_margin)
            ffo_margin_list.append(n)


        result_list = [income, debt, occupancy, analysis, debt_margin_list, ffo_margin_list]
        return result_list
    

    # SEARCH FOR YEAR
    def reit_history(r, yr):
        indexes = ['Ingresos Totales','NOI','FFO','AFFO','Ingresos MXN','Ingresos USD',
        'Activos Totales','Total de Patrimonio','Tasa fija','Tasa variable','Servisio de deuda',
        'Deuda en dolares','Deuda Total','ABR','Margen ABR','NAV','Precio de cierre','CFBIs circulantes']
        list_group = []
        q_list = []
        data = {}

        for i in reits[r][yr].keys():
            a = reits[r][yr][i]['income']
            b = reits[r][yr][i]['debt']
            c = reits[r][yr][i]['occupancy']
            d = reits[r][yr][i]['analysis']

            group = a + b + c + d
            list_group.append(group)
            q_list.append(i.upper())
            
        for x, y in enumerate(q_list):
            data[y] = list_group[x]
            
        df = pd.DataFrame(data, index=indexes)

        clean_last_quart = list(df[q_list[-1]])
        clean_first_quart = list(df[q_list[0]])

        cln_flist = []
        cln_llist = []

        for x in clean_first_quart:
            cln = x.replace(",","")
            cln_num = float(cln)
            cln_flist.append(cln_num)

        for y in clean_last_quart:
            cln = y.replace(",","")
            cln_num = float(cln)
            cln_llist.append(cln_num)

        sec_data = {
            'firstQ': cln_flist,
            'lastQ': cln_llist
        }

        pd.options.display.float_format = '{:,.2f} %'.format
        otherDF = pd.DataFrame(sec_data, index=indexes)
        op = ((otherDF['lastQ'] - otherDF['firstQ']) * 100)/otherDF['firstQ']
        df['Valor actual'] = op

        restult_list = []
        restult_list.append(q_list)

        for z in q_list:
            lz = list(df[z])
            restult_list.append(lz)

        restult_list.append(list(round(df['Valor actual'], 2)))
        print (restult_list)

        return restult_list