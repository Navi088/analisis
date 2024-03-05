from bd_reits import reits

class MainClass:
    def single_reit(a, b, c):
        income_list = reits[a][b][c]['income']
        income = list(income_list)

        debt_list = reits[a][b][c]['debt']
        debt = list(debt_list)

        occupancy_list = reits[a][b][c]['occupancy']
        occupancy = list(occupancy_list)

        analysis_list = reits[a][b][c]['analysis']
        analysis = list(analysis_list)

        result_list = [income, debt, occupancy, analysis]
        
        return result_list