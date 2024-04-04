age = int(input())
if 0 < age < 6:
    print("khordsal")
elif 6 <= age < 10:
    print("koodak")
elif 10 <= age < 14:
    print("nojavan")
elif 14 <= age < 24:
    print("javan")
elif 24 <= age < 40:
    print("bozorgsal")
elif age >= 40:
    print("miansal")