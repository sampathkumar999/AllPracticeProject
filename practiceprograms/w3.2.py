def string_play(input_sentence):
    print(input_sentence)
    print(input_sentence.split())
    l = input_sentence.split()
    for i in l:
        print(i)
    for i in l:
        print('frequency of', i, '=',l.count(i))

string_play('hi my name is sampath am  learning python. learning python is very easy')
