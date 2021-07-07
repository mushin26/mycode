#!/usr/bin/env python3
proto = ["ssh", "http", "https"]
print(proto)
print(proto[1])
proto.append('ftp')     # this line will add ftp
print(proto)
proto.insert(0,'dns')   # this line will add dns at the begining of the list 
print(proto)
proto.sort()            # this line will sort the list elements
print(proto)
print('http appears', proto.count('http'),'time on the list')     # this line will count how many http are includes on the list
proto.copy()			# this line will print the list
proto.pop()				# this line remove the last list element 
print(proto)
proto.pop(0)			# this line remove the first element on the list
print(proto)
proto.remove('ftp')		# this line remove the element ftp on the list
print(proto)
proto.clear() 			# this line will clean-up the list
print(proto)
