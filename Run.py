                                            ####################################
                                            # Random Testcase Generator Script # 
                                            #           By- sd5869             #
                                            ####################################

#####################
# Importing Modules #
#####################

import random
import string

#############################################################
# The Dictionary storing all information about the testcase #
#############################################################

testcase_info=dict()

###############################################################################################################
# Getting basic information i.e number of test files, testcase in each file, number of lines in each testcase #
###############################################################################################################

print("Enter number of test files to be generated")
files=int(input())
print("Enter number of testcases in each file")
t=int(input())
print("Enter number of lines in each testcase")
num_lines=int(input())

#####################################################################################
# This Loop Handles all the input part and collects the details about the testcase. #
#####################################################################################

for i in range(num_lines):
    print("What is in Line "+str(i+1)+" Enter i for integer and l for a list whose elements will be arranged randomly")
    typ=(input())

    ################################
    # Integer information Handling #
    ################################

    if(typ=="i"):

        #############################################
        # Some initialisations for Integer Handling #
        #############################################

        Lower=list()
        Upper=list()

        ####################################################################################################
        # Getting more information i.e number of integers in one line, Range of each integer [Lower,Upper] #
        ####################################################################################################

        print("Enter number of integers in line "+str(i+1))
        num_ele=int(input())
        print("Do you want to add the number of integers present before the integers y/n")
        write_number_of_elements=input()
        for j in range(num_ele):
            print("Enter Range of integer "+str(j+1)+" in line "+str(i+1))
            low=int(input())
            up=int(input())
            Lower.append(low)
            Upper.append(up)
            print("Do you want to repeat this range for all integers y/n")
            ans=input()
            if(ans=="y"):
                while(j<num_ele-1):
                    Lower.append(low)
                    Upper.append(up)
                    j+=1
                break

                #######################################
                # Packing all details into dictionary #
                #######################################

        testcase_info[i]=[typ,num_ele,write_number_of_elements,Lower,Upper]

        #############################
        # List Information Handling #
        #############################

    elif(typ=="l"):

        ##########################################
        # Some initialisations for List Handling #
        ##########################################

        element_list=list()
        a=str()
        print("is the List Details present in List_Resource.py file y/n")
        ans=input()
        if(ans=="y"):

            ####################################################
            # Extracting all details from List_Resource Module #
            ####################################################

            from List_Resource import *
            testcase_info[i]=[typ,num_ele,write_number_of_elements,Repeat,element_list]
        else:

            #########################################################################################
            # Getting information like all elements of list and Repetition of elements in same line #
            #########################################################################################

            print("Enter elements of List and terminate by typing NULL")
            while(a!="NULL"):
                a=input()
                if(a!="NULL"):
                    element_list.append(a)
            print("Enter number of elements from the list to be added in line "+str(i+1))
            num_ele=int(input())
            print("Do you want to add the number of elements present before the list elements y/n")
            write_number_of_elements=(input())
            print("Do you want to repeat number of elements from list in same line y/n")
            Repeat=(input())

                #######################################
                # Packing all details into dictionary #
                #######################################

            testcase_info[i]=[typ,num_ele,write_number_of_elements,Repeat,element_list]
    else:
        raise "INVALID INPUT"

######################################################################################
# This Loop Handles all the part which involves writing in the input and output file #
######################################################################################

for i in range(files):  
    ip = open('input'+str(i)+'.txt', 'w')
    print("Do you want to Write the number of testcases in input file "+str(i+1)+" on first line")
    ans=input()
    if(ans=="y"):
        ip.write(str(t)+"\n")
    for j in range(t):
        for k in range(num_lines):

                #########################
                # Integer File Handling #
                #########################

            if(testcase_info[k][0]=="i"):

                    #####################################
                    # Unpacking Details from Dictionary #
                    #####################################

                [typ,num_ele,write_number_of_elements,Lower,Upper]=testcase_info[k]

                if(write_number_of_elements=="y"):
                    ip.write(str(num_ele)+"\n")
                for l in range(num_ele):
                    if l!=num_ele-1:
                        ip.write(str(random.randrange(Lower[l],Upper[l]+1))+" ")
                    else:
                        ip.write(str(random.randrange(Lower[l],Upper[l]+1)))

                ######################
                # List File Handling #
                ######################

            elif(testcase_info[k][0]=="l"):

                    #####################################
                    # Unpacking Details from Dictionary #
                    #####################################

                [typ,num_ele,write_number_of_elements,Repeat,element_list]=testcase_info[k]
                if(write_number_of_elements=="y"):
                    ip.write(str(num_ele)+"\n")
                if(Repeat=="y"):
                    for l in range(num_ele):
                        if l!=num_ele-1:
                            ip.write(str(random.choice(element_list)+" "))
                        else:
                            ip.write(str(random.choice(element_list)))
                else:

                    #################################################################
                    # Code for Generating non Repetitive Random chocies from a List #
                    #################################################################

                    templist=list(element_list)
                    random.shuffle(templist)
                    for l in range(num_ele):
                        ele=random.choice(templist)
                        if l!=num_ele-1:
                            ip.write(str(ele)+" ")
                        else:
                            ip.write(str(ele))
                        templist.remove(ele)
                        if(templist==[]):
                            raise "Number of Elements are too few they can't be arranged without repetition"
            """
            This is done to add new line after every testcase except for last one
            """
            if(j!=t-1):
                ip.write("\n")
    ip.close()
    print("Do you want output file also y/n")
    ans=input()
    if(ans=="y"):

        #########################################################
        # The ANS module is having the solution in run Function #
        #########################################################

        from ANS import *
        op = open('output'+ str(i)+'.txt','w')
        ip = open('input'+str(i)+'.txt', 'r')
        run(ip,op)

        #####################
        # Closing all files #
        #####################

        op.close()
        ip.close()

                                            ##########################################
                                            # For any bugs or feature request please #
                                            #       Contact: sd5869@gmail.com        #
                                            ##########################################        
