from bd_reits import reits

# import pandas as pd
# import numpy as np

# indexes = ['Ingresos Totales','NOI','FFO','AFFO','Ingresos MXN','Ingresos USD',
#         'Activos Totales','Total de Patrimonio','Tasa fija','Tasa variable','Servisio de deuda',
#         'Deuda en dolares','Deuda Total','ABR','Margen ABR','NAV','Precio de cierre','CFBIs circulantes']
# list_group = []
# q_list = []
# data = {}

# for i in reits['FMTY'][2023].keys():
#     a = reits['FMTY'][2023][i]['income']
#     b = reits['FMTY'][2023][i]['debt']
#     c = reits['FMTY'][2023][i]['occupancy']
#     d = reits['FMTY'][2023][i]['analysis']

#     group = a + b + c + d
#     list_group.append(group)
#     q_list.append(i.upper())
    
# for x, y in enumerate(q_list):
#     data[y] = list_group[x]
    
# df = pd.DataFrame(data, index=indexes)

# clean_last_quart = list(df[q_list[-1]])
# clean_first_quart = list(df[q_list[0]])

# cln_flist = []
# cln_llist = []

# for x in clean_first_quart:
#     cln = x.replace(",","")
#     cln_num = float(cln)
#     cln_flist.append(cln_num)

# for y in clean_last_quart:
#     cln = y.replace(",","")
#     cln_num = float(cln)
#     cln_llist.append(cln_num)

# sec_data = {
#     'firstQ': cln_flist,
#     'lastQ': cln_llist
# }

# pd.options.display.float_format = '{:,.2f} %'.format
# otherDF = pd.DataFrame(sec_data, index=indexes)
# op = ((otherDF['lastQ'] - otherDF['firstQ']) * 100)/otherDF['firstQ']
# df['Valor actual'] = op

# restult_list = []
# restult_list.append(q_list)

# for z in q_list:
#     lz = list(df[z])
#     restult_list.append(lz)

# restult_list.append(list(round(df['Valor actual'], 2)))

# print (restult_list)