#!/usr/bin/env python3
user_input1 = input("Please enter the vendor name associate with the device:")
user_input2 = input("Please enter the purchase date:")
user_input3 = input("Please enter an IPv4 IP address:")

## the line below creates a single string that is passed to print()
# print("You told me the IPv4 address is:" + user_input)

## print() can be given a series of objects separated by a comma
print("You told me the vendor name is: ", user_input1, "\nYou told me the purchase date is: ", user_input2, "\nYou told me the IPv4 address is: ", user_input3)


