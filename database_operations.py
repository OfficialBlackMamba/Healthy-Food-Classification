import openpyxl

def check_database(details):
    try:
        wb = openpyxl.load_workbook("database.xlsx")
        ws = wb.active
        for row in ws.iter_rows(min_row=2, max_col=3):
            if row[2].value == details:
                return True
        return False
    except Exception as e:
        print(f"Error reading database: {str(e)}")
        return False
