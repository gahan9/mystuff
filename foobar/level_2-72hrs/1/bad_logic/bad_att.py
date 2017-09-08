from __future__ import division

def answer(pegs):
	number_of_pegs = len(pegs)
	# list of differences 
	l_diff = [pegs[i+1] - pegs[i] for i in range(number_of_pegs-1)]
	print(l_diff)
	for first_probable_radius in range(l_diff[0], 1, -1):
		if not first_probable_radius > 1:
			return [-1, -1]
		radius_generated = {}
		print(first_probable_radius)
		for part_int in range(1, first_probable_radius*first_probable_radius):
			probable_radius = first_probable_radius/part_int
			match_list = [int(probable_radius), int(part_int)]
			if int(probable_radius) <= 0:
				continue
			for j in range(0, number_of_pegs-1, 2):
				if j == 0:
					radius_generated[j] = probable_radius
					if not radius_generated[j] > 0:
						continue
				else:
					# print(l_diff, "\t : radius_generated : ", radius_generated,"\t : ", j)
					if not j-1 in radius_generated.keys():
						continue
					radius_generated[j] = l_diff[j-1]-radius_generated[j-1]
					if not radius_generated[j] > 0:
						continue
				radius_generated[j+1] = l_diff[j]-radius_generated[j]
				if not radius_generated[j+1] > 0:
					continue
			last_radius = radius_generated[0]/2
			if int(last_radius) == last_radius:
				radius_generated[number_of_pegs-1] = int(last_radius)
			else:
				# print(match_list, probable_radius)
				continue
			# print(radius_generated)
			# print(number_of_pegs)
			# print(radius_generated[number_of_pegs-1])
			if number_of_pegs-2 in radius_generated.keys() and number_of_pegs-1 in radius_generated.keys():
				# print(radius_generated[number_of_pegs-2])
				if radius_generated[number_of_pegs-1] + radius_generated[number_of_pegs-2] == l_diff[-1]:
					# print(radius_generated)
					# print(probable_radius, pr)
					if int(probable_radius) % int(part_int) == 0:
						return [int(probable_radius), 1]
					else:
						return match_list
				elif first_probable_radius==2:
					return [-1,-1]
			else:
				if first_probable_radius==2:
					return [-1, -1]
				else:
					continue



# print(answer([352, 1151, 2352, 2888, 3742, 5712, 7542, 8380, 8470, 9222, 9897]))
# print(answer([352, 2352, 3742, 5712, 7542, 8380, 8470, 9222]))
# print(answer([100, 320, 500, 670]))
# print(answer([10, 32, 50, 68, 85, 101]))
# print(answer([15, 37, 55, 73, 90, 102]))
# print(answer([4, 30, 50]))
# print(answer([1, 2]))
# print(answer([4, 17, 50]))
print(answer([1, 3]))
