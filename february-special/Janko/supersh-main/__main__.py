from supersh_control import welcome, supersh_valid, globs

PROMPT = ' '
HELPFILE = 'help.txt'
var = {}  #here are stored variables

# show welcome info
welcome()


while True:
    # Load input and check its validity.
    cmd = input(PROMPT).strip()
    valid = supersh_valid(cmd, var)
    if not valid:
        print(valid)
        continue

    # If input is valid, evaluate commands or expressions
    # ↓↓↓ HERE WRITE YOUR CODE ↓↓↓
    elif cmd == '':
        continue
    
    elif cmd == '#exit':
        break
    
    elif cmd == '#help':
        with open('help.txt', 'r', encoding= 'UTF-8') as subor:
            print(subor.read())  
        

    elif cmd.startswith('#var'):
        prikaz = cmd.strip().split(' ')
        var[str(prikaz[1])] = eval(prikaz[3], globs | var)
        
    elif cmd == '#list':
        for key, item in var.items():
            print(f'{key};{item}')

    elif cmd.startswith('#save'):
        if cmd == '#save':
            with open('vars.txt','w', encoding= 'UTF') as file:
                for key, item in var.items():
                    print(f'{key};{item}', file = file)
        else:
            prikaz = cmd.strip().split(' ')
            with open(prikaz[1],'w', encoding= 'UTF') as file:
                for key, item in var.items():
                    print(f'{key};{item}', file = file)
   
    elif cmd.startswith('#load'):
        if cmd == '#load':
            with open('vars.txt','r', encoding= 'UTF') as file:
                for line in file:
                    line = line.strip().split(';')
                    var[line[0]] = eval(line[1], globs | var)
        else:
            prikaz = cmd.strip().split(' ')
            with open(prikaz[1],'r', encoding= 'UTF') as file:
                for line in file:
                    line = line.strip().split(';')
                    var[line[0]] = eval(line[1], globs | var)
    else:
        # If the input is only an expression, print value
        print(eval(cmd, globs | var))


