import xlrd
from Table import Iteration


# Scores.xlsx

def check(item):
    if 100 > item > 84:
        return "Superior"
    elif 85 > item > 74:
        return "Top Level"
    elif 75 > item > 64:
        return "Ranking"
    else:
        return "Low Level"


class Excel:
    def __init__(self):
        wb = xlrd.open_workbook("Scores.xlsx")
        self.sheet = wb.sheet_by_index(0)
        pass

    def get_data(self):
        table = Iteration()
        for row in range(1, self.sheet.nrows):
            for col in range(0, 3):
                item = {check(self.sheet.cell_value(row, col))}
                table.add(item, row)
        return table

