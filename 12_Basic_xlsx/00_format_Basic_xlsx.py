# xlsx => workbook > sheet > rows, columns

# add modules
import openpyxl

# xlsxファイルを読み込み、workbook変数に当て込む
workbook = openpyxl.load_workbook("00_stat_104102.xlsx")

# method1: sheet名からsheetを取得
# print(book.get_sheet_names())
# sheet = book.get_sheet_by_name("Sheet0")

# method2: sheet番号からsheetを取得
sheet = workbook.worksheets[0]
for row in sheet.rows: # rows """Iterate over all rows in the worksheet"""
    for column in row:
        print(column.value, end=" ")
    print()
