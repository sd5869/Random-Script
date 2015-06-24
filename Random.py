import random
import string
"""
Some initialisations
"""
ni=list() #number of elements
L=list() #lower limit
U=list() # upper limit
a=str()
pni=list()# print number of elements or not
rlist=list()#random element list temp
elelist=dict()# random element list
ans=list()# ans list for s,i,l
slen=int()#string length list
print("Enter number of test files to be generated")
f=int(input())
print("Enter number of testcases in each file")
t=int(input())
print("Enter number of lines in each testcase")
nl=int(input())
for x in range(nl):
    print("What is in Line "+str(x+1)+" Enter i for integer, s for string and l for a list which will be arranged Randomly")
    ans.append(input())
    if(ans[x]=="i"):
        print("Enter number of integers in line "+str(x+1))
        ni.append(int(input()))
        print("Do you want to add the number of integers present before the integers y/n")
        pni.append(input())
        print("Enter range of each integer in line "+str(x+1)+"(first lower limit then upper limit)")
        for _ in range(ni[x]):
            L.append(int(input()))
            U.append(int(input()))
        elelist[x]=[L,U]
        L=list()
        U=list()
    elif(ans[x]=="l"):
        print("Enter elements of a list which will be selected and arranged randomly terminate by typing NULL")
        while(a!="NULL"):
            a=input()
            if(a!="NULL"):
                rlist.append(a)
        elelist[x]=rlist
        rlist=list()
        print("Enter number of elements from the list to be added in line "+str(x+1))
        ni.append(int(input()))
        print("Do you want to add the number of elements present before the list elements y/n")
        pni.append(input())
    elif(ans[x]=="s"):
        print("Enter number of strings in line "+str(x+1))
        ni.append(int(input()))
        print("Enter length of the string")
        slen=int(input())
        elelist[x]=slen
        print("Do you want to add the number of strings present before the strings y/n")
        pni.append(input())
    else:
        print("INVALID INPUT")
for i in range(f):  
    ip = open('input'+str(i)+'.txt', 'w')
    print("Do you want to Write the number of testcases in input file "+str(i+1)+" on first line")
    Ans=input()
    if(Ans in ["yes","Y","YES","Yes","y"]):
        ip.write(str(t)+"\n")
    for x in range(t):
        for j in range(nl):
            if(ans[j]=="i"):
                for k in range(ni[j]):
                    if pni[k]=="y":
                        ip.write(str(ni[j])+"\n")
                    if k!=ni[j]-1:
                        ip.write(str(random.randrange(elelist[j][0][k],elelist[j][1][k]+1))+" ")
                    else:
                        ip.write(str(random.randrange(elelist[j][0][k],elelist[j][1][k]+1)))
            elif(ans[j]=="l"):
                  for k in range(ni[j]):
                    if pni[k]=="y":
                        ip.write(str(ni[j])+"\n")
                    if k!=ni[j]-1:
                        ip.write(str(random.choice(elelist[j])+" "))
                    else:
                        ip.write(str(random.choice(elelist[j])))
            elif(ans[j]=="s"):
                  for k in range(ni[j]):
                    if pni[k]=="y":
                        ip.write(str(elelist[j])+"\n")
                    if k!=ni[j]-1:
                        ip.write(str(''.join(random.choice(string.ascii_lowercase) for _ in range(elelist[j])))+" ")
                    else:
                        ip.write(str(''.join(random.choice(string.ascii_lowercase) for _ in range(elelist[j]))))
            ip.write("\n")
              
    ip.close()
    print("Do you want output file also y/n")
    Ans=input()
    if(ans=="y"):
        """
        The module having the solution
        """
        from ANS import *
        op = open('output'+ str(i)+'.txt','w')
        ip = open('input'+str(i)+'.txt', 'r')
        run(ip,op)
        op.close()
        ip.close()
