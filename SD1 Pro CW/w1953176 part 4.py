progress=0
trailer=0
retriver=0
excluded=0
outcomes=0


dictionary={}

x="y"
while x=="y":
    try:
        
        while True:
            dicti=input("input your user id:")
            try:
                Pass=int(input("enter your credits at pass:"))
                if Pass in range(0,121,20):
                    break
                else:
                    print("out of range")
            except ValueError:
                print("integer required")
                
        while True:
            try:
                defer=int(input("enter your credit at defer:"))
                if defer in range(0,121,20):
                    break
                else:
                    print("out of range")
            except ValueError:
                print("integer required")
                
        while True:
            try:
                fail=int(input("enter your credit at fail:"))
                if fail in range(0,121,20):
                    break
                else:
                    print("out of range")
            except ValueError:
                print("integer required")
    except:
        continue



    total=Pass+defer+fail
    if total!=120:
        print("total incorrect")
        continue

    if Pass==120:
        print("progress")
        progress+=1
        dictionary[dicti] = "{} - {},{},{}".format('progress',Pass,defer,fail)
    elif Pass==100:
        print("progress(module trailer)")
        trailer+=1
        dictionary[dicti] = "{} - {},{},{}".format('progress(module trailer)',Pass,defer,fail)
    elif 0<=fail<=60:
        print("Do not Progress-module retriever")
        retriver+=1
        dictionary [dicti]= "{} - {},{},{}".format('do not progress-module retriver',Pass,defer,fail) 
    else:
        print("exclude")
        excluded+=1
        dictionary[dicti] ="{} - {},{},{}".format('exclude',Pass,defer,fail)
        

    print("would you like to enter another set of data?")
    while True:
        
        
        x=(input("Enter 'y' for yes or 'q' to quit and view results:"))
        if x=="y" or x=="q":
            break
        else:
            print("Enter y or q")
print("--------------------------------------------------------------- ")
print("Histogram")
print("progress",progress,":",progress*"*")
print("trailer",trailer,  ":",trailer*"*")
print("retriver",retriver,":",retriver*"*")
print("excluded",excluded,":",excluded*"*")
print(outcomes,"outcomes in total")
print("--------------------------------------------------------------- ")



for key,value in dictionary.items():
    print(key,' : ',value)

