import openpyxl
path = 'C:\excel sheets\Book1.xlsx'
workbook = openpyxl.load_workbook(path)
sheet2 = workbook.active


for r in range(4, 7):
    for c in range(1, 4):
        sheet2.cell(row=r, column=c).value = 'Python'

    workbook.save(path)