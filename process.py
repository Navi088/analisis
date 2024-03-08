from bd_reits import reits

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