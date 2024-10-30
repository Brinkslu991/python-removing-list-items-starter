# Lucas Brinks
# 10/30/24
# del/remove/pop

import time

#bands = ['Shinedown','Gemini Syndrome','Three Days Grace','Fury','Avenged Sevenfold','Dragonforce','Falling In Reverse']

#bands.pop(3)
#bands.remove('Dragonforce')
#del bands[0]

#print(bands)

people = ['Josh','Bryce','Thayer','Hunter','Matt']

people.remove('Bryce')

print('Bryce cannot make it.')
print(people)

print('I can only invite two people to the dinner because my new table wont arrive in time.')
time.sleep(1)
people.pop(2)
people.pop(0)

print('Josh and Hunter I cannot invite you to my dinner.')

print(people)

del people[0]
del people[0]

print(people)