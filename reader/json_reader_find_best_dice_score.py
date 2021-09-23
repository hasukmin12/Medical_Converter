import json

with open('/home/has/Results/140_Ureter_test_summary.json','r') as my_json:
    my_code = json.load(my_json)

# print(my_code['results']['all'][0]['1']['Dice'])
# print(my_code['results']['all'][1]['1']['Dice'])

min = 1

# find min
print("who is min")
for i in range(59):
    dice = my_code['results']['all'][i]['1']['Dice']
    if dice <= min:
        min = dice
        print(i+240)
        print(min)


# find max
print("")
print("now we start")
print("who is max")
max = 0
for i in range(59):
    dice = my_code['results']['all'][i]['1']['Dice']
    if dice >= max:
        max = dice
        print(i+240)
        print(max)
