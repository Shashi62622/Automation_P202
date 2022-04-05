import xlrd

def read_locator(sheetname):
    workbook = xlrd.open_workbook("./data_source/datasheet.xls")
    worksheet = workbook.sheet_by_name(sheetname)
    rows = worksheet.get_rows()
    next(rows)

    locators = {row[0].value: (row[1].value, row[2].value) for row in rows}
    return locators






