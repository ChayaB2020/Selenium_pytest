#program to check if a string is palindrome. if its palindrome return -1 
# else try to remove a char and check is it possible to make it palindrome, 
# if palindrome is possible return the index of the character removed, if not possible return -1
def check_palindrome(s):#aab
    for i in range(int(len(s)/2)):
        for ind,ele in enumerate(s):
            if ele==s[-1-ind]:
                continue
            else:
                return False
    return True

a=input("mention the string : ")
if check_palindrome(a):
    print(-1)
else: 
    for i,val in enumerate(a):
        new_a=a[:i]+a[i+1:]
        print('new_a: '+new_a)
        if check_palindrome(new_a):
            print(i)
            break
    else:
        print('-1')