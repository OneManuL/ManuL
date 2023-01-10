message = '20+1*2/2'
res = message.replace('+', '.').replace('-', '.').replace('*', '.').replace('/', '.').split('.')
res2 = [i for i in message if i in '+-/*']
while res2 != []:
    def calc(num1, num2, calcul):
        global result
        if calcul == '+':
            result = num1 + num2
        elif calcul == '-':
            result = num1 - num2
        elif calcul == '*':
            result = num1 * num2
        elif calcul == '/':
            result = num1 / num2
    if '*' in res2:
        calc(float(res[res2.index('*')]), float(res[res2.index('*')+1]), '*')
        res[res2.index('*')] = str(result)
        res.pop(res2.index('*')+1)
        res2.pop(res2.index('*'))
    elif '/' in res2:
        calc(float(res[res2.index('/')]), float(res[res2.index('/')+1]), '/')
        res[res2.index('/')] = str(result)
        res.pop(res2.index('/')+1)
        res2.pop(res2.index('/'))
    else:
        calc(float(res[0]), float(res[1]), (res2[0]))
        res.pop(0)
        res2.pop(0)
        res[0] = str(result)
print(res[0])
