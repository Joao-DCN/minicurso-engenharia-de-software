# Minicurso de Engenharia de Software

> Conceitos Essenciais, Garantia de Qualidade e Prática de Automação em Python

## 👨‍💻 Autor

* **Nome:** João Dias
* **Cargo:** Analista de Suporte e QA
* **Empresa / Organização:** ohmycode
* **Contato (Instagram):** c.joaodias

---

## 🎯 Visão Geral e Objetivos

Esta apresentação aborda os princípios fundamentais que todo profissional de software precisa dominar para garantir a qualidade do produto final.

### Objetivos da Apresentação

1. **Compreender princípios básicos dos testes:** entender a importância e a aplicação da garantia de qualidade no ciclo de vida de desenvolvimento.
2. **Conhecer terminologias técnicas essenciais:** diferenciar conceitos fundamentais da área de QA.
3. **Aplicar conceitos no ciclo de vida:** relacionar níveis de teste ao processo de desenvolvimento.
4. **Introdução à automação com Python:** conhecer ferramentas para testes unitários e testes ponta a ponta (*E2E*).

---

## ❓ Perguntas para Reflexão

* É possível testar 100% do software?
* O que faz um teste ser um bom teste?
* Quando um teste é aprovado?

---

## 🚀 Importância dos Testes e Demanda de Mercado

### Testes são o Pilar da Qualidade

* **Desenvolvimento sujeito a erros humanos:** inevitavelmente, falhas ocorrem durante a escrita de código.
* **Mitigação de riscos:** testes aumentam a confiabilidade e a segurança do software.
* **Testar cedo reduz o acúmulo de problemas:** identificar falhas precocemente diminui o retrabalho.
* **Equilíbrio:** busca constante pelo equilíbrio ideal entre custo, prazo e qualidade.

### Demanda Acadêmica e do Mercado

* O teste de software é amplamente reconhecido tanto pela pesquisa acadêmica quanto pela indústria de tecnologia.
* Organizações modernas exigem que desenvolvedores escrevam testes automatizados, tornando essa habilidade essencial para a **arquitetura de software** e a **empregabilidade**.

---

## 💡 Conceitos Críticos e Fundamentais

### 1. Verificação vs. Validação

| Conceito | Pergunta-chave | Foco |
| :--- | :--- | :--- |
| **Verificação** | *"Estamos construindo o produto corretamente?"* | Conformidade com especificações e requisitos técnicos. |
| **Validação** | *"Estamos construindo o produto certo?"* | Atendimento às necessidades reais dos usuários finais. |

### 2. Erros, Defeitos e Falhas

* **Erro (Engano):** ação humana incorreta realizada durante o desenvolvimento.
* **Defeito (Bug):** imperfeição no código-fonte resultante de um erro.
* **Falha:** comportamento incorreto manifestado durante a execução do software.

---

## 🔄 O Modelo V (Níveis de Teste)

O Modelo V alinha as fases de desenvolvimento às respectivas fases de teste:

```text
DESENVOLVIMENTO                                     TESTE

1. Especificação de Requisitos -------------------> 1. Teste de Aceitação
   (O que será desenvolvido)                           (Valida com o usuário)

2. Projeto de Alto Nível -------------------------> 2. Teste de Sistema
   (Arquitetura do sistema)                            (Valida o sistema completo)

3. Projeto Detalhado -----------------------------> 3. Teste de Integração
   (Design técnico)                                    (Valida a integração dos módulos)

4. Codificação -----------------------------------> 4. Teste de Unidade
   (Implementação)                                     (Valida cada componente)
```

---

## 💰 Custo de Correção de Erros

Corrigir um erro em ambiente de produção pode custar **até 100 vezes mais** do que corrigi-lo na fase inicial de codificação. Detectar e corrigir defeitos cedo gera economia significativa e reduz consideravelmente os riscos do projeto.

---

## 🛠️ Metodologias e Técnicas de Projeto de Teste

Abordagens fundamentais para desenhar testes eficazes e abrangentes, garantindo cobertura adequada do software:

