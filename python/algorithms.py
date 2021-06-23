def allCombinations(array: list, begin: int = 0, subarray: bool = False):
    temp = []
    if len(array) == 0: return []
    else:
        for i in range(begin, pow(2,len(array))):
            valueBinary = str(format(i, 'b'))
            while len(valueBinary) < len(array):
                valueBinary = ''.join(['0', valueBinary])
            if subarray: value = []
            else: value = ''
            for a in range(len(valueBinary)):
                if list(reversed(valueBinary))[a] == '1':
                    if subarray: value.append(array[a])
                    else: value += str(array[a])
            if subarray: temp.append(value)
            else: temp.append(value)
        return(temp)

##################################
# The function returns the combination of all possibilities
# The second parameter which is optional is the pitch, by default it starts at 0
# The third parameter is there for the distinction if it is a string or an array
# Tests
# print(allCombinations([0, 1, 2, 3], 1))
# -> ['0', '1', '01', '2', '02', '12', '012', '3', '03', '13', '013', '23', '023', '123', '0123']
# print(allCombinations(['a', 'b', 'c']))
# -> ['', 'a', 'b', 'ab', 'c', 'ac', 'bc', 'abc']
# print(allCombinations(['a', 'b', 'c'], 1, True))
# -> [['a'], ['b'], ['a', 'b'], ['c'], ['a', 'c'], ['b', 'c'], ['a', 'b', 'c']]
# print(allCombinations([]))
# -> []
##################################


def mathCombinations(array: list, duplicate: bool = False):
    temp = []
    if len(array) == 0: return []
    else:
        for i in range(len(array)):
            value = 1
            cpt = 0
            while cpt != len(str(array[i])):
                value *= int(str(array[i])[cpt])
                cpt += 1
            temp.append(value)
        if duplicate: return temp
        else: return sorted(list(dict.fromkeys(temp)))

##################################
# The function multiplies each number that makes up the element of a list
# The second parameter, which is optional, indicates whether we want duplicates, by default it is false
# Tests
# print(mathCombinations(['1', '2', '3','4', '5'], False))
# -> [1, 2, 3, 4, 5]
# print(mathCombinations([11, 23, 31, 41, 59], False))
# -> [1, 3, 4, 6, 45]
# print(mathCombinations(allCombinations([1, 2, 3, 4, 5], 1), False))
# -> [1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 24, 30, 40, 60, 120]
# print(mathCombinations(allCombinations([1, 2, 3, 4, 5], 1), True))
# -> [1, 2, 2, 3, 3, 6, 6, 4, 4, 8, 8, 12, 12, 24, 24, 5, 5, 10, 10, 15, 15, 30, 30, 20, 20, 40, 40, 60, 60, 120, 120]
# print(mathCombinations(allCombinations([1, 2, 3, 5, 7, 11], 1), False))
# -> [1, 2, 3, 5, 6, 7, 10, 14, 15, 21, 30, 35, 42, 70, 105, 210]
# print(mathCombinations(allCombinations([])))
# -> []
##################################


def arrangement(n: int, k: int):
    if k>n: return 0
    x = 1
    i = n-k+1
    while i<=n:
        x*=i
        i+=1
    return x

##################################
# number of arrangements
# print(arrangement(5,3))
# -> 60
##################################