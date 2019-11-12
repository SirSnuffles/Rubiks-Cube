

# def orientate(orientation, alg):

# 	def orientateRight():
# 		for ind, i in enumerate(alg):
# 			if "F" in i:
# 				alg[ind] = alg[ind].replace("F", "L")
# 			if "L" in i:
# 				alg[ind] = alg[ind].replace("L", "Ba")
# 			if "Ba" in i:
# 				alg[ind] = alg[ind].replace("Ba", "R")
# 			if "R" in i:
# 				alg[ind] = alg[ind].replace("R", "F")
# 		print("New function: ")
# 		return alg
# 	def orientateLeft():
# 		for ind, i in enumerate(alg):
# 			if "F" in i:
# 				alg[ind] = alg[ind].replace("F", "R")
# 			if "L" in i:
# 				alg[ind] = alg[ind].replace("L", "Ba")
# 			if "Ba" in i:
# 				alg[ind] = alg[ind].replace("Ba", "L")
# 			if "R" in i:
# 				alg[ind] = alg[ind].replace("R", "F")
# 		print("New function: ")
# 		return alg
# 	def orientateOpposite():
# 		for ind, i in enumerate(alg):
# 			if "F" in i:
# 				alg[ind] = alg[ind].replace("F", "Ba")
# 			if "L" in i:
# 				alg[ind] = alg[ind].replace("L", "R")
# 			if "Ba" in i:
# 				alg[ind] = alg[ind].replace("Ba", "F")
# 			if "R" in i:
# 				alg[ind] = alg[ind].replace("R", "L")
# 		print("New function: ")
# 		return alg
# 	if orientation == 1: orientateRight()
# 	if orientation == 2: orientateLeft()
# 	if orientation == 3: orientateOpposite()
# 	else: return alg


# def main():
# 	for i in range(4):
# 		print(orientate(i, ["FCW", "FCCW", "LCW", "LCCW", "RCW", "RCCW", "BaCW", "BaCCW", "BCW", "BCCW", "TCW", "TCCW"]))

# if __name__ == '__main__':
# 	main()

# # alg = ['FCW', 'FCCW', 'LCW', 'LCCW', 'RCW', 'RCCW', 'BaCW', 'BaCCW', 'BCW', 'BCCW', 'TCW', 'TCCW']

# # for ind, i in enumerate(alg):
# # 	if "F" in i:
# # 		alg[ind] = "L"
# # 	if "F" in i:
# # 		alg[ind].replace("F", "L")
# # 	if "L" in i:
# # 		alg[ind].replace("L", "Ba")
# # 	if "Ba" in i:
# # 		alg[ind].replace("Ba", "R")
# # 	if "R" in i:
# # 		alg[ind].replace("R", "F")

# # alg = "FCCW"
# # print(alg)
# # alg = alg.replace("F", "L")
# # print(alg)




# list1 = [1,2,3,4,5, 5]
# list2 = [2,3,4,5,5,1]

# x = set([list1[0], list1[1]])
# y = set([list2[0], list2[-1]])
# print(x)
# print(y)
# print(x == y)



foobars = [0,0,1]
if any(x == 1 for x in foobars):
	print(True)
else:
	print(False)
# print(any() == 0)