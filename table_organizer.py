from openpyxl import Workbook


wb = Workbook()
sheet = wb.active

lines = []
with open("players.txt") as f:
    lines = f.readlines()

sheet.insert_rows(idx=1, amount=len(lines))
sheet.insert_cols(idx=1, amount=6)
for i, line in enumerate(lines, 2):
    sheet[f"A{i}"],sheet[f"B{i}"],sheet[f"C{i}"],sheet[f"D{i}"],sheet[f"E{i}"],sheet[f"F{i}"],sheet[f"G{i}"] = line[2:5], line[7:12], line[15:19], line[21:43], line[43:82], line[82:90], line[92:98]

wb.save(filename="table_organizer.xlsx")