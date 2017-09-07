# tuple_maker = lambda p, q : (p,q)
# tuple_addition = lambda p,q : (p[0]+q[0] , p[1]+q[1])
# tuple_multiply_by = lambda p, q : (p[0]*q, p[1]*q)

from fractions import Fraction

def radius_generator(probable_radius, all_diffrences, number_of_pegs):
    radiuses=[probable_radius]
    for i in range(number_of_pegs-1):
        next_radius = all_diffrences[i] - radiuses[-1]
        if next_radius <= 1:
            return False
        radiuses.append(next_radius)
    return radiuses


def answer(pegs):
    print("-------------------------------------------------------------------------------------")
    print(pegs)
    number_of_pegs = len(pegs)
    l_diff = [pegs[i+1] - pegs[i] for i in range(number_of_pegs-1)]
    # print(l_diff)
    flag = True
    if number_of_pegs < 2:
        return [-1,-1]
    elif number_of_pegs == 2 and l_diff[0] >1:
        result = Fraction(l_diff[0]*2, 3)
        flag = False
        return [result.numerator, result.denominator]
    else:
        # final_tuple = (Fraction(-1,2), l_diff[-1])
        if number_of_pegs%2 == 0:
            multiplicand = Fraction(3,2)
        else:
            multiplicand = Fraction(-1,2)
        go_till = len(l_diff)
        # print(go_till)
        result = 0
        for i in range(go_till-1):
            result = l_diff[i]-result
        final_result = l_diff[-1] - result
        final_result = Fraction(final_result, multiplicand)
        radius = radius_generator(final_result, l_diff, number_of_pegs)
        if final_result < 1:
            return [-1, -1]
        elif not radius:
            return [-1, -1]
        elif final_result >1 and radius:
            return [final_result.numerator, final_result.denominator]
    if flag:
        return [-1,-1]


print(answer([352, 1151, 2352, 2888, 3742, 5712, 7542, 8380, 8470, 9222, 9897]))
print(answer([352, 2352, 3742, 5712, 7542, 8380, 8470, 9222]))
print(answer([100, 320, 500, 670]))
print(answer([10, 32, 50, 68, 85, 101]))
print(answer([15, 37, 55, 73, 90, 102]))
print(answer([4, 30, 50]))
print(answer([12, 19, 22]))
print(answer([1, 2]))
print(answer([4, 17, 50]))
print(answer([1, 76]))
print(answer([1, 76, 126]))
print(answer([1, 98]))
print(answer([90, 100, 111, 119]))
