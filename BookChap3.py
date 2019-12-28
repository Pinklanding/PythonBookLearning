
bicycles=["a111","bbb","cc","dxd"]
print(bicycles[1].title())

print(bicycles[-1])

#n=input("Which one is your bick?")
#n=int(n)-1
#msg = "My bike is a "+bicycles[n].title()+"."
#print(msg)

names = ["adf","deg","goep","nie"]
for name in names:
    print(name)

moto = ["honda", "ymh", "szk"]
print(moto)
moto[0] = "dcat"
print(moto)
moto.append("honda")
print(moto)

moto.insert(0,"dkt")
print(moto)

del moto[3]
print(moto)

moto.pop()
print(moto)

moto.pop(0)
print(moto)

moto.remove("ymh")
print(moto)

too_expsv = "dcat"
to_remove = too_expsv
moto = moto.remove(to_remove)
print(moto)
print("\nA "+to_remove.title()+" is removed.")
print("\nA "+too_expsv.title()+" is too expensive.\n\n\n")

guests = ["ama", "bent", "candy", "dice", "envy"]
cnt_come = "ama"
new_guest = "fen"
new_vip = "zeto"

def invite_list (list,nocome,newone,vip):
    list.remove(nocome);
    list.append(newone);
    list.insert(0,vip);
    for eachone in list:
        print("Hi " + eachone.title()+ ", will you join me?");

    print("Sorry, we can only invite two")

    while len(list)>2:
        delete_one = list.pop()
        print("Sorry "+delete_one.title()+", you are not in the list now.")

    for eachone in list:
        print("Hi " + eachone.title() + ", you are still invited.");

    print("we invited "+ str(len(list)) + " guests to this party.")
    print("The party is finished.")

    list.pop()
    list.pop()

    if len(list)==0:
        print("The list is empty.\n\n")


guests1 = ["ama", "bent", "candy", "dice", "envy"]
invite_list(guests1,cnt_come,new_guest,new_vip)
guests2 = ["ama", "qenty", "candy", "picky", "envy"]
invite_list(guests2,"qenty","harry","winny")

guests.sort()
print(guests)

guests.sort(reverse=True)
print(guests)

sorted(guests)
print(sorted(guests))
print(guests)

guests.reverse()
print(guests)

def travel_list():
    cities=[]
    for city in input().split(","):
        cities.append(city)

    print("Original")
    print(cities)

    print("sorted()")
    sorted_cities = sorted(cities)
    print(sorted_cities)

    print("Original")
    print(cities)

    print("reverse sorted()")
    sorted_cities = sorted(cities,reverse=True)
    print(sorted_cities)

    print("Original")
    print(cities)

    print("sort()")
    cities.sort()
    print(cities)

    print("reverse()")
    cities.reverse()
    print(cities)


travel_list()