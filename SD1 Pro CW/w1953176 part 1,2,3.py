# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
#Student ID:w1953176  ,  20220243 
 
#Date:2022.12.12


progress=0
trailer=0
retriver=0
excluded=0
outcomes=0
mylist=[]
lists=[]

x="y"
while x=="y":
    try:
        
        while True:
            try:
                #getting student pass credit
                Pass=int(input("enter your credits at pass:"))
                if Pass in range(0,121,20):
                    break
                else:
                    print("out of range")
            except ValueError:
                #validating the integer
                print("integer required")
                
        while True:
            try:
                #getting student defer credit
                defer=int(input("enter your credit at defer:"))
                if defer in range(0,121,20):
                    break
                else:
                    #check the range
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


#total=120
    total=Pass+defer+fail
    if total!=120:
        print("total incorrect")
        continue

    if Pass==120:
        print("progress")
        progress+=1
        mylist = "{} - {},{},{}".format('progress',Pass,defer,fail)
    elif Pass==100:
        print("progress(module trailer)")
        trailer+=1
        mylist = "{} - {},{},{}".format('progress(module trailer)',Pass,defer,fail)
    elif 0<=fail<=60:
        print("Do not Progress-module retriever")
        retriver+=1
        mylist = "{} - {},{},{}".format('do not progress-module retriver',Pass,defer,fail) 
    else:
        print("exclude")
        excluded+=1
        mylist ="{} - {},{},{}".format('exclude',Pass,defer,fail)
        
    lists.append(mylist)
    outcomes+=1
    print("would you like to enter another set of data?")
    while True:
        
        
        x=(input("Enter 'y' for yes or 'q' to quit and view results:"))
        if x=="y" or x=="q":
            break
        else:
            print("Enter y or q")
def histrogram():
    print("--------------------------------------------------------------- ")
    print("Histogram")
    print("progress",progress,":",progress*"*")
    print("trailer",trailer,  ":",trailer*"*")
    print("retriver",retriver,":",retriver*"*")
    print("excluded",excluded,":",excluded*"*")
    print(outcomes,"outcomes in total")
    print("--------------------------------------------------------------- ")
histrogram()


print("part 2:")
for p in lists:
        print(p) 
        
        
print("part 3:")

file=open("file.txt",'w')
for p in lists:
    file.write(p)
    file.write('\n')
file.close()



file=open("file.txt",'r')
for i in file:
    print(i,end="")
file.close()



    
                
