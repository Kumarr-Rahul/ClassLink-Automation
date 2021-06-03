from script import send, send1, send2, send3, send4, send5
import schedule
import time

#Maths
schedule.every().monday.at("05:30").do(send)
schedule.every().tuesday.at("06:30").do(send)
schedule.every().wednesday.at("06:30").do(send)
schedule.every().friday.at("08:30").do(send)

#Formal Language & Automata theory
schedule.every().monday.at("08:30").do(send1)
schedule.every().tuesday.at("05:30").do(send1)
schedule.every().thursday.at("05:30").do(send1)

#Computer Architecture
schedule.every().tuesday.at("08:30").do(send2)
schedule.every().wednesday.at("08:30").do(send2)
schedule.every().thursday.at("08:30").do(send2)

#Design And Analysis of Algorithm
schedule.every().wednesday.at("04:30").do(send3)
schedule.every().thursday.at("06:30").do(send3)
schedule.every().friday.at("04:30").do(send3)

#Environmental Science
schedule.every().monday.at("10:30").do(send4)
schedule.every().tuesday.at("09:30").do(send4)
schedule.every().thursday.at("09:30").do(send4)

#Biology
schedule.every().tuesday.at("10:30").do(send5)
schedule.every().wednesday.at("09:30").do(send4)
schedule.every().thursday.at("10:30").do(send4)

while True:
    schedule.run_pending()
    time.sleep(1)