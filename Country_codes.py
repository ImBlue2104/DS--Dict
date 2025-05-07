country_codes = {
    'India': 93672,
    "Australia": 20183,
    'New Zealand': 93213 
    }

#acceses India's code:
print("India's country code: ")
print(country_codes.get('India', "Not Found"))

#acceses Japan's code;
print("Japan's country code: ")
print(country_codes.get('Japan', "Not Found"))#prints not found since japan is not in dict.