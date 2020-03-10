# import xlrd



# file = xlrd.open_workbook('data_ptabc.xlsx')
# sheet = file.sheet_by_index(0)
# print(sheet.nrows,sheet.ncols)
# sheet = file.sheet_by_name('Data Karyawan')
# print(sheet.nrows, sheet.ncols)


# import csv

# with open('data_ptabc.csv', 'w', newline='')as file:
#     kolom = list(out[0].keys())
#     tulis =csv.DctWriter(file,fieldnames=kolom)
#     tulis.writeheader()
    # tulis.writerows(out)


# import json
# with open('data_ptabc.json','w')as file:
    #  json.dump(out, file)