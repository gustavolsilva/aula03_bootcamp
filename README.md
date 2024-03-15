# aula03_bootcamp

## Debug do VSCode
Quando precisamos fazer a verificação de execução linha a linha para descobrirmos como o código está sendo interpretado e executado pelo computador, usamos a função do Debug <br>

## Controle de Fluxo

### If
Faz avaliação em linhe e executa os comandos que estiverem aninhado após, se e e somente se, ele for verdeira. <br>

A estrutrutura segue sempre: <br>
```
if condicao:
    <o que quer executar>
```

Lembrando que caso tenha mais de uma condição, usa-se a clausula ```elif```
```
if condicaoif:
    <o que executar se verdeiro o if>
elif condicaoelif:
    <o que executar se verdadeiro o elif>
```
Podemos ter diversos if e elif encadeados<br>
```
if condicaoif:
    <o que executar se verdeiro o if>
elif condicaoelif:
    <o que executar se verdadeiro o elif>
elif condicaoelif2:
    <o que executar se verdadeiro o elif2>
elif condicaoelif3:
    <o que executar se verdadeiro o elif3>
```
Em caso de ter uma resposta falsa na verificação condicional ```if```, colocamos ao final uma clausula ```else```
```
if condicaoif:
    <o que executar se verdeiro o if>
elif condicaoelif:
    <o que executar se verdadeiro o elif>
elif condicaoelif2:
    <o que executar se verdadeiro o elif2>
elif condicaoelif3:
    <o que executar se verdadeiro o elif3>
else:
    <executa o conteudo do else>
```

### For
Passa sob sequencias. Imagine que eu tenha uma lista e precise percorrer todos os itens dela.

```
for i in range(num1, num n)
    <acao>
```

Posso pedir para ele percorrer uma Lista (Tipo Complexo)

*Adendo: Listas, são do tipo complexo que podem ter diversos itens primitivos dentro dela.*

