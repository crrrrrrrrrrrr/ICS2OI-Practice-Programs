# counted loops
#1. averaging marks
#number_marks = int(input("# of marks: "))
#number = number_marks
# declare variables
#total_sum = 0
#while number > 0:
  # get mark
  #mark = int(input("enter mark: "))
  # add mark to total sum
  #total_sum = total_sum + mark
  # clear mark, subtract counter
  #mark = 0
  #number = number - 1
# calculate average
#average = total_sum / number_marks
#print ("the average is " + str(round(average,2)))

#2. perfect squares
#print ("number   square")
# calculate and print squares
#number = 1
#while number < 7:
  # print number and square
 # print (str(number) + "        " + str(number**2))
  # increase counter
  #number += 1
#print ("   done")

#3. coundown to rocket!
#print ("get ready!")
#import time
#time.sleep (0.5)
#number = 5
#while number > 0:
 # print (str(number), end=" ",flush=True)
  #print (str(number))
  #time.sleep (1)
  #number -= 1
#print ("""
#blastoff!""")

#4. counting by 5s
# get number
#number = int(input("enter a number from 50-100: "))
#counter = 100
# print numbers counting down
#while counter >= number:
  #print (counter)
  #counter -= 5

#5. bank balance
# variables
#i_balance = 1000.00
#interest_rate = 0.06
#interest = 0
#balance = 1000
#year = 1
# print titles
#print ("year    initial balance     interest     balance")
#while year <= 10:
  # calculate interest, balance
  #interest = i_balance * interest_rate
  #balance = interest + i_balance
  # print results
  #print (str(year) + "         " + str(round(i_balance,1)) + "           " + str(round(interest,1)) + "          " + str(round(balance,1)))
  # next year
  #year += 1
  #i_balance = balance

#6. random numbers from range
#import random
# loop for 10 numbers
#x = 1
#while x <11 :
  #print (round(random.uniform(4,5),2))
  #print (random.randrange(0,10)) 
  #print (random.randint(20,30))
  #x += 1
