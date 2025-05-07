#intialize dict
test_dict = {'Class': 2, 'Grade': 2, 'Roll_num': 2, 'ranking': 2, "fav": 1}

#prints test dict
print("Original Dictionary:"+ str(test_dict))

k = 2

reps = 0
for key in test_dict:
    if test_dict[key] == k:
        reps = reps+1
print(f"The number of times {k} is repeated is {reps}")