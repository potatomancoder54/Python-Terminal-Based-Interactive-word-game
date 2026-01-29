import time

print('Hello player This is a Terminal Based INTERATIVE WORD GAME!')
time.sleep(1)
print('You will be given a series of clues to guess the correct word.')
time.sleep(2)
print('Let\'s begin!')
time.sleep(3)
score = 0
def ask_question(clue, answer):
    global score
    print(clue)
    user_answer = input('Your awnser: ').strip().lower()
    if user_answer == answer:
        print('Correct!\n')
        score += 1
    else:
        print(f'Wrong! The correct answer was: {answer}\n')
questions = [
    ("I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?", "echo"),
    ("I come from a mine and get surrounded by wood always. Everyone uses me. What am I?", "pencil"),
    ("I have keys but no locks. I have space but no room. You can enter, but you can’t go outside. What am I?", "keyboard"),
    ("What has to be broken before you can use it?", "egg"),]
for clue, answer in questions:
    ask_question(clue, answer)
print(f'Game over! Your final score is: {score} out of {len(questions)}')
time.sleep(4)
print('Thanks for playing!')