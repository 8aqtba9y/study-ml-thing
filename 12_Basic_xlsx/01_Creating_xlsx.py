import openpyxl.styles

# workbook生成
workbook = openpyxl.Workbook()

sheet = workbook.active

sheet["A1"] = "テストファイル"
sheet["A2"] = "おはようございます"
sheet.merge_cells("A1:C1")
sheet["A1"].font = openpyxl.styles.Font(size=20,color="FF0000")

# workbook保存
workbook.save("01_newFile.xlsx")