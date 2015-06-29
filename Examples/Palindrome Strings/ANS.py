                                            ####################################
                                            #                 ANS.py           #
                                            #       this file is part of the   #
                                            # Random Testcase Generator Script # 
                                            #          Made By- sd5869         #
                                            ####################################

#############################################################################################################
# In this file you can add your own solution with which can you  generate the output to the input Testcases #		
#############################################################################################################

##########################################################
# The function that must be used for coding the solution #
##########################################################
def run(ip,op):

	###########################################################
	# Note: Please use ip.readline() in place of input()      #
	# and use op.write() inplace of print() in your solution. #
	# Don't forget to add "\n" in op.write() whenever needed. #
	###########################################################

	###################################
	# Start solution below this block #
	###################################
    t=int(ip.readline())
    for _ in range(t-1):
        s = ip.readline()
        s=list(s)
        s.remove('\n')
        s=''.join(s)
        rs=reversed(list(s))
        if(list(s) == list(rs)):
            op.write("Palindrome"+"\n")
        else:
            op.write("Not Palindrome"+"\n")
    s = ip.readline()
    rs=reversed(s)
    """
    This needs to be done to prevent writing extra new line in output file
    """
    if(list(s) == list(rs)):
        op.write("Palindrome")
    else:
        op.write("Not Palindrome")
    
	####################################
	# Finish solution below this block #
	####################################

	#######################################################################################################
	# Don't Remove this as if Written is not printed on the Screen that means you code in having an Error #
	#######################################################################################################
    print("Written")
