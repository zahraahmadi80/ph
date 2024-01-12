char = input("Enter a character : ")[0]

if char in "AaEeIiOoUu":
    print("{} is vowel word".format(char))
elif (char >= "A" and char <= "Z") or (char >= "a" and char <= "z"):
    print("{} is consonant word".format(char))
elif char >= "0" and char <= "9":
    print("{} is digit".format(char))
else:
    print("{} is other characters".format(char))