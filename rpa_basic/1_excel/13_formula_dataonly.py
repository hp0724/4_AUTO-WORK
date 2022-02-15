from json import load
from openpyxl import load_workbook
wb =load_workbook("sample_formula.xlsx",data_only=True)
ws=wb.active


# evaluate  되지 않은 상태의 데이터는 none이라고 표시 
# 엑셀을 저장해주자 
for row in ws.values:
    for cell in row:
        print(cell)

