#step 25: Character Counter => count different character types

'''print('='*50)
print('character counter'.upper().center(50))
print('='*50)


text= input('Enter text to analyze: ')

# Initialize counters
letters = 0
digits = 0
spaces = 0
others = 0

#count each type
for char in text:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1
    elif char == ' ':
        spaces += 1
    else:
        others += 1


#display results
print('='*50)
print('analysis results'.upper().center(50))
print('='*50)
print(f'Total character : {len(text)}')
print(f'letters: {letters}')
print(f'Digits : {digits}')
print(f'spaces : {spaces}')
print(f'Others : {others}')
print('-'*50)'''


#step 26: Vowel counter with details => count vowels and show which ones
print('='*50)
print('vowel counter'.upper().center(50))
print('='*50)
print()

text = input('Enter text: ')

a_count = 0
e_count = 0
i_count = 0
o_count = 0
u_count = 0
total_count = 0

for char in text:
    if char == 'a':
        a_count += 1
        total_count += 1
    elif char == 'i':
        i_count += 1
        total_count += 1
    elif char == 'e':
        e_count += 1
        total_count +=1
    elif char == 'o':
        o_count += 1
        total_count +=1
    elif char == 'u':
        u_count +=1
        total_count +=1


#Display results
print()
print('='*50)
print('vowel breakdown'.upper().center(50))
print('='*50)

print(f'A: {a_count}')
print(f'U: {u_count}')
print(f'I: {i_count}')
print(f'O: {o_count}')
print(f'E: {e_count}')
print('-'*50)
print(f'Total count : {total_count}')
print(f'Total consonants: {sum([1 for c in text if c.isalpha()]) - total_count}')
print('='*50)



