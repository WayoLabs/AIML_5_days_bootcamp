import re

# Sample text
text = "My email is example123@gmail.com and my backup is contact.me@yahoo.com"

# Pattern to find emails
pattern = r"[a-zA-Z0-9_.]+@[a-zA-Z]+\.(com|net|org)"
# Find all matches
emails = re.findall(pattern, text)
print("Found emails:", emails)

#corrected pattern
pattern = r"[a-zA-Z0-9_.]+@[a-zA-Z]+\.(?:com|net|org)"
emails = re.findall(pattern, text)
print("Found emails:", emails)


text2='''
Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
Tesla's CFO number (999)-333-7777
'''
pattern2 = '\(\d{3}\)-\d{3}-\d{4}|\d{10}'

matches2 = re.findall(pattern2, text2)
print("Found phone numbers:", matches2)





text = '''
The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. 
'''

pattern = 'FY\d{4} Q[1-4]'

matches = re.findall(pattern, text)
print("Found matches:", matches)


text = "Event dates: 01-04-2024, 2024/04/01, and April 1, 2024"

# Simple pattern for DD-MM-YYYY and YYYY/MM/DD
pattern = r"(\d{2}[-/]\d{2}[-/]\d{4}|\d{4}[-/]\d{2}[-/]\d{2}|[A-Z][a-z]+ \d{1,2}, \d{4})"

dates = re.findall(pattern, text)
print("Dates found:", dates)
