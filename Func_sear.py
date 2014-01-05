
def search(sorted_list, n):  
 "This will return the index of the number 'n' in the given list or -1 depending on whether 'n' is in the list or not."
 
 y = sorted(sorted_list) # Assigning sorted_list to variable y after sorting
 

 if y != sorted_list : print 'Please enter sorted list' # Checking whether given list is sorted or not

 # To figure out index of n in list
 else:
 
 
    p = 1
    for i in sorted_list:
		if n == i: 
			print 'The index of the given number in the list is ', sorted_list.index(n)
			break
		elif p == len(sorted_list): 
			print -1
		else:
			p = p + 1	 
	 



 
search([1,3,4,2], 7) 
  
  
