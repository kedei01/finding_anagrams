# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True
def find_anagrams(string1, string2):
    if sorted(string1) == sorted(string2):
        print("True")
    else:
        print("False")


string1 = "EARTH"
string2 = "HEART"
print("String value1 : ", string1)
print("String value2 : ", string2)
find_anagrams(string1, string2)
