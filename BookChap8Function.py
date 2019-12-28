# def describe_pet(pname,ptype = 'dog'):
#     print(pname.title())
#     print(ptype)
#
# describe_pet('andy')
# describe_pet('billy','cat')
#
# def get_fine_name(fname,lname,mname = ''):
#     if mname:
#         fullname = fname.title() + ' ' + mname.title() + ' ' + lname.title()
#     else:
#         fullname = fname.title() + ' ' + lname.title()
#     return fullname
#
# finename1 = get_fine_name("df","gegeg")
# print(finename1)
#
# finename2 = get_fine_name("df","gegeg",'tere')
# print(finename2)
#
# active = True
# n=0
# while active:
#     print("\nInput your name:")
#     fname = input('f')
#     mname = input('m')
#     lname = input('l')
#
#     finename = get_fine_name(fname, mname, lname)
#
#     print("hello, " + finename)
#
#     n += 1
#     if n>2:
#         active = False

# def greet(names):
#     for name in names:
#         print('Hello ' + name)
#
# names = ['a','b','c']
# greet(names)

### function_name(list_name[:])##### use a copy of original lists, not the original one.
#
# def make_pizza(size, *toppings):#### * means new a empty tuple, this one should be at the last of ()
#     print(size)
#     print(toppings)
#
# make_pizza(12, 'a','c','v','e')
#
# def user_profile(first, last, **userinfo):#### ** means new a empty dictionary, should be at the last position.
#     profile = {}
#     profile['name']=first.title()+' '+last.title()
#
#     #print(userinfo)
#     for key, value in userinfo.items():
#         profile[key] = value
#
#     return  profile
#
# profile1 = user_profile("a","b",sss='fdfw',ggg='cwe',qq='ggeg')
#
# print(profile1)

#####pizza.py -> import pizza; then you can use all the functions in pizza.py
##### module_name.function_name()
##### from module_name import function_name as fn
##### from module_name import *
##### import module_name as mn

