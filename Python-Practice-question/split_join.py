# Taking input from the user
text = input("Enter the String : ")

#Splitting the string into a list of words
words = text.split()

#Joining the words back into a string  with spaces
joined_text = " ".join(words)

print("split words : ", words)
print("joined words : ",joined_text)