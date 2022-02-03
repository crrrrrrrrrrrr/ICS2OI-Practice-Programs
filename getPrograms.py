# get programs

# 1. covert lb to kg
#weight_lbs = int (input ("Please enter your weight in pounds: "))
# convert pounds to kilograms
#weight_kgs = weight_lbs / 2.2046
# print weight in kilograms
#print ("You weigh " + str(round(weight_kgs,2)) + " kgs.")

# 2. average grade
# get name
#name = input("hi! What's your name? ")
#print ("nice to meet you " + name + "!")
# get marks
#math = int(input("what mark did you get in math? "))
#english = int(input("what mark did you get in english? "))
#history = int(input("what mark did you get in history? "))
#french = int(input("what mark did you get in french? "))
# calculate average
#average = (math + english + history + french)/4 
# print average, depending
#if average >= 85 :
  #print (name + ", you have a " + str(round(average,1)) + " average")
#else :
  #print (name + ", that's too bad, your average is " + str(round(average,2)))

# 3. daily, weekly, monthly, yearly gross pay
#hours = float(input("average hours worked per day: "))
#hour_pay = float(input("hourly pay: "))
# calculate daily, weekly, monthly, yearly
#daily = hours * hour_pay
#weekly = daily * 7
#monthly = weekly * 4
#yearly = weekly * 56
# print calculations
#print ("your daily gross pay is " + str(round(daily,2)) + """
#your weekly gross pay is """ + str(round(weekly,2)) + """
#your monthly gross pay is """ + str(round(monthly,2)) + """
#your yearly gross pay is """ + str(round(yearly,2)))

# 4. age calculations
#years = float(input("how old are you: "))
# calculate age in months, days, hours, minutes, seconds
#months = years * 12
#days = months * 30
#hours = days * 365
#minutes = hours * 60
# print ages, delay
#import time
#time.sleep (0.5)
#print ("you are " + str(round(months,0)) + " months old" + """
#you are """ + str(round(days,0)) + " days old" + """
#you are """ + str(round(hours,0)) + " hours old" + """
#you are """ + str(round(minutes,0)) + " minutes old")

# 5. conversational computer
# import time for delays
import time
# introduction
print ("hi! my name's Antikythera")
time.sleep(0.5)
print ("but you can call me Ani")
name = input ("what's your name? ")
# comment on name
if len(name) >= 7 :
  print ("wow, " + name + " is a long name!")
else :
  print (name + ", cool name")
print ("""
""")
# ask about age
age = int(input("how old will you be turning in 2022? "))
# calculate birth year 
birth_year = 2022 - age
if birth_year >= 2008 :
  print ("oh, so you were born in " + str(birth_year) + """!
did you know that the first iPhone is older than you?""")
elif birth_year == 2007 :
  print ("""born in 2007! 
you're the same age as the first iPhone""")
else :
  print ("born in " + str(birth_year) + """!
did you know that 
you're older than the first iPhone?""")
# end convo
print ("""
""")
time.sleep(1)
print ("well I gotta head out! bye!")
