def maximizar_troca_de_figurinhas(figurinhas_da_maria, figurinhas_do_joao):
  
    controle = 0
    quantidade = 0

    if len(figurinhas_da_maria) < len(figurinhas_do_joao):  
        for i in range(len(figurinhas_da_maria)):
            for j in range(len(figurinhas_do_joao)):
                if figurinhas_da_maria[i] == figurinhas_do_joao[j]:
                    controle += 1
        quantidade = len(figurinhas_da_maria) - controle


    elif len(figurinhas_do_joao) < len(figurinhas_da_maria):
        for i in range(len(figurinhas_do_joao)):
            for j in range(len(figurinhas_da_maria)):
                if figurinhas_do_joao[i] == figurinhas_da_maria[j]:
                    controle += 1
        quantidade = len(figurinhas_do_joao) - controle

                                                              
    else:
        for i in range(len(figurinhas_da_maria)):
            for j in range(len(figurinhas_do_joao)):
                if figurinhas_da_maria[i] == figurinhas_do_joao[j]:
                    controle += 1
        quantidade = len(figurinhas_da_maria) - controle

    return quantidade
    



if __name__ == '__main__':
    A, B = input().split(' ')
    figurinhas_da_maria = input().split(' ')
    figurinhas_da_joao = input().split(' ')
    print(maximizar_troca_de_figurinhas(figurinhas_da_maria, figurinhas_da_joao))

