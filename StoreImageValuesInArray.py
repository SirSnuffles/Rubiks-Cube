from PIL import Image
import cv2
import webcolors
import os


class SaveToArray(object):
	def __init__(self, directory = "D:/Programming/RCSolver/RCSolver"):
		self.imagecount = 0
		self.directory = directory
		self.tempColour = ''
		self.arrayOfValues = [[None, None, None, None, None, None, None, None, None],		#1-9 w
							[None, None, None, None, None, None, None, None, None],			#10-18 o
							[None, None, None, None, None, None, None, None, None],			#19-27 y
							[None, None, None, None, None, None, None, None, None],			#28-36 r
							[None, None, None, None, None, None, None, None, None],			#37-45 b
							[None, None, None, None, None, None, None, None, None]]			#46-54 g
		self.loadImagesToSplit()

	def __repr__(self):
		'''returns raw value of arrayOfValues'''
		return self.arrayOfValues

	def __str__(self):
		'''prints formatted version of arrayOfValues for end user in following format'''
#                       '#' '#' '#'
#                       '#' 'b' '#'
#                       '#' '#' '#'

#   '#' '#' '#'         '#' '#' '#'         '#' '#' '#'
#   '#' 'w' '#'         '#' 'g' '#'         '#' 'y' '#'
#   '#' '#' '#'         '#' '#' '#'         '#' '#' '#'

#                       '#' '#' '#'
#                       '#' 'o' '#'
#                       '#' '#' '#'

#                       '#' '#' '#'
#                       '#' 'r' '#'
#                       '#' '#' '#'
		print()

	def saveToArray(self, colour, position):
		if 1 <= position <= 9:
			self.arrayOfValues[0][position - 1] = colour
		elif 10 <= position <= 18:
			self.arrayOfValues[1][(position%9) - 1] = colour
		elif 19 <= position <= 27:
			self.arrayOfValues[2][(position)%9 - 1] = colour
		elif 28 <= position <= 36:
			self.arrayOfValues[3][(position)%9 - 1] = colour
		elif 37 <= position <= 45:
			self.arrayOfValues[4][(position)%9 - 1] = colour
		elif 46 <= position <= 54:
			self.arrayOfValues[5][(position)%9 - 1] = colour
		else:
			print("Error!: could not assign position to array!")

	def loadImagesToSplit(self):
		for filename in os.listdir(self.directory):
			if filename.endswith(".jpg"):
				for singleImageColour in self.splitImage(filename):
					self.imagecount += 1
					self.saveToArray(self.tempColour, self.imagecount)
					# print(self.tempColour)
					# print(self.imagecount)

	def splitImage(self, input_image):
		for x in range(3):
			for y in range(3):
				yield self.getImage(input_image, y*240,x*240,240,240)

	def getImage(self, input_image, start_x = 0, start_y = 0, width = 720, height = 720):
		input_img = Image.open(input_image)
		box = (start_x, start_y, start_x + width, start_y + height)
		output_img = input_img.crop(box)
		self.get_dominate_RGB_color(output_img)

	def get_colour_name(self, rgb_triplet):
	    min_colours = {}
	    for key, name in webcolors.css21_hex_to_names.items():
	        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
	        rd = (r_c - rgb_triplet[0]) ** 2
	        gd = (g_c - rgb_triplet[1]) ** 2
	        bd = (b_c - rgb_triplet[2]) ** 2
	        min_colours[(rd + gd + bd)] = name
	    return min_colours[min(min_colours.keys())]

	def get_dominate_RGB_color(self, file):
		img = file
		colors = img.getcolors(2000000) #put a higher value if there are many colors in your image
		max_occurence, most_present = 0, 0
		try:
			for c in colors:
				if (c[1][0] + c[1][1] + c[1][2]) > 150:
					if c[0] > max_occurence:
						(max_occurence, most_present) = c
			self.tempColour = self.get_colour_name(most_present)
			# print(self.get_colour_name(most_present))
		except TypeError:
			raise Exception("Too many colors in the image")

	def returnArray(self):
		return self.arrayOfValues


def main():
	newObj = SaveToArray()
	print(newObj.returnArray())


if __name__ == '__main__':
	main()