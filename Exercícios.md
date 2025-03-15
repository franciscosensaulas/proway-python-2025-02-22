## Ex.2: Calculadora de Descontos em Produtos

Solicite o nome do produto, o preço original e o percentual de desconto.  
Calcule o valor do desconto e o preço final do produto após o desconto.  

### Validações:  
- **Nome do produto**: mínimo de 3 e máximo de 30 caracteres. `def solicitar_nome`
- **Preço original**: mínimo de 1.00 e máximo de 10000.00. `def solicitar_preco`
- **Percentual de desconto**: mínimo de 0.0 e máximo de 100.0. `def solicitar_percentual_desconto`

Crie funções para:
1. Solicitar as entradas (solicitar_nome, solicitar_preco e solicitar_percentual_desconto) do usuário.
2. Calcular o valor do desconto a partir do preço original e percentual (calcular_desconto)
3. Calcular o preço final após o desconto (calcular_preco_final)
4. Apresentar dados (apresentar_dados)

---

## Ex.3: Calculadora de IMC

Solicite o nome, peso e altura de uma pessoa.  
Calcule o Índice de Massa Corporal (IMC) e classifique o resultado.  

A fórmula para o cálculo do IMC é:  
`IMC = peso / (altura * altura)`  

### Validações:  
- **Nome**: mínimo de 3 e máximo de 30 caracteres.
- **Peso**: mínimo de 20.0 e máximo de 200.0 kg.
- **Altura**: mínimo de 1.0 e máximo de 2.5 metros.

Crie funções para:
1. Calcular o IMC.
2. Classificar o IMC de acordo com as faixas estabelecidas:
   - Abaixo de 18.5: Abaixo do peso.
   - Entre 18.5 e 24.9: Peso normal.
   - Entre 25.0 e 29.9: Sobrepeso.
   - Entre 30.0 e 39.9: Obesidade.
   - Acima de 40.0: Obesidade grave.
3. Solicitar as entradas (nome, peso, altura) do usuário e apresentar o IMC e a classificação.


## Exercícios de banco de dados
- Criar a tabela de Fornencedores com o id e nome (tamanho máximo de 50)
- Criar o arquivo fornecedor_db na pasta src
- Adicionar o menu "Fornecedores" no main
- Criar o método executar_menu no fornecedor_db.py 
- Criar o método cadastrar_fornecedor
- Criar o método listar_fornecedores
- Criar o método apagar_fornecedor
- Criar o método editar_fornecedor
- Adicionar validação de tamanho mínimo do nome de 10 e máximo de 50
- Adicionar uma coluna na tabela de fornecedores de cnpj (tamanho máximo 18)
- Alterar o método cadastrar_fornecedor adicionando o cnpj
- Alterar o método listar_fornecedores adicionando o cnpj
- Alterar o método editar_fornecedor adicionando o cnpj
- Adicionar regex para validar o cnpj no formato '00.000.000/0000-00'
- Adicionar uma coluna na tabela de fornecedores de descrição
- Alterar o método cadastrar_fornecedor adicionando o descrição
- Alterar o método listar_fornecedores adicionando o descrição
- Alterar o método editar_fornecedor adicionando o descrição