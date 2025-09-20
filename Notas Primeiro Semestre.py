import matplotlib.pyplot as plt
def notas(texto):
    print(f'sua nota {texto} é 9 :)')
notas (texto = 'em Arquitetura de computadores')
notas (texto = 'em Banco de Dados')
notas (texto = 'em Paradigmas de Linguagens de Programação em Python')
def inseg(texto):
    print(f'sua nota {texto} é 7')
inseg (texto = 'em Introdução a segurança da Informação')
def PenCom(texto):
    print(f'sua nota {texto} é 6 :(')
PenCom (texto = 'em Pensamento Computacional')
print('Parabéns, você passou em todas as matérias, agora está de férias')

names = ['Para. Python', 'Arq. comp', 'Banc Dad', 'seg. Info',  'Pens. comp']
counts = [9, 9, 9, 7, 6]

fig, ax = plt.subplots()
bar_container = ax.bar(names, counts)
ax.set(ylabel='Notas', title='Materias', ylim=(0, 10))
ax.bar_label(bar_container, fmt='{:,.0f}')

plt.show()