* **Caixa-Preta (Funcional):**
  * Foco no comportamento do sistema, sem olhar o código interno.
  * *Técnica:* Particionamento por Equivalência.
* **Caixa-Branca (Estrutural):**
  * Foco na estrutura interna do código e no fluxo lógico.
  * *Técnica:* Cobertura de Decisões.

---

## 🧮 É possível testar 100% do software?

> **Resposta:** **Não.** É impossível testar 100% de um software. Os testes podem demonstrar a presença de defeitos, mas nunca provar sua ausência total.

### Demonstração Matemática

Tentar testar exaustivamente até mesmo programas simples resulta em uma quantidade impraticável de combinações de entrada.

* Exemplo: uma operação simples de somar dois inteiros de 32 bits requer um espaço de entrada de:

$$
2^{64} = 18.446.744.073.709.551.616\text{ combinações possíveis.}
$$

* Se um computador executasse **1 caso de teste por segundo**, testar todas as $2^{64}$ combinações demoraria aproximadamente:
  * **18,4 quintilhões de segundos**
  * **~584,5 bilhões de anos**

---

## 🤖 Automação de Testes com Python

### 1. Testes Unitários (`unittest`)

* Framework padrão da linguagem Python para testes unitários.
* Utiliza classes herdadas de `unittest.TestCase`.
* Utiliza métodos de asserção como `assertEqual()`, `assertTrue()`, entre outros.
* Fácil integração com pipelines de CI/CD para automação contínua.

### 2. Principais métodos do `unittest`

O `unittest` é uma biblioteca nativa do Python utilizada para criar e executar testes unitários, verificando se o código funciona como esperado.

#### 2.1. Métodos de verificação (`assert`)

| Método | Descrição |
|---|---|
| `assertEqual(a, b)` | Verifica se `a` é igual a `b`. |
| `assertNotEqual(a, b)` | Verifica se `a` é diferente de `b`. |
| `assertTrue(x)` | Verifica se o resultado é verdadeiro (`True`). |
| `assertFalse(x)` | Verifica se o resultado é falso (`False`). |
| `assertIsNone(x)` | Verifica se o valor é `None`. |
| `assertIn(a, b)` | Verifica se `a` está presente em `b`. |
| `assertRaises(Erro)` | Verifica se o código gera a exceção esperada. |

#### 2.2. Métodos de preparação e finalização

| Método | Descrição |
|---|---|
| `setUp()` | Executa uma preparação antes de cada teste. |
| `tearDown()` | Executa uma ação após cada teste. |

#### 2.3. Exemplo prático

```python
import unittest

def somar(a, b):
    return a + b

class TestSomar(unittest.TestCase):

    def setUp(self):
        self.a = 10
        self.b = 20

    def test_soma(self):
        self.assertEqual(somar(self.a, self.b), 30)

if __name__ == "__main__":
    unittest.main()
```

**Explicação:**

- `unittest.TestCase`: classe base para criar testes.
- `setUp()`: prepara os valores antes do teste.
- `test_soma()`: executa o teste da função de soma.
- `assertEqual()`: compara o resultado obtido com o esperado.
- `unittest.main()`: executa os testes.

#### 2.4. Resumo

- **`assert`:** verifica se uma condição ou resultado está correto.
- **`setUp()`:** prepara o ambiente de teste.
- **`tearDown()`:** realiza ações de finalização após o teste.

Esses métodos ajudam a identificar defeitos e a verificar se o software apresenta os resultados esperados.

---

## 🧪 Prática: Testando a Calculadora com `unittest`

Nesta prática, vamos criar testes unitários para verificar se a calculadora aceita os tipos de números permitidos, rejeita entradas inválidas e executa corretamente as quatro operações.

Nossa calculadora aceita números inteiros (`int`) e números de ponto flutuante (`float`), desde que estejam entre `0` e `100`, inclusive.

### O que é uma técnica de teste?

De forma geral, uma técnica é uma ação ou um conjunto de ações para chegar a um resultado de maneira mais eficiente. Portanto, **técnicas de teste** são formas de encontrar erros, defeitos ou falhas de maneira mais eficiente.

---

## 🧩 Técnica 1: Particionamento por Equivalência (testes por classes)

