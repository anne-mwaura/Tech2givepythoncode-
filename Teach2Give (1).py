
# coding: utf-8

# In[3]:

#Write a program that prints the numbers from 1 to 100. For multiples of 3, print "Fizz"; for multiples of 5, print "Buzz"; and for numbers that are multiples of both 3 and 5, print "FizzBuzz".
def FizzBuzz():
    for i in range(1, 101):
        if i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Bizz")
        elif i % 5 == 0 and i%3==0:
            print("FizzBuzz")
        else:
            print(i)


# In[4]:

FizzBuzz()


# In[5]:

#Write a program to generate the Fibonacci sequence up to 100.
k = [0, 1]
while k[-1] <= 100:
    k.append(k[-1] + k[-2])
if k[-1] > 100:
    k.pop()
print(k)


# In[6]:

#Write a program that takes an integer as input and returns true if the input is a power of two.
def murife(i):
    if i <= 0:
        return False
    while i % 2 == 0:
            i //= 2
    
    return i == 1


# In[8]:

print(murife(7))
print(murife(8))


# In[9]:

#Write a program that accepts a string as input, capitalizes the first letter of each word in the string, and then returns the result string
def wesley(name):
    return name.capitalize()

name = "i love you"
result = wesley(name)
print(result)


# In[10]:

#Write a program that takes an integer as input and returns an integer with reversed digit ordering.
def number(i):
    k=0
    while i != 0:
        digit = i % 10
        k = k * 10 + digit
        n //= 10
    return k


# In[11]:

number=254
result = int(str(number)[::-1])
print(result)


# In[12]:

#Write a program that counts the number of vowels in a sentence.
def count_vowels(sentence):
    vowels = 'aeiou'
    count = 0
    for char in sentence:
        if char in vowels:
            count += 1
    
    return count


sentence = "This is a sample sentence with some vowels."
print("Number of vowels:", count_vowels(sentence))


# In[ ]:



