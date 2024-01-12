import random #ایمپورت کن یا وارد کن کتابخانه رندوم را برای انتخاب های تصادفی


Current = 0#  متغییر کورنتبا مقدار صفر یعنی خالی
A = 0
B = 0
A = random.randint(1, 2)# اگر بخواهیم اعداد تصادفی رادر یک حلقه بی پایان تکرار کنیم از این دستور استفاده میکینم
B = random.randint(1, 2)
# noinspection PyRedeclaration
Current = random.randint(1, 2)

print("if a=1:dirty else if A =2:clean")
print("ifB=1:dirty else if B=2:clean")
print("-------------------------------------------")
print("if Current = 1 : location is A else if Current = 2 : location is B")
print("-------------------------------------------")
print(f"A = {A} B = {B} Current = {Current}")
print("-------------------------------------------")
if Current == 1:
    print("our location in A")
    if A == 1:
        print("location A is dirty")
        A = 2
        print("A has been cleaned")
        print("moving location to B")# حرکت کند به لوکیشن خانه بی
        if B == 1:
            print("location B is dirty")  # چاپ کن لوکیشن یا محل خانه مورد نظر را
            B = 2
            print("B has been cleaned")
        else:
            print("B is clean")
    elif A == 2:
        print("A has been cleaned")
        if B == 2:
            print("B has been cleaned")
        elif B == 1:# اگر برای مثال خانه بی برابر با 1 بود در خط بعدی چاپ کند لوکیشن خانه بی را
            print("location B is dirty")
            B = 2
            print("B has been cleaned")
elif Current == 2:
    print("our location in B")
    if B == 1:
        print("location B is dirty")
        B = 2
        print("B has been cleaned")
        print("moving location to A")
        if A == 1:
            print("location A is dirty")
            A = 2
            print("A has been cleaned")
        else:
            print("A is clean")
    elif B == 2:
        print("B has been cleaned")
        if A == 2:
            print("A has been cleaned")
        elif A == 1:
            print("location A is dirty")
            A = 2
            print("A has been cleaned")
#صبا 