import re

text = "My email is student@gmail.com and my phone number is 9876543210."

# Find email
email = re.findall(r'\S+@\S+', text)

# Find phone number
phone = re.findall(r'\d{10}', text)

# Search for word
search = re.search(r'email', text)

print("Email:", email)
print("Phone:", phone)

if search:
    print("'email' found in the text")
else:
    print("'email' not found")