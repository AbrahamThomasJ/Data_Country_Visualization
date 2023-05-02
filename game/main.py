import random



def choose_options():
    options = ('piedra', 'papel', 'tijera')

    user_option = input('piedra, papel o tijera => ')
    user_option = user_option.lower()


    if not user_option in options:
      print('esa opcion no es valida')
      return None,None

    computer_option = random.choice(options)

    print('User option =>', user_option)
    print('Computer option =>', computer_option)
    return user_option, computer_option


def user_vs_computer(user_option,computer_option):
    u_w = 0
    c_w = 0
    
    if user_option == computer_option:
        print('Empate!')
        return 0,0
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('piedra gana a tijera')
            print('user gano!')
            u_w += 1
            return u_w,c_w

        else:
            print('Papel gana a piedra')
            print('computer gano!')
            c_w += 1
            return u_w,c_w

    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('papel gana a piedra')
            print('user gano')
            u_w += 1
            return u_w,c_w

        else:
            print('tijera gana a papel')
            print('computer gano!')
            c_w += 1
            return u_w,c_w

    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('tijera gana a papel')
            print('user gano!')
            u_w += 1
            return u_w,c_w
            
        else:
            print('piedra gana a tijera')
            print('computer gano!')
            c_w += 1
            return u_w,c_w

    

def ppt_game():
     

    computer_wins = 0
    user_wins = 0

    rounds = 1
    while True:

        print('*' * 10)
        print('ROUND', rounds)
        print('*' * 10)

        print('computer_wins', computer_wins)
        print('user_wins', user_wins)

        user_option, computer_option = choose_options()
        rounds += 1
        if user_option == 0:
            continue

        u_w,c_w = user_vs_computer(user_option,computer_option)
        if user_option == None: continue

        computer_wins += c_w
        user_wins += u_w

        if computer_wins == 2:
            print('El ganador es la computadora')
            break
        if user_wins == 2:
            print('El ganador es el usuario') 
            break
        
        

    
ppt_game()