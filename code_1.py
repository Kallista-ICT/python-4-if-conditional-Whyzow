user_input = int(input("Please the year you were born: "))

if 1928 <= user_input <= 1945:       #1928-1945: Silent Gen
    Category = "Silent Gen"
elif 1946 <= user_input <= 1964:     #1946-1964: Baby boomer
    Category = "Baby boomer"
elif 1965 <= user_input <= 1980:     #1965-1980: Gen X
    Category = "Generation X"
elif 1981 <= user_input <= 1996:     #1981-1996: Millennials
    Category = "Millennials"
elif 1997 <= user_input <= 2012:     #1997-2012: Gen Z
   Category = "Generation Z"
elif 2013 <= user_input >= 2013:     #2013-present: Gen Alpha
   Category = "Generation Alpha" 

print(f"You are a: {Category}")