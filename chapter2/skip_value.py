# examples of slicing string 
myStr = 'abcdEfghijklaaaaa'
print(myStr[1:12:2])
print(myStr)
# manipulation of strings
# length of string
print(len(myStr))
# endsWidth
print(myStr.endswith('run'))
print(myStr.endswith('jkl'))
# startswith
print(myStr.startswith('abc'))
print(myStr.startswith('kl'))
# count
print(myStr.count('a'),myStr.count('b'))
# capitalize
print(myStr.capitalize())
# lower
print(myStr.lower())
# find
print(myStr.find('d'))
# replace
print(myStr.replace('d','Z'))

