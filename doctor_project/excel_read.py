import pandas as pd
from curve_fitting import points_compute
excel_path = 'data.xlsx'
d = pd.read_excel(excel_path, sheet_name=0, header=0, usecols=[3, 4, 5], names=None)
print(d)
d_li = d.values.tolist()
age = []
NT_proBNP = []
Troponin = []
stroke = []
for s_li in d_li:
    age.append(int(s_li[0]))
    NT_proBNP.append(s_li[1])
    Troponin.append(1000*s_li[2])
    stroke.append(0)

# assert(len(age) == len(NT_proBNP) == len(Troponin) == len(stroke))

print(age)
print(NT_proBNP)
print(Troponin)
print(stroke)

points = points_compute(stroke, age, Troponin, NT_proBNP)

print(points)
print(len(points))
# print(d['sheet1'].NT-proBNP)