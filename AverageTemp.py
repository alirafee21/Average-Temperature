months = ["January", "Feburary","March", "April", "May", "June", "July", "August", "September", "October","November", "December"]
highs = []
lows = []
ranges=[]
b = 0


#questions for daytime highs loop
for month in months:
    highs.append(float(input("what is the daytime high in" + ' ' + month + str("? ") ).lower()))


#questions for nighttime lows loop
for month in months:
    lows.append(float(input("what is the nighttime low in" + ' ' + month + str("? ") ).lower()))

#average caluculator for average daytime high
sum = 0
for num in highs:
    sum = sum + num
    avg = sum / len(highs)
print ("Your yearly daytime average high is", " " + str(round(avg,1)),"°C")

#average caluculator for average nighttime low
sum = 0
for num in lows:
    sum = sum + num
    avg = sum / len(highs)
print ("Your yearly nighttime average low is", " " + str(round(avg,1)),"°C")

#range caluculator for highs and lows
y = len(months)
differences=[]
for (x) in range (y):
    x1 = highs[x]
    x2 = lows[x]
    totalx = x1-x2
    differences.append(round(totalx,1))
print ("your temperature ranges for each month are"," "+ str(differences))

#maximum average temperature difference caluculator
max_temp = max(differences)
index = differences.index(max_temp)
largemonth = months[index]
print(str(largemonth) + "", "has the largest average difference, the average difference is","" + str(max_temp))

#minimum average temperature difference caluculator
min_temp = min(differences)
index =differences.index(min_temp)
smallmonth = months[index]
print(str(smallmonth) + "", "has the smallest average difference, the average difference is","" + str(min_temp))
