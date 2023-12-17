#Given two binary strings str1 and str2, return their sum as a binary string.
#  str1 and str2 consist of 0 or 1 characters only.
#  cannot use int() method
#  str1 and str2 are non-empty strings

str1 = '1111' 
str2 = '111'

def add_binary_method(str1, str2):
  return bin(int(str1, 2) + int(str2, 2))[2:]

#print(add_binary_method(str1, str2))


# iterate two strings in reverse order useing pointers.
# for each itgeration retrieve corresponding digits of the two strings
def add_binary(str1, str2):
  pt1 = len(str1)-1
  pt2 = len(str2)-1
  
  carry = 0
  result = []

  #loop until both of the pointer is not first digit
  while pt1 >= 0 or pt2 >= 0:
    num_str1 = 0 if pt1 < 0 else int(str1[pt1])
    num_str2 = 0 if pt2 < 0 else int(str2[pt2])
    
    #sum the retrieved digits and carry
    sum = num_str1 + num_str2 + carry
    bi_sum = bin(sum)
    carry = 0
    if sum > 1:
      carry = 1
    
    #print('sum = '+ str(sum) + ' str1 digit = ' + str1[pt1] + ' str2 digit = ' + str2[pt2] + ' pt2 = '+str(pt2))
    #print('carry = {} |sum = {} | bi_sum = {} last digit = {}'.format(carry, sum, bi_sum[2:], bi_sum[-1]))
    result.append(bi_sum[-1])
    
    pt1 -= 1
    pt2 -= 1
    
  if carry == 1:
    result.append(carry)
  result.reverse()

  '''
  to save reversed list to another list
  reversed_list = original_list[::-1]

  #example
  reversed_result = result[::-1]
  print(reversed_result)
  '''

  '''
  list contains various data type. you can't use .join() method on list if data type is not string
  you must convert it to str

  ''.join(str(element) for element in list)
  '''

  return ''.join(str(num) for num in result)
  #print(f'result = {"".join(str(e) for e in result)}') 
  
  
  
  '''
 for i in range(str1_len):
   print(str1[i])

 print('str2: '+ str2)
 for char in reversed(str2):
   print(char)
 '''
  
#test
print(add_binary('10', '11')) #"101"
print(add_binary('101', '1101')) #"10010"
print(add_binary(str1, str2)) #10110