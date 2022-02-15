from openpyxl import load_workbook
wb=load_workbook("sample.xlsx")
ws = wb.active

# ws.insert_rows(8) # 8번째 줄에 공간 삽입
# ws.insert_rows(8,5) # 8번째 줄 위치에 5 삽입
# wb.save("sample_insert_rows.xlsx")
#ws.insert_cols(2) # B번쨰 열이 비워짐 
ws.insert_cols(2,3)
wb.save("sample_insert_cols.xlsx")
