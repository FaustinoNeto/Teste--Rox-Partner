import pandas as pd
import matplotlib.pyplot as plt

# Carregar o conjunto de dados
file_name = 'sales_data.xlsx'
sales_data = pd.read_excel(file_name)

# Adicionar uma coluna para o valor total da venda
sales_data['total_value'] = sales_data['quantity'] * sales_data['unit_price']

# Calcular vendas totais por produto (quantidade e valor)
product_sales = sales_data.groupby('product_name').agg({
    'quantity': 'sum',
    'total_value': 'sum'
}).reset_index()

# Ordenar por valor total das vendas
product_sales = product_sales.sort_values(by='total_value', ascending=False)

# Converter a coluna 'order_date' para o formato datetime
sales_data['order_date'] = pd.to_datetime(sales_data['order_date'])

# Calcular as vendas diárias (quantidade e valor)
daily_sales = sales_data.groupby('order_date').agg({
    'quantity': 'sum',
    'total_value': 'sum'
}).reset_index()

# Gráfico 1: Vendas totais por produto (quantidade)
plt.figure(figsize=(10, 6))
plt.bar(product_sales['product_name'],
        product_sales['quantity'], color='skyblue')
plt.title('Total de Vendas por Produto (Quantidade)')
plt.xlabel('Produto')
plt.ylabel('Quantidade Vendida')
plt.show()

# Gráfico 2: Vendas totais por produto (valor)
plt.figure(figsize=(10, 6))
plt.bar(product_sales['product_name'],
        product_sales['total_value'], color='lightgreen')
plt.title('Total de Vendas por Produto (Valor)')
plt.xlabel('Produto')
plt.ylabel('Valor Total das Vendas (R$)')
plt.show()

# Gráfico 3: Vendas diárias (quantidade)
plt.figure(figsize=(10, 6))
plt.plot(daily_sales['order_date'],
         daily_sales['quantity'], marker='o', linestyle='-')
plt.title('Vendas Diárias (Quantidade)')
plt.xlabel('Data do Pedido')
plt.ylabel('Quantidade Vendida')
plt.grid(True)
plt.show()

# Gráfico 4: Vendas diárias (valor)
plt.figure(figsize=(10, 6))
plt.plot(daily_sales['order_date'], daily_sales['total_value'],
         marker='o', linestyle='-', color='orange')
plt.title('Vendas Diárias (Valor)')
plt.xlabel('Data do Pedido')
plt.ylabel('Valor Total das Vendas (R$)')
plt.grid(True)
plt.show()


# Adicionar uma coluna para o valor total da venda
sales_data['total_value'] = sales_data['quantity'] * sales_data['unit_price']

# Converter a coluna 'order_date' para o formato datetime
sales_data['order_date'] = pd.to_datetime(sales_data['order_date'])

# Adicionar uma coluna para o mês
sales_data['order_month'] = sales_data['order_date'].dt.to_period('M')

# Calcular vendas mensais por produto (quantidade e valor)
monthly_sales = sales_data.groupby(['order_month', 'product_name']).agg({
    'quantity': 'sum',
    'total_value': 'sum'
}).reset_index()

# Encontrar o produto mais vendido em cada mês
top_product_per_month = monthly_sales.loc[monthly_sales.groupby('order_month')[
    'quantity'].idxmax()]

# Ordenar os dados por mês
top_product_per_month = top_product_per_month.sort_values(by='order_month')
# Gráfico 5: Produto mais vendido por mês
plt.figure(figsize=(12, 8))
plt.bar(top_product_per_month['order_month'].astype(
    str), top_product_per_month['quantity'], color='skyblue')
for i in range(len(top_product_per_month)):
    plt.text(i, top_product_per_month['quantity'].iloc[i],
             top_product_per_month['product_name'].iloc[i], ha='center', va='bottom')
plt.title('Produto Mais Vendido por Mês (Quantidade)')
plt.xlabel('Mês')
plt.ylabel('Quantidade Vendida')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Correlação entre quantidade e valor total das vendas
plt.figure(figsize=(10, 6))
plt.scatter(sales_data['quantity'], sales_data['total_value'], alpha=0.5)
plt.title('Correlação entre Quantidade e Valor Total das Vendas')
plt.xlabel('Quantidade Vendida')
plt.ylabel('Valor Total das Vendas (R$)')
plt.grid(True)
plt.show()

# Análise dos clientes mais valiosos
top_customers = sales_data.groupby('cliente_id')['total_value'].sum(
).sort_values(ascending=False).head(10).reset_index()

plt.figure(figsize=(10, 6))
plt.bar(top_customers['cliente_id'].astype(str),
        top_customers['total_value'], color='lightcoral')
plt.title('Top 10 Clientes por Valor Total Gasto')
plt.xlabel('ID do Cliente')
plt.ylabel('Valor Total Gasto (R$)')
plt.show()

# Distribuição dos preços dos produtos vendidos
plt.figure(figsize=(10, 6))
plt.hist(sales_data['unit_price'], bins=10,
         color='lightblue', edgecolor='black')
plt.title('Distribuição dos Preços dos Produtos Vendidos')
plt.xlabel('Preço Unitário (R$)')
plt.ylabel('Frequência')
plt.grid(True)
plt.show()

# Análise de retorno de clientes
customer_orders = sales_data.groupby(
    'cliente_id')['order_date'].count().reset_index()
customer_orders.columns = ['cliente_id', 'order_count']

plt.figure(figsize=(10, 6))
plt.hist(customer_orders['order_count'], bins=range(
    1, customer_orders['order_count'].max() + 2), color='lightgreen', edgecolor='black')
plt.title('Distribuição do Número de Pedidos por Cliente')
plt.xlabel('Número de Pedidos')
plt.ylabel('Número de Clientes')
plt.grid(True)
plt.show()
