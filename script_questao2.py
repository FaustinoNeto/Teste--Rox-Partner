import pandas as pd
import matplotlib.pyplot as plt

# Carregar o conjunto de dados
file_sales = 'sales_data.xlsx'
sales_data = pd.read_excel(file_sales)

file_customer = 'customer_data.xlsx'
customer_data = pd.read_excel(file_customer)
# Renomear a coluna
customer_data.rename(columns={'id_cliente': 'cliente_id'}, inplace=True)

# Criar a nova coluna 'nome_sobrenome'
customer_data['nome_sobrenome'] = customer_data['nome'] + \
    ' ' + customer_data['sobrenome']

# Excluir a coluna 'nome' e 'sobrenome'
customer_data.drop(columns=['nome'], inplace=True)
customer_data.drop(columns=['sobrenome'], inplace=True)


# Combinar os DataFrames usando a chave 'cliente_id'
combined_data = pd.merge(customer_data, sales_data,
                         on='cliente_id', how='inner')

# Verificar o resultado
print(combined_data.head())

# Salvar os dados combinados em um novo arquivo Excel
combined_data.to_excel('combined_customer_sales_data.xlsx', index=False)
