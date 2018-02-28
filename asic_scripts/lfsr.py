import sys
sys.setrecursionlimit(10**8)
from sys import argv
import copy
#Parameter Set
#USB3 Gen2 Scrambler LFSR Configuration
poly_num = "210124" #Polynomial Number = x^23 + x^21 + x^16 + x^8 + x^5 + x^2 + 1
stage = 23 #LFSR Stage Number
adv_cnt = 8 #LFSR Advance Total Number
lfsr_list = [] #store the LFSR value
pop_list = [] #store the poped value from the LFSR,used to xor with input data

#fo = open("lfsr.txt","w+")
poly_v = bin(int(poly_num,16))
poly_v = poly_v[2:]
adv_list = []
sublist = []
s = ""
loop_num = 0
#1. initial value
for num in range(0,stage):
	s="d"+str(num)
	sublist = [s]
	lfsr_list.append(copy.copy(sublist))
	#print("initial lfsr_list" + str(lfsr_list))
	adv_list.append(copy.copy([]))
#2. advance loop
'''
in each loop, we do such steps 
a. shift the current LFSR value "lfsr_list"
b. pop the MSB of "lfsr_list" and get the "lfsr_msb" value
c. add "lfsr_msb" to "pop_list" which is used to do xor operation with input data
d. feedback "lfsr_msb" to new "lfsr_list" based on poly_num 
'''
def feedback_lfsr(lfsr_list,msb,poly):
	
	#poly_v = '{:0>23}'.format(poly)
	#print(len(poly))
	for cnt in range(0,len(poly)):
		if(poly[-1-cnt] == "1"):
			sublist = lfsr_list[cnt]
			for msb_ele in msb:
				msb_cnt = sublist.count(msb_ele)	
				if(msb_cnt == 0):
					sublist.append(msb_ele)
				else:
					sublist.remove(msb_ele)
			#lfsr_list[cnt] = sublist
	#print(poly_v)
	
def p_list(l):
	print("[",end="")
	for i in range(0,len(l)):
		each_ele = l[i]
		if(i != 0):
			print(",",end="")
		if isinstance(each_ele,list):
			p_list(each_ele)
		else:
			print(str(each_ele),end="")
	print("]",end="")	

def print_list(l,prefix):
	for num in range(0,len(l)):
		print(prefix + str(num) + ": ",end="")
		p_list(l[num])
		print("")

for loop_num in range(0,adv_cnt):
	print("Current Loop: " + str(loop_num))
	lfsr_msb = lfsr_list[-1]
	#a
	lfsr_list.insert(0,lfsr_msb)
	lfsr_list.pop()
	#c
	pop_list.append(lfsr_msb)
	#d
	feedback_lfsr(lfsr_list,lfsr_msb,poly_v)
	#add each loop LFSR value into adv_list
	
	for i in range(0,len(lfsr_list)):
		adv_list[i].append(copy.copy(lfsr_list[i]))
		
print("--------------------------")
print("LFSR value is :")
print_list(lfsr_list,"D");
print("--------------------------")
print("POP lfsr_list value is :")
print_list(pop_list,"P");
print("--------------------------")
print("ADV lfsr_list value is :")
print_list(adv_list,"D")
#fo.close()