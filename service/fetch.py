import requests
import re
import datetime
import pickle

from bs4 import BeautifulSoup
from utls import monthToNum

url = "https://www.myhora.com/%E0%B8%9B%E0%B8%8F%E0%B8%B4%E0%B8%97%E0%B8%B4%E0%B8%99/%E0%B8%A7%E0%B8%B1%E0%B8%99%E0%B8%9E%E0%B8%A3%E0%B8%B0.aspx"

regex_date = re.compile(r'(0?[1-9]|[12]\d|30|31) (มกราคม|กุมภาพันธ์|มีนาคม|เมษายน|พฤษภาคม|มิถุนายน|กรกฎาคม|สิงหาคม|กันยายน|ตุลาคม|พฤศจิกายน|ธันวาคม) (\d{4}|\d{2})')
regex_quarter = re.compile(r'(ขึ้น|แรม) (๐|[๐-๙][๐-๙]?|๓๑) ค่ำ')
regex_month = re.compile(r'(?<=\()(๐|[๐-๙][๐-๙]?|๑๐๐)(?=\))')
regex_year = re.compile(r'ปี(.*?)\(')
regex_year_not_bracket = re.compile(r'ปี(.*)')

r = requests.get(url)

b = BeautifulSoup(r.text, "html.parser")
row = b.find_all("div", {"id": "print_div1"})

result = []

for data in row:
    col = data.find_all("div", {"class": "bud-day"})

    for cols in col:
        # Get Data
        date = regex_date.findall(cols.text)
        quarter = regex_quarter.findall(cols.text)
        month_quarter = regex_month.findall(cols.text)
        year_quarter = regex_year.findall(cols.text)
        year_not_bracket = regex_year_not_bracket.findall(cols.text)

        # Format month to number month
        month = monthToNum(date[0][1])

        # Format string to datetime
        date = datetime.date(int(date[0][2])-543, month, int(date[0][0])).isoformat()

        result.append({
            "date": date,
            "type": 0 if quarter[0][0] == "แรม" else 1,
            "type_num": int(quarter[0][1]),
            "month": int(month_quarter[0], 10),
            "year": (year_quarter if len(year_quarter) > 0 else year_not_bracket)[0]
        })

pickle.dump(result, open("bud.pkl", "wb"))