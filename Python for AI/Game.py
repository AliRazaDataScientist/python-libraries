questions = [
    'Who is the Founder of Pakistan?',
    'What is the Birthday of Pakistan?',
    'Who see the dream for Pakistan?',
    'Who is the first Governor General of Pakistan?',
    'Who is the first Prime Minister of Pakistan?'
]

options = [
    ['a: Allama Iqbal', 'b: Quaid-e-Azam Mohammad Ali Jinnah', 'c: Liaquat Ali Khan', 'd: Sir Syed Ahmed Khan'],
    ['a: 25th December 1876', 'b: 15th August 1947', 'c: 23rd March 1940', 'd: 14th August 1947'],
    ['a: Quaid-e-Azam Mohammad Ali Jinnah', 'b: Sir Syed Ahmed Khan', 'c: Allama Iqbal', 'd: Liaquat Ali Khan'],
    ['a: Quaid-e-Azam Mohammad Ali Jinnah', 'b: Allama Iqbal', 'c: Liaquat Ali Khan', 'd: Khawaja Nazimuddin'],
    ['a: Khawaja Nazimuddin', 'b: Liaquat Ali Khan', 'c: Ghulam Muhammad', 'd: Muhammad Ali Bogra']
]

number = 0
ans_list = []
for quest in questions:
    print(quest)
    liststore = options[number]
    for opt in liststore:
        print(opt)
    number = number + 1
    x = input('Enter your answer: ')
    print(type(x))
    if x not in ['a','b','c','d']:
        x = input('Enter the valid answer: ')
    ans_list.append(x)
# ans_list = ['a','c','c','b','b']
answerkey = ['b','d','c','a','b']
ans_num = 0
points = 0
for ans in ans_list:
    if(ans == answerkey[ans_num]):
        points = points + 20
    ans_num = ans_num + 1
print('You got',points,'points.')
print('The answer list is: ',ans_list)