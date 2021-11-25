from typing import List
# notes:
# type contract of element_array: List[object:]
# type contract of sub_arrays within elem_array: List[str]

# terminology/keywords
# sub_arrays = 'proto songs' -> 'song' (when complete), strs = 'verses', outermost array = 'pool'

# things we need code to do:
# overarching array
element_array: List = []

def text_input(user_input: str) -> None:
    '''take user text input, store it as an element of an array'''
    element_array.append(user_input)
# (^ what will eventually be depicted graphically)

# user can combine elements of this array into a sub-array containing those two elements
def combine_strings(str1pos: int, str2pos: int) -> None:
    '''inst.s an array, appends string 1, followed by string 2'''
    sub_array = []
    # to make sure str2pos refer to the same string after removing str1
    sub_array.append(element_array.pop(str1pos))

    if str1pos < str2pos:
        str2pos -= 1
    sub_array.append(element_array.pop(str2pos))

    element_array.insert(str1pos, sub_array)

def combine_array_string(arraypos: int, stringpos: int, insertpos: int) -> None:
    '''if one of them is already an array, have to specify order of where it goes in the array'''
    work_arr: List = element_array[arraypos]
    
    work_arr.insert(insertpos, element_array.pop(stringpos))
    
    if stringpos < arraypos:
        arraypos -= 1
    element_array.pop(arraypos)
    element_array.insert(arraypos, work_arr)


def combine_array_array(array1pos: int, array2pos: int, insertpos: int) -> None:
    '''if both are arrays, specify location of insertion, and combine into one array'''
    work_arr: List = element_array[array1pos]
    # if adding second array to end of first, use append method
    output_arr: List = []
    if insertpos == len(element_array):
        work_arr.extend(element_array[array2pos])
        output_arr = work_arr
    # if inserting second array anywhere else
    else:
        output_arr.extend(work_arr[0: insertpos])
        output_arr.extend(element_array[array2pos])
        output_arr.extend(work_arr[insertpos:])
    
    # removing original arrays from list of elements
    element_array.pop(array1pos)
    if array1pos < array2pos:
        array2pos -= 1
    element_array.pop(array2pos)
    
    # output array contains final array, combination of array 1 and 2 regardless of insert position
    element_array.insert(array1pos, output_arr)

def arr_export(arraypos: int) -> str:
    '''convert a sub-array into a string of text, and output
    for each element in the subarray, accumulate string val, append newline char'''
    output_str: str = ""
    lst: List = element_array[arraypos]
    for elem in lst:
        output_str += elem + "\n"
    
    return output_str


if __name__ == '__main__':
    # ===tests====

    #stores input str in array,
    # prints first and only elem of test array
    songlyrictest = "hey this a song lyric doo doo doo"
    text_input(songlyrictest)
    print(element_array[0])
    print()

    # combines two verses into a proto-song, print values of test array
    element_array = ['scooby dooby dooby doo', 'where are you', 'we\'ve got a mystery to solve']
    combine_strings(0,1)
    print(element_array[0], element_array[1])
    print()

    # add a verse to proto-song, given insert location, prints test array
    element_array = [['roses are red','violets are blue'], 'i like leather shoes', 'i am not dead']
    combine_array_string(0,2,2)
    print(element_array[0], element_array[1])
    print()

    # combines two proto songs into one proto song (ie, one set of brackets), prints resulting prtosong.
    element_array = [['roses are red','i like leather shoes'], ['violets are blue', 'i am not dead']]
    combine_array_array(0,1,1)
    print(element_array[0])
    print()

    # given position of a song in the pool
    print(arr_export(0))

    # TODO:
    # when a verse is added to a proto song, it can't be rearranged