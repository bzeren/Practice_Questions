##Q1: List the strings that are anagrams from a set of strings (ayni harflerden olusan farkli kelime) 
##Q2: Find the longest palindrome of a string (tersten okundugunda ayni olan kelime)


def isWord(s):
#    print "isWord("+s+")"
    words = ["sword", "word", "words" , "board", "door", "key", "keyboard"] #sorted for convenience
    return True if s in words else False
    

global ans
ans = set()

"""
Generates a set of anagrams given a set of words and stores them in ans
"""
def generateAnagrams(_set):
    allLetters = []
    for word in _set:
        allLetters.extend([w for w in word]) #convert word to array of characters and store them
    
    anagrams = generateAnagramsStrArr(allLetters)

"""
Input: Array of characters representing the string to find anagrams of
Return: Set of strings of anagrams
O(n!)
"""
def generateAnagramsStrArr(sarr):
    # Terminating conditions:
    if len(sarr) == 1:
        return [''.join(sarr)]
    elif len(sarr) == 2:
        return [''.join(sarr), ''.join(sarr[::-1] )] 
    
    else:
        s = ''.join(sarr)
        answer = [s]
        if isWord(s):
            ans.add(s)
        
        for characterIndex in range(len(sarr)):
            c = sarr[characterIndex]#.pop()
            s_short = sarr[:characterIndex] + sarr[characterIndex+1:] #sarr without one char
            
            words = generateAnagramsStrArr(s_short) #recursively operate on smaller array
            for word in words:
                for i in range(len(word)+1): 
                  x = ''.join(word[:i] + c + word[i:]) #string new word
                  #print 'x', x
                  if isWord(x): #found an anagram
                     ans.add(x) # add it to answer list
                  answer.append(x) # save all words for higher recursive operation
                 
                  if isWord(''.join(word)): #the word by itself was not checked at any other point in the computation
                      ans.add(word) 
                  answer.append(word) #save all words s
        return answer 


"""
Finds the longest palindrome in a string
O(n^3) implementation
"""
def longestPalindrome(s): ## additional spec: one word or full strings?
  s = s.lower() #convert to lowercase
  longest = '' #will hold longest palindrome as they are found
  
  end = 1
  while end < len(s):  # increase ending index at each iteration
      for beg in range(end): # check every different-length substring up to the end
          substr = s[beg:end+1]
          if len(substr) > len(longest) and isPalindrome(substr): #new longest palindrome
              longest = substr #save longest
      end+=1
              
  return longest
          
"""
Checks if a string is a palindrome.
O(n/2) implementation
"""
def isPalindrome(s): 
    s = s.lower() #convert to lower case
    if len(s) == 1:
        return True #single-length strings are palindromes by definition
        
    i = 0 #init counter
    while i <= len(s) / 2:
        if s[i] != s[-(i+1)]:  #check characters on either side for inequality
            return False
        i+= 1
    return True

def isPalindromeOneLine(s):
    return s.lower() == s.lower()[::-1]
          

######### TESTS ########
pals = ["hannah", "HANNAH", "HaNnah", "racecar", "RACEcar", "2112", "deified", "peeweep", "revIver", "rotatoR"]
pals_expected = [s.lower() for s in pals]

nonpals = ["qwerty", "hanna", "racetrack", "revivers", "rotators", "RotaToRS", "annaHANNAHannab", 'banna-hannahb	']
nonpals_expected = ['', 'anna', '', 'reviver', 'rotator', 'rotator', 'annahannahanna', 'hannah']

## Test isPalindrome():
def isPalindromeTest():
    for pal in pals:
        assert isPalindrome(pal), "Incorrect -- %r is NOT a palindrome!" % (pal)
        assert isPalindromeOneLine(pal), "Incorrect -- %r is NOT a palindrome!" % (pal)
    
    for nonpal in nonpals:
        assert isPalindrome(nonpal) == False, "Incorrect -- %r actually is a palindrome." % (nonpal)
        assert isPalindromeOneLine(nonpal) == False, "Incorrect -- %r actually is a palindrome." % (nonpal)
    
    print "All tests passed for isPalindrome()"


## Test longestPalindrome():
def longestPalindromeTest():
    for i in range(len(pals)):
        assert longestPalindrome(pals[i]) == pals_expected[i], "Incorrect -- expected %r but got %r" % (expected[i], longestPalindrome(pals[i]))
    
    for i in range(len(nonpals)):
        assert longestPalindrome(nonpals[i]) == nonpals_expected[i], "Incorrect -- expected %r but got %r" % (nonpals_expected[i], longestPalindrome(nonpals[i]))   
    print "All tests passed for longestPalindrome()"


isPalindromeTest()
longestPalindromeTest()


wo = set(["owrosd"])
generateAnagrams(wo)
print ans