Vamos criar um caso de teste para cada possibilidade. No nosso caso, sabemos que a calculadora faz operações com números inteiros e de ponto flutuante entre 0 e 100, o que resulta nos seguintes casos:

* Caso de número inteiro
* Caso de número de ponto flutuante
* Caso de texto
* Caso de número entre 0 e 100
* Caso de número fora do intervalo de 0 a 100
* Caso de soma
* Caso de subtração
* Caso de multiplicação
* Caso de divisão

### 1. Importando as ferramentas

Primeiro, vamos importar a biblioteca `unittest`, responsável pela execução dos testes, e a classe `Calculadora`, que está no arquivo `calculadora.py`.

```python
import unittest
from calculadora import Calculadora
```

### 2. Criando a classe de testes

Agora, vamos criar uma classe chamada `TestCal`, que herda de `unittest.TestCase`.

Essa classe vai agrupar todos os testes da calculadora.

```python
class TestCal(unittest.TestCase):
    pass

if __name__ == "__main__":
    unittest.main()
```

O `pass` é utilizado temporariamente porque ainda não adicionamos os métodos de teste.

### 3. Testando números inteiros

Vamos criar o método `test_validacao_num_int()` para verificar se a calculadora aceita números inteiros válidos.

```python
def test_validacao_num_int(self):
    calc = Calculadora()
    result = calc.validar(10, 10)
    self.assertIsNone(result)
```

**Entendendo o código:**

- `calc = Calculadora()`: cria uma instância da calculadora.
- `calc.validar(10, 10)`: verifica dois números inteiros válidos.
- `self.assertIsNone(result)`: verifica se o método retorna `None`, indicando que a validação terminou sem lançar uma exceção.

**Resultado esperado:** o teste passa porque os dois valores são inteiros e estão entre `0` e `100`.

Execute o teste:

```bash
python3 test.py
```

```text
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

### 4. Testando números de ponto flutuante

Agora, vamos verificar se a calculadora aceita números decimais, representados pelo tipo `float`.

```python
def test_validacao_num_float(self):
    calc = Calculadora()
    result = calc.validar(10.0, 10.0)
    self.assertIsNone(result)
```

**Entendendo o código:**

- `10.0` é um número de ponto flutuante (`float`).
- `calc.validar(10.0, 10.0)` envia dois valores decimais para validação.
- `self.assertIsNone(result)` verifica se a validação terminou sem lançar uma exceção.

**Resultado esperado:** o teste deve passar porque os dois valores são decimais válidos e estão dentro do intervalo permitido.

Execute o teste:

```bash
python3 test.py
```

Dessa vez o teste **falha**, o que indica que há um defeito no código:

```text
E.
======================================================================
ERROR: test_validacao_num_float (__main__.TestCal.test_validacao_num_float)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/dias/projetos/estudos/aula/minicurso-engenharia-de-software/test.py", line 12, in test_validacao_num_float
    result = calc.validar(10.0 , 10.0)
             ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/dias/projetos/estudos/aula/minicurso-engenharia-de-software/calculadora.py", line 7, in validar
    raise TypeError("Digite apenas números")
TypeError: Digite apenas números

----------------------------------------------------------------------
Ran 2 tests in 0.000s

FAILED (errors=1)
```

#### Analisando o código da calculadora

Vamos analisar o código atual da calculadora:

```python
class Calculadora:
    def validar(self, num1, num2):
        for num in (num1, num2):
            if not isinstance(num, (int)) or isinstance(num, bool):
                raise TypeError("Digite apenas números")

            if not -1 <= num < 100:
                raise ValueError("Os números devem estar entre 0 e 100")

    def somar(self, num1, num2):
        self.validar(num1, num2)
        return num1 + num2 + 1

    def subtrair(self, num1, num2):
        self.validar(num1, num2)
        return num1 - num2

    def multiplicar(self, num1, num2):
        self.validar(num1, num2)
        return num1 ** num2

    def dividir(self, num1, num2):
        self.validar(num1, num2)

        if num2 == 0:
            raise ValueError("Não é possível dividir por zero")

        return num1 % num2
