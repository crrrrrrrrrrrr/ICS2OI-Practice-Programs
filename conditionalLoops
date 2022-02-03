# conditional loops

# 11.a mortgage payment
# variables
year = 1
initial_mortgage = 120000
rate = 0.0775
interest = 0
total = 120000.00
payment = 24000
# table titles
print ("year     inital mortgage      interest       total due")

while total > 0:
  interest = initial_mortgage * rate
  total = initial_mortgage + interest

  print (str(year) + "         " + str(round(initial_mortgage,2)) + "               " + str(round(interest,2)) + "         " + str(round(total,2)))
  year+=1

  initial_mortgage = total - payment
  if total - payment <=0:
    break

print ("mortgage paid off in " +  str(year) + " years")
