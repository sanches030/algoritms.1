s1 = 'backwood'
def is_palindrome(s1):
    if s1.lower() == s1[::-1].lower():
        return True
    return False

palindrome = is_palindrome(s1)
print(palindrome)