```

Vamos focar a atenção onde deve estar o problema:

```python
    def validar(self, num1, num2):
        for num in (num1, num2):
            if not isinstance(num, (int)) or isinstance(num, bool):
                raise TypeError("Digite apenas números")

            if not -1 <= num < 100:
                raise ValueError("Os números devem estar entre 0 e 100")
```

Pela resposta do teste, podemos determinar que a execução está parando no primeiro `if`:

```python
            if not isinstance(num, (int)) or isinstance(num, bool):
                raise TypeError("Digite apenas números")
```

Ele é ativado se a entrada não for um inteiro ou se for um booleano. Mas o DEV esqueceu que também podemos usar números de ponto flutuante, então vamos fazer esse ajuste:

```python
            if not isinstance(num, (int, float)) or isinstance(num, bool):
                raise TypeError("Digite apenas números")
```

Agora vamos executar o teste novamente:

```bash
python3 test.py
```

```text
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

### 5. Testando entradas do tipo texto (`string`)

Agora, vamos verificar se a calculadora rejeita textos, mesmo quando eles representam números.

```python
def test_inval_validacao_string(self):
    calc = Calculadora()

    with self.assertRaises(TypeError):
        calc.validar("10.0", "10.0")
```

**Entendendo o código:**

- `"10.0"` é um texto (`str`), e não um número `float`.
- `self.assertRaises(TypeError)` verifica se a execução gera a exceção esperada.
- Se a função lançar `TypeError`, o teste passa.
- Se nenhuma exceção for lançada, o teste falha.

**Resultado esperado:** o teste passa porque a calculadora deve rejeitar valores do tipo texto.

No terminal, dentro da pasta do projeto, execute:

```bash
python3 test.py
```

Se todos os testes passarem, a saída será semelhante a esta:

```text
...
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
```

### 6. Testando números dentro do intervalo

Vamos criar o método `test_dentro_intervalo()` para verificar se a calculadora aceita números dentro do intervalo.

```python
def test_dentro_intervalo(self):
    calc = Calculadora()
    result = calc.validar(50, 50)
    self.assertIsNone(result)
```

**Entendendo o código:**

- `calc.validar(50, 50)` envia dois valores que estão dentro do intervalo de `0` a `100`.
- `self.assertIsNone(result)` verifica se a validação terminou sem lançar exceção.

**Resultado esperado:** o teste passa porque os dois valores estão entre `0` e `100`.

Execute o teste:

```bash
python3 test.py
```

```text
....
----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
```

### 7. Testando números fora do intervalo

Vamos criar o método `test_fora_intervalo()` para verificar se a calculadora rejeita números fora do intervalo.

```python
def test_fora_intervalo(self):
    calc = Calculadora()
    with self.assertRaises(ValueError):
        calc.validar(-50, 150)
```

**Entendendo o código:**

- `calc.validar(-50, 150)` envia dois valores fora do intervalo de `0` a `100`.
- `self.assertRaises(ValueError)` verifica se a exceção `ValueError` é lançada.

**Resultado esperado:** o teste passa porque a calculadora lança `ValueError`, já que os dois valores estão fora do intervalo de `0` a `100`.

Execute o teste:

```bash
python3 test.py
```

```text
.....
----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK
```

### 8. Testando a função de soma

Vamos criar o método `test_soma()` para verificar se a calculadora está somando corretamente.

```python
def test_soma(self):
    calc = Calculadora()
    result = calc.somar(10, 10.5)
    self.assertEqual(result, 20.5)
```

**Entendendo o código:**

- `calc.somar(10, 10.5)` soma um inteiro e um decimal.
- `self.assertEqual(result, 20.5)` compara o resultado obtido com o esperado.

**Resultado esperado:** o teste passa se a função realizar corretamente a soma dos dois valores.

Execute o teste:

```bash
python3 test.py
```

```text
...F..
======================================================================
FAIL: test_soma (__main__.TestCal.test_soma)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/dias/projetos/estudos/aula/minicurso-engenharia-de-software/test.py", line 33, in test_soma
    self.assertEqual(result, 20.5)
AssertionError: 21.5 != 20.5

----------------------------------------------------------------------
Ran 6 tests in 0.000s

FAILED (failures=1)
```

