import mysql.connector

# Função para criar a tabela
def create_tabelas():
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='admin',
        database='projeto_cdc',
    )
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tbl_produtos (
            id_produto INT AUTO_INCREMENT PRIMARY KEY,
            nome_produto VARCHAR(100) NOT NULL,
            marca_produto VARCHAR(100),
            nome_secao VARCHAR(100)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tbl_compra (
            id_compra INT AUTO_INCREMENT PRIMARY KEY,
            id_prod INT,
            qtd_comprada INT,
            custo_compra DECIMAL(10,2),
            estoque_produto INT,
            dt_vld_produto DATE,
            constraint FOREIGN KEY (id_prod) REFERENCES tbl_produtos(id_produto)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tbl_cliente (
            id_cliente INT AUTO_INCREMENT PRIMARY KEY,
            nome_clie VARCHAR(100),       
            cpf_clie VARCHAR(11),
            tel_clie VARCHAR(14)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tbl_vendas (
            id_vendas INT AUTO_INCREMENT PRIMARY KEY,
            id_prod INT,
            id_clie INT,
            valor_venda DECIMAL(10,2),
            qndt_itens INT,
            dt_venda DATE,
            constraint FOREIGN KEY (id_prod) REFERENCES tbl_produtos(id_produto),
            constraint FOREIGN KEY (id_clie) REFERENCES tbl_cliente(id_cliente)
      )
    ''')


    conexao.commit()
    cursor.close()
    conexao.close()


# Função para inserir um produto
def create_prod_multiplos(lista_produtos):
    """
    lista_produtos = [
      
    ]
    """
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='admin',
        database='projeto_cdc',
    )
    cursor = conexao.cursor()
    cursor.executemany(
        "INSERT INTO tbl_produtos (nome_produto, marca_produto, nome_secao) VALUES (%s, %s, %s)",
        lista_produtos
    )
    conexao.commit()
    print('')
    print(f"{cursor.rowcount} produtos inseridos com sucesso.")
    print("")
    cursor.close()
    conexao.close()


# Função para ler os produtos
def read_prod():
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='admin',
        database='projeto_cdc',
    )
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM tbl_produtos")
    produtos = cursor.fetchall()
    print("---------------------------------tbl_produto--------------------------------------")
    for prod in produtos:
        print(f"id_produto: {prod[0]}, nome_produto: {prod[1]}, marca_produto: {prod[2]}, nome_secao: {prod[3]}")
        print("------------------------------------------------------------------------------")
    cursor.close()
    conexao.close()
 

# Função para atualizar um produto
def update_prod(id_produto, novo_nome, nova_marca, nova_secao):
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='admin',
        database='projeto_cdc',
    )
    cursor = conexao.cursor()
    cursor.execute("""
        UPDATE tbl_produtos
        SET nome_produto = %s, marca_produto = %s, nome_secao = %s
        WHERE id_produto = %s
    """, (novo_nome, nova_marca, nova_secao, id_produto))
    conexao.commit()
    cursor.close()
    conexao.close()


# Função para deletar um produto
def delete_prod(id_produto):
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='admin',
        database='projeto_cdc',
    )
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM tbl_produtos WHERE id_produto = %s", (id_produto,))
    conexao.commit()
    cursor.close()
    conexao.close()



#--------------------------------------------------------------------------------------------------------------------------------------




# Função para inserir um produto
def create_compra_multiplos(lista_compra):
    """
    lista_compra = [
      
    ]
    """
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='admin',
        database='projeto_cdc',	
    )
    cursor = conexao.cursor()
    cursor.executemany(
        "INSERT INTO tbl_compra (id_prod ,qtd_comprada, custo_compra, estoque_produto, dt_vld_produto) VALUES (%s, %s, %s, %s, %s)",
        lista_compra
    )
    conexao.commit()
    print('')
    print(f"{cursor.rowcount} compra inseridos com sucesso.")
    print('')
    cursor.close()
    conexao.close()


# Função para ler os produtos
def read_compra():
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='admin',
        database='projeto_cdc',
    )
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM tbl_compra")
    compras = cursor.fetchall()
    print("-------------------------------tbl_compras---------------------------------------")
    print('')
    for comp in compras:
        print(f"id_compra: {comp[0]}, id_prod: {comp[1]}, qtd_comprada: {comp[2]}, custo_compra: {comp[3]}, estoque_produto: {comp[4]},  dt_vld_produto: {comp[5]} ")
        print("-----------------------------------------------------------------------------")

    cursor.close()
    conexao.close()
 

# Função para atualizar um produto
def update_compra(id_compra, id_prod,novo_custo, novo_esto, nova_qtd, nova_vld):
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='admin',
        database='projeto_cdc',
    )
    cursor = conexao.cursor()
    cursor.execute("""
        UPDATE tbl_compra
        SET id_prod = %s, qtd_comprada = %s, custo_compra = %s, estoque_produto = %s, dt_vld_produto = %s
        WHERE id_compra = %s
    """, ( id_prod, nova_qtd, novo_custo, novo_esto , nova_vld, id_compra))
 
    conexao.commit()
    cursor.close()
    conexao.close()


# Função para deletar um produto
def delete_compra(id_compra):
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='admin',
        database='projeto_cdc',
    )
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM tbl_compra WHERE id_compra = %s", (id_compra,))

    conexao.commit()
    cursor.close()
    conexao.close()


#-----------------------------------------------------------------------------------------------------------------------------------------




# Inserir múltiplas vendas
def create_venda_multiplos(lista_venda):
    """
    lista_venda = [
      
    ]
    """
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='admin',
        database='projeto_cdc',
    )
    cursor = conexao.cursor()
    cursor.executemany(
        "INSERT INTO tbl_vendas (id_prod, id_clie, valor_venda, qndt_itens, dt_venda) VALUES (%s, %s, %s, %s, %s)",
        lista_venda
    )
    conexao.commit()
    print('')
    print(f"{cursor.rowcount} vendas inseridas com sucesso.")
    print('')
  
    cursor.close()
    conexao.close()


# Ler todas as vendas
def read_venda():
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='admin',
        database='projeto_cdc',
    )
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM tbl_vendas")
    vendas = cursor.fetchall()
    print("--------------------------------tbl_vendas---------------------------------------")
    print('')
    for venda in vendas:
        print(f"id_vendas: {venda[0]}, id_prod: {venda[1]}, id_clie: {venda[2]}, valor_venda: {venda[3]}, qndt_itens: {venda[4]}, dt_venda: {venda[5]}")
        print("-----------------------------------------------------------------------------")
    
    cursor.close()
    conexao.close()


# Atualizar uma venda
def update_venda(id_venda, id_prod, id_clie, novo_valor, nova_qtd, nova_dt):
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='admin',
        database='projeto_cdc',
    )
    cursor = conexao.cursor()
    cursor.execute("""
        UPDATE tbl_vendas
        SET id_prod = %s, id_clie = %s, valor_venda = %s, qndt_itens = %s, dt_venda = %s
        WHERE id_vendas = %s
    """, ( id_prod, id_clie, novo_valor, nova_qtd, nova_dt, id_venda))

    conexao.commit()
    cursor.close()
    conexao.close()


# Deletar uma venda
def delete_venda(id_venda):
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='admin',
        database='projeto_cdc',
    )
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM tbl_vendas WHERE id_vendas = %s", (id_venda,))

    conexao.commit()
    cursor.close()
    conexao.close()


#---------------------------------------------------------------------------------------------------------------------------------------------


def create_cliente(nome_clie, cpf_clie, tel_clie):
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='admin',
        database='projeto_cdc',
    )
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO tbl_cliente (nome_clie, cpf_clie, tel_clie) VALUES (%s, %s, %s)",
        (nome_clie, cpf_clie, tel_clie)
    )
    conexao.commit()
    print(f"Cliente {nome_clie} inserido com sucesso!")
    cursor.close()
    conexao.close()


def read_cliente():
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='admin',
        database='projeto_cdc',
    )
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM tbl_cliente")
    clientes = cursor.fetchall()
    for cliente in clientes:
        print(f"id_cliente: {cliente[0]}, nome_clie: {cliente[1]}, cpf_clie: {cliente[2]}, tel_clie: {cliente[3]}")
    cursor.close()
    conexao.close()


def update_cliente(id_cliente, novo_nome, novo_cpf, novo_tel):
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='admin',
        database='projeto_cdc',
    )
    cursor = conexao.cursor()
    cursor.execute("""
        UPDATE tbl_cliente
        SET nome_clie = %s, cpf_clie = %s, tel_clie = %s
        WHERE id_cliente = %s
    """, (novo_nome, novo_cpf, novo_tel, id_cliente))
    conexao.commit()
    print(f"Cliente {id_cliente} atualizado com sucesso!")
    cursor.close()
    conexao.close()


def delete_cliente(id_cliente):
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='admin',
        database='projeto_cdc',
    )
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM tbl_cliente WHERE id_cliente = %s", (id_cliente,))
    conexao.commit()
    print(f"Cliente {id_cliente} deletado com sucesso!")
    cursor.close()
    conexao.close()


def menu():
    while True:  # Mantém o programa rodando até o usuário escolher sair
        print("\nEscolha uma opção:")
        print("-" * 50)
        print("1. Adicionar produto")
        print("-" * 50)
        print("2. Listar produtos")
        print("-" * 50)
        print("3. Atualizar produto")
        print("-" * 50)
        print("4. Deletar produto")
        print("-" * 50)
        print("5. Adicionar compra")
        print("-" * 50)
        print("6. Listar compras")
        print("-" * 50)
        print("7. Atualizar compra")
        print("-" * 50)
        print("8. Deletar compra")
        print("-" * 50)
        print("9. Adicionar venda")
        print("-" * 50)
        print("10. Listar vendas")
        print("-" * 50)
        print("11. Atualizar venda")
        print("-" * 50)
        print("12. Deletar venda")
        print("-" * 50)
        print("13. Adicionar cliente")
        print("-" * 50)
        print("14. Listar clientes")
        print("-" * 50)
        print("15. Atualizar cliente")
        print("-" * 50)
        print("16. Deletar cliente")
        print("-" * 50)
        print("17. Sair")
        print("-" * 50)

        opcao = input("Digite sua opção: ")
        print("")

        if opcao == '1':
            nome_produto = input("Digite o nome do produto: ")
            marca_produto = input("Digite a marca do produto: ")
            nome_secao = input("Digite a seção do produto: ")
            create_prod_multiplos([(nome_produto, marca_produto, nome_secao)])
           
        
        elif opcao == '2':
            read_prod()
            break
        
        elif opcao == '3':
            id_produto = int(input("Digite o ID do produto que deseja atualizar: "))
            novo_nome = input("Digite o novo nome: ")
            nova_marca = input("Digite a nova marca: ")
            nova_secao = input("Digite a nova seção: ")
            update_prod(id_produto, novo_nome, nova_marca, nova_secao)
           
        
        elif opcao == '4':
            id_produto = int(input("Digite o ID do produto que deseja deletar: "))
            delete_prod(id_produto)
           
        
        elif opcao == '5':
            id_produto = int(input("Digite o ID do produto comprado: "))
            qtd_comprada = input("Digite a quantidade comprada: ")
            custo_compra = float(input("Digite o custo da compra: "))
            estoque_produto = int(input("Digite o estoque do produto: "))
            dt_vld_produto = input("Digite a data de validade (YYYY-MM-DD): ")
            create_compra_multiplos([(id_produto,qtd_comprada, custo_compra, estoque_produto, dt_vld_produto)])
          
            
        elif opcao == '6':
            read_compra()
            break
        
        elif opcao == '7':
            id_compra = int(input("Digite o ID da compra que deseja atualizar: "))
            id_produto = int(input("Digite o ID do produto comprado: "))
            nova_qtd = input("Digite a nova quantidade comprada: ")
            novo_custo = float(input("Digite o novo custo da compra: "))
            novo_esto = int(input("Digite o novo estoque do produto: "))
            nova_vld = input("Digite a nova data de validade (YYYY-MM-DD): ")
            update_compra(id_compra, id_produto,novo_custo, novo_esto, nova_qtd, nova_vld)
           
        
        elif opcao == '8':
            id_compra = int(input("Digite o ID da compra que deseja deletar: "))
            delete_compra(id_compra)
            
        
        elif opcao == '9':
            id_produto = int(input("Digite o ID do produto vendido: "))
            id_cliente = int(input("Digite o ID do cliente: "))
            valor_venda = float(input("Digite o valor da venda: "))
            qndt_itens = int(input("Digite a quantidade de itens vendidos: "))
            dt_venda = input("Digite a data da venda (YYYY-MM-DD): ")
            create_venda_multiplos([(id_produto, id_cliente, valor_venda, qndt_itens, dt_venda)])
          

        elif opcao == '10':
            read_venda()
            break        

        elif opcao == '11':
            id_venda = int(input("Digite o ID da venda que deseja atualizar: "))
            id_produto = int(input("Digite o ID do produto vendido: "))
            id_cliente = int(input("Digite o ID do cliente: "))
            novo_valor = float(input("Digite o novo valor da venda: "))
            nova_qtd = int(input("Digite a nova quantidade de itens vendidos: "))
            nova_dt = input("Digite a nova data da venda (YYYY-MM-DD): ")
            update_venda(id_venda, id_produto, id_cliente, novo_valor, nova_qtd, nova_dt)
           

        elif opcao == '12':
            id_venda = int(input("Digite o ID da venda que deseja deletar: "))
            delete_venda(id_venda)
          

        elif opcao == '13':
            nome_clie = input("Digite o nome do cliente: ")
            cpf_clie = input("Digite o CPF do cliente: ")
            tel_clie = input("Digite o telefone do cliente: ")
            create_cliente(nome_clie, cpf_clie, tel_clie)
            

        elif opcao == '14':
            read_cliente()
            break

        elif opcao == '15':
            id_cliente = int(input("Digite o ID do cliente que deseja atualizar: "))
            novo_nome = input("Digite o novo nome: ")
            novo_cpf = input("Digite o novo CPF: ")
            novo_tel = input("Digite o novo telefone: ")
            update_cliente(id_cliente, novo_nome, novo_cpf, novo_tel)
          

        elif opcao == '16':
            id_cliente = int(input("Digite o ID do cliente que deseja deletar: "))
            delete_cliente(id_cliente)
          

        elif opcao == '17':
            print("Saindo...")
            break  # Sai do loop e encerra o programa
        
        else:
            print("Opção inválida! Tente novamente.")

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Testando o CRUD

# Cria a tabela (apenas na primeira vez)
create_tabelas()

menu()
# Exemplo de uso das funções13139