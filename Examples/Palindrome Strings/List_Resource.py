                                            ####################################
                                            #	      List_Resource.py	       #
                                            #	    this file is part of the   #
                                            # Random Testcase Generator Script # 
                                            #          Made By- sd5869         #
                                            ####################################

#####################################################################################
# In this file you can generate your own list according to requirements of testcase #
#####################################################################################

##################################################################
# The function that must be used for Generating you desired List #
##################################################################

import random
import string
def listgen():
        L=list()
        for ele in range(10000):
                tmp_str=''.join(random.choice(string.ascii_lowercase) for _ in range(random.randrange(1,101)))
                L.append(tmp_str)
                tmp_str=''.join(random.choice(string.ascii_lowercase) for _ in range(random.randrange(1,51)))
                rev=list(tmp_str)
                rev.reverse()
                rev_str=''.join(rev)
                L.append(tmp_str+rev_str)
        random.shuffle(L)
        return L

#######################################################################################################
# The details of following parameters must be provided for the successful generation of the testcases #															#
# num_ele: it stands for the number of elements to be written from the list in a line 		      #
# write_number_of_elements: it stands for writing num_ele on file or not (set = to "y" for yes)       #
# Repeat: it stands for repeating the elements of list in same line or not (set = "y" for yes)        #
# element_list: it contains all elements of list that we want to be written			      #
#######################################################################################################

num_ele=1
write_number_of_elements="n"
Repeat="y"
element_list=list(listgen())