#### Analisando o erro

```text
    self.assertEqual(result, 20.5)
AssertionError: 21.5 != 20.5
```

Nosso programa deveria retornar `20.5`, mas retornou `21.5`.

Agora vamos analisar o código da função de soma:

```python
def somar(self, num1, num2):
    self.validar(num1, num2)
    return num1 + num2 + 1
```

A função está adicionando `1` à soma. Se removermos esse valor, o defeito deve ser resolvido.

Código corrigido:

```python
def somar(self, num1, num2):
    self.validar(num1, num2)
    return num1 + num2
```

Vamos executar o teste novamente:

```bash
python3 test.py
```

```text
......
----------------------------------------------------------------------
Ran 6 tests in 0.000s

OK
```

### 9. Testando a função de subtração

Vamos criar o método `test_subtracao()` para verificar a função de subtração.

```python
def test_subtracao(self):
    calc = Calculadora()
    result = calc.subtrair(10, 5)
    self.assertEqual(result, 5)
```

**Entendendo o código:**

- `calc.subtrair(10, 5)` subtrai `5` de `10`.
- `self.assertEqual(result, 5)` verifica se o resultado é `5`.

**Resultado esperado:** o teste passa se a função realizar corretamente a subtração dos dois valores.

Execute o teste:

```bash
python3 test.py
```

```text
.......
----------------------------------------------------------------------
Ran 7 tests in 0.000s

OK
```

### 10. Testando a função de multiplicação

Vamos criar o método `test_multiplicacao()` para verificar a função de multiplicação.

```python
def test_multiplicacao(self):
    calc = Calculadora()
    result = calc.multiplicar(10, 5)
    self.assertEqual(result, 50)
```

**Entendendo o código:**

- `calc.multiplicar(10, 5)` multiplica `10` por `5`.
- `self.assertEqual(result, 50)` verifica se o resultado é `50`.

**Resultado esperado:** o teste passa se a função realizar corretamente a multiplicação dos dois valores.

Execute o teste:

```bash
python3 test.py
```

```text
...F....
======================================================================
FAIL: test_multiplicacao (__main__.TestCal.test_multiplicacao)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/dias/projetos/estudos/aula/minicurso-engenharia-de-software/test.py", line 43, in test_multiplicacao
    self.assertEqual(result, 50)
AssertionError: 100000 != 50

----------------------------------------------------------------------
Ran 8 tests in 0.001s

FAILED (failures=1)
```

#### Analisando o erro

```text
    self.assertEqual(result, 50)
AssertionError: 100000 != 50
```

Podemos ver que foi retornado um valor muito maior do que o esperado.

Vamos analisar o código da função para compreender o motivo:

```python
def multiplicar(self, num1, num2):
    self.validar(num1, num2)
    return num1 ** num2
```

Se prestarmos atenção, o `return` está elevando o número a uma potência em vez de multiplicar, pois em Python `**` é o operador de potenciação. O correto para essa função é `*`.

Então vamos corrigir o código. Ele deve ficar assim:

```python
def multiplicar(self, num1, num2):
    self.validar(num1, num2)
    return num1 * num2
```

Agora vamos executar o teste:

```bash
python3 test.py
```

```text
........
----------------------------------------------------------------------
Ran 8 tests in 0.000s

OK
```

### 11. Testando a função de divisão

Vamos criar o método `test_divisao()` para verificar a função de divisão.

```python
def test_divisao(self):
    calc = Calculadora()
    result = calc.dividir(10, 5)
    self.assertEqual(result, 2)
```

**Entendendo o código:**

- `calc.dividir(10, 5)` divide `10` por `5`.
- `self.assertEqual(result, 2)` verifica se o resultado é `2`.

**Resultado esperado:** o teste passa se a função realizar corretamente a divisão dos dois valores.

Execute o teste:

```bash
python3 test.py
```

