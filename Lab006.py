# program to find max no in two nos

print(max(10,23))
print(max(10,23,45))
print(max(10,23,45,-1,-2,100,1,87.34))  # * args = unlimited no of arguments

#TypeError: '>' not supported between instances of 'str' and 'int'
print(max(10,23,45,-1,-2,100,1,87.34,"Asmita"))