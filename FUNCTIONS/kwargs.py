def print_kwarge(**kwargs):
    for key , value in kwargs.items():
        print(f"{key}:{value}")                 #for formating in strings we use  f string


print(print_kwarge(name = "shaktiman",power = "flying", enemy ="docotr cyphrys"))