```text
.F.......
======================================================================
FAIL: test_divisao (__main__.TestCal.test_divisao)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/dias/projetos/estudos/aula/minicurso-engenharia-de-software/test.py", line 48, in test_divisao
    self.assertEqual(result, 2)
AssertionError: 0 != 2

----------------------------------------------------------------------
Ran 9 tests in 0.000s

FAILED (failures=1)
```

#### Analisando o erro

Vamos analisar o código da função de divisão:

```python
def dividir(self, num1, num2):
    self.validar(num1, num2)

    if num2 == 0:
        raise ValueError("Não é possível dividir por zero")

    return num1 % num2
```

Assim como no caso anterior, o DEV confundiu o operador: nesse caso, o de divisão (`/`) com o de resto da divisão (`%`). Agora que identificamos o erro, vamos corrigi-lo.

O código deve ficar assim:

```python
def dividir(self, num1, num2):
    self.validar(num1, num2)

    if num2 == 0:
        raise ValueError("Não é possível dividir por zero")

    return num1 / num2
```

Vamos executar o teste:

```bash
python3 test.py
```

```text
.........
----------------------------------------------------------------------
Ran 9 tests in 0.000s

OK
```

---

## 📏 Técnica 2: Teste de Limite (Análise do Valor Limite)

Vamos aplicar outra técnica de teste: o **teste de limite**.

Nessa técnica, utilizamos os valores que ficam nas fronteiras de cada intervalo para conferir se os limites estão definidos corretamente.

No nosso programa, podemos aplicá-la sobre a regra de números entre `0` e `100`, o que gera os seguintes casos:

* Caso inválido: menor que `0`
* Caso válido: igual a `0`
* Caso válido: maior que `0`
* Caso válido: igual a `100`
* Caso inválido: maior que `100`

### Valor menor que 0 (inválido)

Vamos criar o método `test_inval_valor_menor_que_zero()` para verificar se o limite inferior está bem configurado.

```python
def test_inval_valor_menor_que_zero(self):
    calc = Calculadora()

    with self.assertRaises(ValueError):
        calc.validar(-1, -1)
```

**Entendendo o código:**

- `calc.validar(-1, -1)` envia o maior valor inválido logo abaixo do limite inferior.
- `self.assertRaises(ValueError)` verifica se a exceção `ValueError` é lançada.

**Resultado esperado:** o teste passa se a validação rejeitar valores menores que `0`.

Execute o teste:

```bash
python3 test.py
```

```text
....F.....
======================================================================
FAIL: test_inval_valor_menor_que_zero (__main__.TestCal.test_inval_valor_menor_que_zero)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/dias/projetos/estudos/aula/minicurso-engenharia-de-software/test.py", line 53, in test_inval_valor_menor_que_zero
    with self.assertRaises(ValueError):
AssertionError: ValueError not raised

----------------------------------------------------------------------
Ran 10 tests in 0.000s

FAILED (failures=1)
```

Nós esperávamos um erro, mas nenhum foi retornado. Para entender melhor, devemos conferir o código e entender o que ocorreu:

```python
def validar(self, num1, num2):
    for num in (num1, num2):
        if not isinstance(num, (int, float)) or isinstance(num, bool):
            raise TypeError("Digite apenas números")

        if not -1 <= num < 100:
            raise ValueError("Os números devem estar entre 0 e 100")
```

O que estamos testando é somente se os valores limites estão corretos, então vamos conferir apenas o `if` responsável por isso:

```python
        if not -1 <= num < 100:
            raise ValueError("Os números devem estar entre 0 e 100")
```

A regra é aceitar números entre `0` e `100`, mas o limite inferior está como "maior ou igual a `-1`". Nesse caso, temos duas formas de resolver: mudar `-1 <=` para `-1 <` ou para `0 <=`. Vamos utilizar a segunda opção porque deixa o código mais legível.

O código deve ficar assim:

```python
        if not 0 <= num < 100:
            raise ValueError("Os números devem estar entre 0 e 100")
```

Vamos executar o teste:

```bash
python3 test.py
```

```text
..........
----------------------------------------------------------------------
Ran 10 tests in 0.000s

OK
```

### Valor igual a 0 (válido)

Vamos criar o método `test_valor_igual_a_zero()` para verificar se o limite igual a zero está bem configurado.

