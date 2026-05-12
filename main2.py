                            #listas e tuplas
# quantidade = int(input('quantos itens deseja adicionar? '))
# produtos = []
# for item in range(quantidade):
#     nome_item = input('adicione um produto a lista: ')
#     produtos.append(nome_item)
# print(produtos)
# remover = input('deseja remover um produto? ')
# if remover == 'sim':
#     remover_produto = input('qual produto deseja remover? ')
#     produtos.remove(remover_produto)
# print(produtos)

#print([input('adicione um produto a lista: ') for _ in range(int(input('quantos itens deseja adicionar? ')))])

# frutas = ('pera' , 'uva' , 'banana' , 'maça', 'melao')
# for fruta in frutas:
#     print(fruta)
# disponivel = input('digite uma fruta: ')
# if disponivel in frutas:
#     print('possui essa fruta')
# else:
#     print('nao possui essa fruta')

# print(f'a qauntidade de frutas é {len(frutas)}')

        ##ex_flex 
# playlist = []
# contador = 1
# while contador == 1:
#         acao = int(input('''
#         o que deseja fazer?
#         1- adicionar uma música na última posição
#         2- adicionar uma música e especificar sua posição
#         3- remover uma música pelo nome
#         4- remover uma música pela posição
#         5- apagar tudo
#         '''))
#         if acao == 1:
#                 adicionar = input('qual música você deseja adicionar à playlist? ')
#                 playlist.append(adicionar)
#         elif acao == 2:
#                 adicionar_ = input('qual música você deseja adicionar? ')
#                 adicionar_posicao = int(input(f'em qual posição você deseja adicionar {adicionar_}? '))
#                 playlist.insert(adicionar_posicao , adicionar_)
#         elif acao == 3:
#                 remover_nome = input('qual música você deseja remover (nome)? ')
#                 playlist.remove(remover_nome)
#         elif acao == 4: 
#                 remover_posicao = int(input('qual música você deseja remover (posição)? '))
#                 playlist.pop(remover_posicao)
#         elif acao == 5:
#                 playlit.clear()
#         print(playlist)  


# notas = []
# contador = 0
# while contador != 5:
#         nota = float(input(f'insira a {contador + 1}ª nota: '))
#         notas.append(nota)
#         contador += 1
# print(f'''
# a média das notas é {sum(notas)/5}
# a maior nota foi {max(notas)}
# a menor nota foi {min(notas)}
#  ''')


#  playlist = ['oceano , 296']
#  contador = 2
#  while contador == 1:
#          acao = int(input('''
#          o que deseja fazer?
#          1- adicionar uma música na última posição
#          2- adicionar uma música e especificar sua posição
#          3- remover uma música pelo nome
#          4- remover uma música pela posição
#          5- apagar tudo
#          '''))
#          if acao == 1:
#                  adicionar = input('qual música você deseja adicionar à playlist? ')
#                  playlist.append(adicionar)
#          elif acao == 2:
#                  adicionar_ = input('qual música você deseja adicionar? ')
#                  adicionar_posicao = int(input(f'em qual posição você deseja adicionar {adicionar_}? '))
#         #          playlist.insert(adicionar_posicao , adicionar_)
        #  elif acao == 3:
        #          remover_nome = input('qual música você deseja remover (nome)? ')
        #          playlist.remove(remover_nome)
        #  elif acao == 4: 
        #          remover_posicao = int(input('qual música você deseja remover (posição)? '))
        #          playlist.pop(remover_posicao)
        #  elif acao == 5:
        #          playlit.clear()
        #  print(playlist)  

