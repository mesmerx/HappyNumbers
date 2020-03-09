# contexto
Para saber se um número é feliz, você deve obter o quadrado de cada dígito deste número, em seguida você faz a soma desses resultados. A seguir o mesmo procedimento deve ser feito com o valor resultante desta soma. Se ao repetir o procedimento diversas vezes obtivermos o valor 1, o número inicial é considerado feliz.

o pretexto desse código é verificar de forma eficiente o tipo do número

# algumas notas

<details>
<summary>
<font size=5><b>complexidade</b></font>
</summary>
fazer a sequencia para verificação se o número é feliz é altamente custoso, considerando k rotações de números
e considerenado o número k de ciclos com possivel recorrencia infinita
temos :

~~~
complexidade : O(kn)
~~~
para melhorar isso usarei dois approachs
~~~
*<b>hash set</b>: usando uma coleção de números já feitos para quebrar a sequencia garanto velocidade na entrega 
O(1) caso número ja tenha sido testado (acesso a memoria em python é sempre O(1)
mas na media a complexidade deve ser
o(kn)/O(knlogk)
que já é um avançdo em relação a sem o hash 
~~~
    
~~~
*<b>usando dois marcadores</b>: introduzindo dois marcadores consigo garantir que o número nãos e repete e casos e repita está em ciclo e logo não é feliz 
ou sejá reduzo o pior dos casos a um O(kn) aonde o k é um número nao infinito
 ~~~

</details>

## parametros de velocidade

terão 3 parametros para velocidade

* hash é salvo e lido em arquivo em disco, para futuros acessos
* hash é gerado na hora do 0
* hash não é usado então toda verificação é feita do 0

## considerações

* o cache pode ser otimizado, algumas melhorias possiveis: 
salvar o cache já em json, para uma ligibilidade de código
salvar o cache em um banco de dados, caso o arquivo cresca muito(talvez redis ou mongo)
* o crescimento númerico é mais rapido que o crescimento de seus quadrados, ex: 9999 = 9²+9²+9²+9²=9²*2= 324, e o 324< 9999 logo já estaria em cache sua arvore, o que significa que na segunda interação já teriamos a resposta, tornando o(1), o ponto critico aparece razoavelmente cedo, algo como ~ 55


