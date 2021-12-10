import openpyxl
from selenium import webdriver
path = 'C:\excel sheets\Book1.xlsx'
workbook = openpyxl.load_workbook(path)
sheet = workbook.active


for r in range(4,7):
    for c in range(1,4):
        sheet.cell(row=r,column=c).value='welcome'

    workbook.save(path)