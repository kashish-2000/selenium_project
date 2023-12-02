str= "welcome to applogic kashish gupta"
char_frequency ={}
for char in str:
    char_frequency[char]= char_frequency.get(char,0)+1
for char,frequency in char_frequency.items():
    print(f"Charcater'{char}'occurs {frequency} items")