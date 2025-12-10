def user_input(prompt):
    while True:
        pr = input(prompt)
        if pr.strip():
            return pr.strip()
        else:
            print('Enter a non-empty value!')

def user_input_int(prompt, minimum=None, maximum=None):
    while True:
        try:
            pr = int(input(prompt))
            if minimum is not None and pr < minimum:
                print(f'Enter a number >= {minimum}!')
                continue
            if maximum is not None and pr > maximum:
                print(f'Enter a number <= {maximum}!')
                continue
            return pr
        except ValueError:
            print('Enter a valid integer!')

quizzes = []  # list of dicts: {'question': str, 'options': [...], 'answer': int}

def create_quiz():
    q = user_input('Write the question: ')
    print('--- Give options ---')
    opts = []
    for i in range(1, 5):
        opts.append(user_input(f'opt{i}: '))
    ans = user_input_int('Real/correct answer (1-4): ', minimum=1, maximum=4)
    quizzes.append({'question': q, 'options': opts, 'answer': ans})
    print('Added successfully.\n')

def list_quizzes():
    if not quizzes:
        print('Nothing to see here.\n')
        return
    for idx, q in enumerate(quizzes, start=1):
        print(f'{idx}. {q["question"]}')
        for i, opt in enumerate(q['options'], start=1):
            print(f'   {i}) {opt}')
        print()  # blank line between questions

def update_quiz():
    if not quizzes:
        print('Nothing to update.\n')
        return
    list_quizzes()
    idx = user_input_int('Enter question number to update: ', minimum=1, maximum=len(quizzes)) - 1
    selected = quizzes[idx]
    print('What do you want to change?')
    print('0) Question')
    print('1) Option 1')
    print('2) Option 2')
    print('3) Option 3')
    print('4) Option 4')
    print('5) Correct answer number')
    choice = user_input_int('Choose 0-5: ', minimum=0, maximum=5)
    if choice == 0:
        selected['question'] = user_input('New question: ')
    elif 1 <= choice <= 4:
        newopt = user_input(f'New text for option {choice}: ')
        selected['options'][choice-1] = newopt
    else:  # choice == 5
        new_ans = user_input_int('New correct answer (1-4): ', minimum=1, maximum=4)
        selected['answer'] = new_ans
    print('Changed successfully.\n')

def play_quiz():
    if not quizzes:
        print('No quizzes to play.\n')
        return
    score = 0
    for idx, q in enumerate(quizzes, start=1):
        print(f'Q{idx}: {q["question"]}')
        for i, opt in enumerate(q['options'], start=1):
            print(f'   {i}) {opt}')
        choice = user_input_int('Choose 1-4: ', minimum=1, maximum=4)
        if choice == q['answer']:
            print('You genius! ✅\n')
            score += 1
        else:
            correct_text = q['options'][q['answer']-1]
            print(f'Better luck next time. Correct answer: {q["answer"]}) {correct_text}\n')
    print(f'Your score: {score}/{len(quizzes)}\n')

def delete_quiz():
    if not quizzes:
        print('Nothing to delete.\n')
        return
    list_quizzes()
    idx = user_input_int('Enter the question number you want to delete: ', minimum=1, maximum=len(quizzes)) - 1
    removed = quizzes.pop(idx)
    print(f'Removed question: {removed["question"]}\n')

def main_loop():
    while True:
        print('Choose Option: [c]reate  [l]ist  [p]lay  [u]pdate  [d]elete  [e]xit')
        choose = input('Here: ').strip().lower()
        if choose == 'c':
            create_quiz()
        elif choose == 'l':
            list_quizzes()
        elif choose == 'u':
            update_quiz()
        elif choose == 'p':
            play_quiz()
        elif choose == 'd':
            delete_quiz()
        elif choose == 'e':
            print('Have a nice day!')
            break
        else:
            print('Invalid input\n')

if __name__ == '__main__':
    main_loop()