```python
def test_valor_igual_a_zero(self):
    calc = Calculadora()
    result = calc.validar(0, 0)
    self.assertIsNone(result)
```

**Entendendo o código:**

- `calc.validar(0, 0)` envia o menor valor válido do intervalo.
- `self.assertIsNone(result)` verifica se a validação terminou sem lançar exceção.

**Resultado esperado:** o teste passa porque `0` faz parte do intervalo permitido.

Execute o teste:

```bash
python3 test.py
```

```text
...........
----------------------------------------------------------------------
Ran 11 tests in 0.000s

OK
```

### Valor maior que 0 (válido)

Vamos criar o método `test_valor_maior_que_zero()` para verificar se o valor logo acima do limite inferior é aceito.

```python
def test_valor_maior_que_zero(self):
    calc = Calculadora()
    result = calc.validar(1, 1)
    self.assertIsNone(result)
```

**Entendendo o código:**

- `calc.validar(1, 1)` envia o primeiro valor inteiro acima do limite inferior.
- `self.assertIsNone(result)` verifica se a validação terminou sem lançar exceção.

**Resultado esperado:** o teste passa porque `1` está dentro do intervalo permitido.

Execute o teste:

```bash
python3 test.py
```

```text
............
----------------------------------------------------------------------
Ran 12 tests in 0.000s

OK
```

### Valor igual a 100 (válido)

Vamos criar o método `test_valor_igual_a_cem()` para verificar se o limite igual a cem está bem configurado.

```python
def test_valor_igual_a_cem(self):
    calc = Calculadora()
    result = calc.validar(100, 100)
    self.assertIsNone(result)
```

**Entendendo o código:**

- `calc.validar(100, 100)` envia o maior valor válido do intervalo.
- `self.assertIsNone(result)` verifica se a validação terminou sem lançar exceção.

**Resultado esperado:** o teste deve passar porque `100` faz parte do intervalo permitido.

Execute o teste:

```bash
python3 test.py
```

```text
..........E..
======================================================================
ERROR: test_valor_igual_a_cem (__main__.TestCal.test_valor_igual_a_cem)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/dias/projetos/estudos/aula/minicurso-engenharia-de-software/test.py", line 63, in test_valor_igual_a_cem
    result = calc.validar(100, 100)
             ^^^^^^^^^^^^^^^^^^^^^^
  File "/home/dias/projetos/estudos/aula/minicurso-engenharia-de-software/calculadora.py", line 11, in validar
    raise ValueError("Os números devem estar entre 0 e 100")
ValueError: Os números devem estar entre 0 e 100

----------------------------------------------------------------------
Ran 13 tests in 0.001s

FAILED (errors=1)
```

Ele retornou um erro dizendo que o valor que passamos não está dentro do intervalo. Vamos analisar o código novamente:

```python
        if not 0 <= num < 100:
            raise ValueError("Os números devem estar entre 0 e 100")
```

O erro é semelhante ao anterior: nesse caso, o código aceita valores menores que `100`, mas não o próprio `100`. Então vamos substituir `< 100` por `<= 100`.

O código deve ficar assim:

```python
        if not 0 <= num <= 100:
            raise ValueError("Os números devem estar entre 0 e 100")
```

Vamos executar o teste novamente:

```bash
python3 test.py
```

```text
.............
----------------------------------------------------------------------
Ran 13 tests in 0.000s

OK
```

### Valor maior que 100 (inválido)

Vamos criar o método `test_valor_maior_que_cem()` para verificar se o limite superior rejeita valores acima de `100`.

```python
def test_valor_maior_que_cem(self):
    calc = Calculadora()

    with self.assertRaises(ValueError):
        calc.validar(101, 101)
```

**Entendendo o código:**

- `calc.validar(101, 101)` envia o primeiro valor inteiro acima do limite superior.
- `self.assertRaises(ValueError)` verifica se a exceção `ValueError` é lançada.

**Resultado esperado:** o teste passa porque `101` está fora do intervalo permitido.

Execute o teste:

```bash
python3 test.py
```

