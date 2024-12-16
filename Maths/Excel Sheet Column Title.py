# TC: O(LogN) Log base 26 of n
def getExcelColumn(columnNum):
    res = ""
    while columnNum > 0:
        rem = (columnNum - 1) % 26
        res += chr(ord("A") + rem)
        columnNum = (columnNum - 1) // 26

    return res[::-1]


print(getExcelColumn(78))
