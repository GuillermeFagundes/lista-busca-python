# Desafio de reflexão

A busca sequencial é mais adequada quando a lista é pequena, não está ordenada ou muda com frequência. Ela examina os elementos um a um e, por isso, funciona sem preparação prévia. Também pode ser a melhor escolha quando será feita apenas uma busca, pois ordenar toda a lista só para isso pode custar mais do que percorrê-la uma vez.

A busca binária apresenta vantagem em listas grandes e ordenadas, principalmente quando muitas consultas serão realizadas. A cada comparação, ela descarta aproximadamente metade da parte restante da lista. Por esse motivo, cresce muito mais devagar do que a busca sequencial conforme aumenta a quantidade de elementos.

Entretanto, a busca binária depende da ordenação. Se os dados ainda não estiverem ordenados, é preciso considerar o custo de ordená-los. Assim, para dados estáveis e muitas consultas, ordenar uma vez e usar busca binária costuma compensar; para dados pequenos, desordenados ou consultados poucas vezes, a busca sequencial tende a ser mais simples e adequada.