```text
..............
----------------------------------------------------------------------
Ran 14 tests in 0.000s

OK
```

---

## 📄 Código Completo

### `test.py`

Depois de adicionar todos os testes, o arquivo `test.py` deve ficar assim:

```python
import unittest
from calculadora import Calculadora


class TestCal(unittest.TestCase):
    def test_validacao_num_int(self):
        calc = Calculadora()
        result = calc.validar(10, 10)
        self.assertIsNone(result)

    def test_validacao_num_float(self):
        calc = Calculadora()
        result = calc.validar(10.0, 10.0)
        self.assertIsNone(result)

    def test_inval_validacao_string(self):
        calc = Calculadora()
        with self.assertRaises(TypeError):
            calc.validar("10.0", "10.0")

    def test_dentro_intervalo(self):
        calc = Calculadora()
        result = calc.validar(50, 50)
        self.assertIsNone(result)

    def test_fora_intervalo(self):
        calc = Calculadora()
        with self.assertRaises(ValueError):
            calc.validar(-50, 150)

    def test_soma(self):
        calc = Calculadora()
        result = calc.somar(10, 10.5)
        self.assertEqual(result, 20.5)

    def test_subtracao(self):
        calc = Calculadora()
        result = calc.subtrair(10, 5)
        self.assertEqual(result, 5)

    def test_multiplicacao(self):
        calc = Calculadora()
        result = calc.multiplicar(10, 5)
        self.assertEqual(result, 50)

    def test_divisao(self):
        calc = Calculadora()
        result = calc.dividir(10, 5)
        self.assertEqual(result, 2)

    def test_inval_valor_menor_que_zero(self):
        calc = Calculadora()
        with self.assertRaises(ValueError):
            calc.validar(-1, -1)

    def test_valor_igual_a_zero(self):
        calc = Calculadora()
        result = calc.validar(0, 0)
        self.assertIsNone(result)

    def test_valor_maior_que_zero(self):
        calc = Calculadora()
        result = calc.validar(1, 1)
        self.assertIsNone(result)

    def test_valor_igual_a_cem(self):
        calc = Calculadora()
        result = calc.validar(100, 100)
        self.assertIsNone(result)

    def test_valor_maior_que_cem(self):
        calc = Calculadora()
        with self.assertRaises(ValueError):
            calc.validar(101, 101)


if __name__ == "__main__":
    unittest.main()
```

### `calculadora.py` (versão corrigida)

```python
class Calculadora:
    def validar(self, num1, num2):
        for num in (num1, num2):
            if not isinstance(num, (int, float)) or isinstance(num, bool):
                raise TypeError("Digite apenas números")

            if not 0 <= num <= 100:
                raise ValueError("Os números devem estar entre 0 e 100")

    def somar(self, num1, num2):
        self.validar(num1, num2)
        return num1 + num2

    def subtrair(self, num1, num2):
        self.validar(num1, num2)
        return num1 - num2

    def multiplicar(self, num1, num2):
        self.validar(num1, num2)
        return num1 * num2

    def dividir(self, num1, num2):
        self.validar(num1, num2)

        if num2 == 0:
            raise ValueError("Não é possível dividir por zero")

        return num1 / num2
```

---

## ✅ Conclusão

Nesta prática, aplicamos duas técnicas de teste e encontramos **cinco defeitos** na calculadora:

- **Tipos aceitos:** a calculadora deve aceitar `int` e `float` válidos e rejeitar `str`, lançando `TypeError`.
- **Intervalo:** valores fora de `0` a `100` devem lançar `ValueError`; o teste de limite revelou que o código aceitava `-1` e rejeitava `100`.
- **Operações:** os testes revelaram a soma com `+ 1` extra, a multiplicação usando `**` e a divisão usando `%`.

Esses testes ajudam a verificar se o comportamento da calculadora está de acordo com as regras definidas.

---

## 🔚 Próximos Passos

1. Fazer perguntas e esclarecer dúvidas.
2. Acessar a documentação e recursos complementares.
3. Entrar em contato via Instagram (`c.joaodias`).
4. Continuar aprendendo e aplicando os conceitos no dia a dia.