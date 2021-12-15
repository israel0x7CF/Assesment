# Programming questions
def recursive_function_reverse(list, starting_elt, ending_elt):

    if starting_elt == ending_elt:
        return list
    else:
        temp = list[starting_elt]
        list[starting_elt] = list[ending_elt]
        list[ending_elt] = temp
        ending_elt -= 1
        starting_elt += 1
        recursive_function_reverse(list, starting_elt, ending_elt)


def GCD(number_1, number_2):
    i = 1
    temp = 0
    Gcd_list = []
    if number_1 > number_2:
        temp = number_1
        number_1 = number_2
        number_2 = temp
    while(i <= number_1):
        if((number_1 % i == 0) and (number_2 % i == 0)):
            Gcd_list.append(i)
        i += 1
    return Gcd_list


# number_1 = int(input('enter a number'))
# number_2 = int(input('enter antoher number'))
# temp = GCD(number_1, number_2)
# print('list of GCD', temp)
