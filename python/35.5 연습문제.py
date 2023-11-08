class Date:
    @staticmethod
    def is_date_valid(date_str):
        splited = date_str.split("-")
        try:
            year = int(splited[0])
            month = int(splited[1])
            day = int(splited[2])
            if year<0: return False
            if month < 0 or month > 12: return False
            if day < 0 or day > 31: return False
            return True
        except:
            return False


if Date.is_date_valid('2000-10-31'):
    print('올바른 날짜 형식입니다.')
else:
    print('잘못된 날짜 형식입니다.')

class Date:
    @staticmethod
    def is_date_valid(date_string):
        year,month,day = map(int, date_string.split("-"))
        return month<=12 and day<=31