from math import ceil

def is_palindrome(word):
    
    i = 0
    j = len(word) - 1

    while i < ceil(len(word)/2):

    	if word[i] != word[j]:

    		return False

    	i += 1
    	j -= 1

    return True


def longest_palindrome(word):

	longest = ""

	for i in range(len(word)):

		j = i

		while j < len(word):

			sub = word[i:j+1]

			if is_palindrome(sub):

				if len(sub) > len(longest):

					longest = sub

			j += 1

	return longest


print(longest_palindrome("bananas"))
print(longest_palindrome("racecar"))