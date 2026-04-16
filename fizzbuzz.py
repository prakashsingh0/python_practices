
# for i in range (1,21):
#     if i == 5 or i == 16:
#         print("fuzzbuzz")
#     elif i%2:
#         print('fizz is Odd : {}'.format(i))
#     else:
#         print('fizz is even : {}'.format(i))

# for i in range(1,21):
#     if i == 4 or i == 16:
#         print('fuzzbuzz')
#     elif i%2 ==0:
#         print(f'fuzz is even : {i}')
#     else:
#          print(f'fuzz is Odd : {i}')


banned_words = ["damn","crap","shit", "hell","china"]

while True:
    user_input = input("Please enter some text (q to quit): ")
    
    if user_input.lower() == 'q' or user_input.lower() == 'quit':
        break

    filtered = user_input
    for word in banned_words:
        stars = "*" * len(word)
        filtered = filtered.lower().replace(word, stars)

    print(filtered)