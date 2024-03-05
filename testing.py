from bd_reits import reits

# BUSCAR FIBRAS
income_list = reits['FUNO'][2023]['q1']['income']
income = list(income_list)

debt_list = reits['FUNO'][2023]['q1']['debt']
debt = list(debt_list)

occupancy_list = reits['FUNO'][2023]['q1']['occupancy']
occupancy = list(occupancy_list)

analysis_list = reits['FUNO'][2023]['q1']['analysis']
analysis = list(analysis_list)

result_list = [income, debt, occupancy, analysis]
print (result_list[3][1])