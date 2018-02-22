def rot13(y):
	result= ""

	for x in y:
		z=ord(x)

		if z<=ord('z') and z>=ord('a'):
			if z> ord('m'):
				z-=13
			else:
				z +=13
		elif z<=ord('Z') and z>= ord('A'):
				if z>ord('M'):
					z-=13
				else:
					z+=13
			
		result += chr(z)
	
	return result 

keimeno=raw_input("Write something: ")
print(rot13(keimeno))