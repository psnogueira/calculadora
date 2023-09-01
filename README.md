# Calculadora de Números Complexos
<p>Calcula:</p>
<ul>
  <li>Soma;</li>
  <li>Subtração;</li>
  <li>Multiplicação;</li>
  <li>Exponenciação;</li>
</ul>

## Como funciona
<p>O programa calcula separadamente a parte real e imaginária dos números complexos, e depois imprime o resultado na forma 'a + bi'.</p>
<ul>
  <li>Para calcular, o programa reescreve os métodos de soma, subtração, multiplicação e exponenciação para a classe 'Complexo'</li>
  <li>Para imprimir, o programa reescreve o método __str__() para exibir número complexo já formatado na forma 'a + bi'</li>
</ul>

## Exemplo de uso
Para criar um Número Complexo:
- a = Complexo(1, 1)  ------> "1+1i"
- b = Complexo(1, 1/3)  ---->"1+(1/3)i"
- c = Complexo(-6/5, 3)  ---> "-(6/5)+3i"

Para fazer uma operação:
- soma = a + b
- subtracao = a - b
- multiplicacao = b * c
- exponenciacao = c**3
- equação = a * b + c**2

## Resultados
<table>
  <tr>
    <th>Operação</th>
    <th>Resultado</th>
  </tr>
  <tr>
    <td>Soma</td>
    <td>2+1.333i</td>
  </tr>
  <tr>
    <td>Subtração</td>
    <td>0+0.667i</td>
  </tr>
  <tr>
    <td>Multiplicação</td>
    <td>-2.2+2.6i</td>
  </tr>
  <tr>
    <td>Potênciação</td>
    <td>30.672-14.04i</td>
  </tr>
  <tr>
    <td>Equação</td>
    <td>-6.893-5.867i</td>
  </tr>
</table>
