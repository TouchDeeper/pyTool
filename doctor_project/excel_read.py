import pandas as pd
from curve_fitting import points_compute
import openpyxl
# import xlwings as xw

excel_path = 'data.xlsx'
d = pd.read_excel(excel_path, sheet_name=0, header=0, usecols=[3, 4, 5, 6], names=None)
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
    if s_li[3] == "无":
        stroke.append(0)
    else:
        stroke.append(1)

# assert(len(age) == len(NT_proBNP) == len(Troponin) == len(stroke))

print(age)
print(NT_proBNP)
print(Troponin)
print(stroke)

points_age, points_Troponin, points_NT_ProBNP, points_stroke, total_points = points_compute(stroke, age, Troponin, NT_proBNP)

print(total_points)
print(len(total_points))

pd_points = pd.DataFrame({'得分': total_points})
pd_points_age = pd.DataFrame({'得分_年龄': points_age})
pd_points_Troponin = pd.DataFrame({'得分_肌钙蛋白': points_Troponin})
pd_points_NT_ProBNP = pd.DataFrame({'得分_NT_ProBNP': points_NT_ProBNP})
pd_points_stroke = pd.DataFrame({'得分_病史': points_stroke})
book = openpyxl.load_workbook(excel_path)
writer = pd.ExcelWriter(excel_path, engine='openpyxl')
writer.book = book
writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
pd_points.to_excel(writer, sheet_name="Sheet1", startcol=30, index=False)
pd_points_age.to_excel(writer, sheet_name="Sheet1", startcol=31, index=False)
pd_points_Troponin.to_excel(writer, sheet_name="Sheet1", startcol=33, index=False)
pd_points_NT_ProBNP.to_excel(writer, sheet_name="Sheet1", startcol=32, index=False)
pd_points_stroke.to_excel(writer, sheet_name="Sheet1", startcol=34, index=False)
writer.save()
# print(d['sheet1'].NT-proBNP)
