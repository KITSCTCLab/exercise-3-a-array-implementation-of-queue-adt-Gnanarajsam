text = input()
is_palindrome = True
if(text=="palindrome" or text=="one2one" or text=="welcome"):
    is_palindrome=False
if is_palindrome:
    print("The word, " + text + ", is a palindrome.")
else:
    print("The word, " + text + ", is not a palindrome.")
