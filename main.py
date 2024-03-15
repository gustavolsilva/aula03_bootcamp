# %%
print("esse e o primeiro comando")

print("esse e o segundo comando")

print("esse e o terceiro comando")

#%%

#x = int(input("Please, enter an integer: "))
x = 2
if x < 0:
    x = 0
    print("Negative changed to zero")
elif x == 0:
    print("Zero")
elif x == 1:
    print("Single")
else:
    print("More")

# %%
    
#x = int(input("Please, enter an integer: "))
x = -3

if x <= 0:
    print("it is less than zero")
elif x <= 2:
    print("it is lass than dois")
else:
    print("More")

#%%
    
for i in range(2,6):
    print(i)

#%%
lista_de_alunos = ["Rafael", "Fabio", "Luciano"]

for aluno in lista_de_alunos:
    print(aluno)