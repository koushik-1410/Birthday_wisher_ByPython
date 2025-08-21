import pandas as pd
import datetime as dt
import pywhatkit as kit

today = dt.datetime.today()
data=pd.read_csv("birthday_dataset.csv")

def check_birthday():
    phone_no=[]
    data["Birthday"]=pd.to_datetime(data["Birthday"])
    for i in range(len(data["Birthday"])):
        if(data["Birthday"][i].day==today.day and data["Birthday"][i].month==today.month):
            phone_no.append((str(data["Phone"][i]),i))
    return phone_no


def sent_whatsappmsg(numbers):
    for i in numbers:
        num_str = str(i[0])
        if(len(num_str)==10):
           wp_no="+91"+num_str
        elif len(num_str) == 12 and num_str.startswith("91"):   # without '+'
            wp_no = "+" + num_str
        elif(len(num_str)==13):
            wp_no=num_str
        else:
            continue
        text=f"Happy Birthday! Dear {data["Names"][i[1]]}🎉 \nWishing you a day filled with love, laughter, and happiness.\nBirthday Wisher by Python"
        kit.sendwhatmsg_instantly(wp_no,text, wait_time=20, tab_close=True, close_time=7)


def main():

    numbers=check_birthday()
    print(numbers)

    if numbers:
        sent_whatsappmsg(numbers)


main()

