#!/usr/bin/env python
# coding: utf-8

# 1. In mathematics, the Fibonacci numbers, commonly denoted Fn, form a
# sequence, called the Fibonacci sequence, such that each number is the sum
# of the two preceding ones, starting from 0 and 1:
# 
# The beginning of the sequence is this:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
# The function fastFib(num) returns the fibonacci number Fn, of the given num
# as an argument.
# Examples
# fib_fast(5) ➞ 5
# fib_fast(10) ➞ 55
# fib_fast(20) ➞ 6765
# fib_fast(50) ➞ 12586269025
# 
# 
# 
# 
# 
# 
# 
# Ans:-

# In[1]:


def fib_fast_one(in_num):
    temp_list = []
    for ele in range(in_num+1):
        if ele in [0,1]:
            temp_list.append(ele)
        else:
            temp_list.append(temp_list[-1]+temp_list[-2])
    print(f'fib_fast_one({in_num}) ➞ {temp_list[-1]}')
    
# Approach 2 -> Memory Efficient
def fib_fast_two(in_num):
    back_two,back_one,output = 0,1,0
    for ele in range(in_num+1):
        if ele > 1:
            output = back_two+back_one
            back_two = back_one
            back_one = output
    print(f'fib_fast_two({in_num}) ➞ {output}')

fib_fast_one(5)
fib_fast_one(10)
fib_fast_one(20)
fib_fast_one(50)    
print() 
fib_fast_two(5)
fib_fast_two(10)
fib_fast_two(20)
fib_fast_two(50)


# 2. Create a function that takes a strings characters as ASCII and returns each
# characters hexadecimal value as a string.
# Examples
# convert_to_hex(&quot;hello world&quot;) ➞ &quot;68 65 6c 6c 6f 20 77 6f 72 6c 64&quot;
# convert_to_hex(&quot;Big Boi&quot;) ➞ &quot;42 69 67 20 42 6f 69&quot;
# convert_to_hex(&quot;Marty Poppinson&quot;) ➞ &quot;4d 61 72 74 79 20 50 6f 70 70 69 6e
# 73 6f 6e&quot;
# 
# 
# 
# 
# 
# 
# 
# Ans:-

# In[2]:


def convert_to_hex(in_string):
    out_string = []
    for ele in in_string:
        out_string.append(hex(ord(ele))[2:])
    print(f'convert_to_hex({in_string}) ➞ {" ".join(out_string)}')

convert_to_hex("hello world")
convert_to_hex("Big Boi")
convert_to_hex("Marty Poppinson")


# 3. Someone has attempted to censor my strings by replacing every vowel
# with a *, l*k* th*s. Luckily, I&#39;ve been able to find the vowels that were
# removed.
# Given a censored string and a string of the censored vowels, return the
# original uncensored string.
# Example
# uncensor(&quot;Wh*r* d*d my v*w*ls g*?&quot;, &quot;eeioeo&quot;) ➞ &quot;Where did my vowels go?&quot;
# uncensor(&quot;abcd&quot;, &quot;&quot;) ➞ &quot;abcd&quot;
# uncensor(&quot;*PP*RC*S*&quot;, &quot;UEAE&quot;) ➞ &quot;UPPERCASE&quot;
# 
# 
# 
# 
# 
# ANs:-

# In[3]:


def uncensor(in_string,in_vowels):
    window = 0
    out_string = ''
    for ele in in_string:
        if ele == '*':
            out_string += in_vowels[window]
            window +=1
        else:
            out_string += ele
    print(f'uncensor{in_string,in_vowels} ➞ {out_string}')

uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo")
uncensor("abcd", "")
uncensor("*PP*RC*S*", "UEAE") 


# 4. Write a function that takes an IP address and returns the domain name
# using PTR DNS records.
# Example
# get_domain(&quot;8.8.8.8&quot;) ➞ &quot;dns.google&quot;
# get_domain(&quot;8.8.4.4&quot;) ➞ &quot;dns.google&quot;
# 
# 
# 
# 
# 
# 
# Ans:-

# In[4]:


import socket
def get_domain(in_ip):
    print(f'get_domain({in_ip}) ➞ {socket.gethostbyaddr(in_ip)} ➞ {socket.gethostbyaddr(in_ip)[0]}')
    
get_domain("8.8.8.8")
get_domain("8.8.4.4")


# 5. Create a function that takes an integer n and returns the factorial of
# factorials. See below examples for a better understanding:
# Examples
# fact_of_fact(4) ➞ 288
# # 4! * 3! * 2! * 1! = 288
# fact_of_fact(5) ➞ 34560
# fact_of_fact(6) ➞ 24883200
# 
# 
# 
# 
# 
# Ans:-

# In[5]:


def fact_of_fact(in_num):
    # Internal Function to generate factorial of a Number
    def get_factorial(n):
        if n == 1:
            return 1
        else:
            return n*get_factorial(n-1)      
    out_num = 1
    for ele in range(1,in_num+1):
        out_num *= get_factorial(ele)
    print(f'fact_of_fact({in_num}) ➞ {out_num}')

fact_of_fact(4)
fact_of_fact(5)
fact_of_fact(6)

