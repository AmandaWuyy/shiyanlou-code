import random

NUM_DIGITS = 3
MAX_GUESS = 10

def getSecretNum():
    # 返回一个由 NUM_DIGITS 个不重复随机数组成的字符串
    numbers = list(range(10))
    random.shuffle(numbers)    # 随机修改列表元素的顺序。这个函数没有返回值，而是把传递给它的列表“就地”修改。
    # 列表的前 NUM_DIGITS 个数字组成的一个字符串
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    # 返回一个由 Pico, Fermi 和 Bagels 组成的，用来提示用户的字符串
    if guess == secretNum:
        return 'You got it!'
    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'
    clues.sort()
    return ' '.join(clues)    # join()将字符串的列表连接起来，作为一个单个的字符串返回
                              # 调用该方法的字符串（' '，这是一个空格字符串' '）会出现在列表中每个字符串之间（即作为分隔符）。
                              # 返回的字符串，是把 clue 中的各个字符串组合到一起，每个字符串之间会有一个空格。

def isOnlyDigits(num):
    # 如果字符串只包含数字，返回真。否则返回假
    if num == '':
        return False
    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False
    return True

print('I am thinking of a %s-digit number. Try to guess what it is.' % (NUM_DIGITS))    # 字符串插值对于任意的数据类型都有效，而不仅仅是对字符串有效。所有值都会自动转换为字符串数据类型。
print('The clues I give are...')
print('When I say:    That means:')
print('  Bagels       None of the digits is correct.')
print('  Pico         One digit is correct but in the wrong position.')
print('  Fermi        One digit is correct and in the right position.')

while True:
    secretNum = getSecretNum()
    print('I have thought up a number. You have %s guesses to get it.' % (MAX_GUESS))
    guessesTaken = 1
    while guessesTaken <= MAX_GUESS:
        guess = ''
        # while 循环条件在第一次判断时为False，从而确保执行可以进入到从 while 开始的循环中
        while  len(guess) != NUM_DIGITS or not isOnlyDigits(guess):
            print('Guess #%s: ' % (guessesTaken))
            guess = input()
        print(getClues(guess, secretNum))
        guessesTaken += 1
        if guess == secretNum:
            break    # 嵌套循环，break只是暂停最内部的循环，而不会对最外部循环产生任何影响
        if guessesTaken > MAX_GUESS:
            print('You ran out of guesses. The answer was %s.' % (secretNum))
        print('Do you want to play again? (yes or no)')
        if not  input().lower().startswith('y'):
            break