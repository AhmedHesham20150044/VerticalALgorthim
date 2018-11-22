import xlrd
def Excel_file(file):
    wb = xlrd.open_workbook(file)
    sheet = wb.sheet_by_index(0)
    List = list()
    for row in range(1,sheet.nrows):
        myset = set()
        for col in range(1, 20):
            myset.add(col)
        List.append(myset)

    return List

def Print(file) :
    data = Excel_file(file)
    for i in data :
        for j in i :
            print(j)

print("Course Evaluation .xlsx")