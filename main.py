from tkinter import*
from tkinter import Tk, StringVar, ttk
from tkinter import messagebox
from tkinter import filedialog as fd
# IMPORTE PILLOW
from PIL import Image, ImageTk
# IMPORTE CALENDARIO
from tkcalendar import calendar_, DateEntry
from datetime import date

# Importando dados do arquivo view pra main
from view import * 



cor0 = "#2e2d2b"
cor1 = "#feffff"
cor2 = "#4fa882"
cor3 = "#38576b"
cor4 = "#403d3d"
cor5 = "#e06636"
cor6 = "#038cfc"
cor7 = "#3fbfb9"
cor8 = "#263238"
cor9 = "#e9edf5"

# Criando janela ==============================================================================================================================================
 
janela = Tk()
janela.title('')
janela.geometry('900x600')
janela.configure(background=cor9)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")

# Criando frames =============================================================================================================================================

frameCima = Frame(janela, width=1043, height=50,background=cor1, relief=FLAT)
frameCima.grid(row=0, column=0)

frameMeio = Frame(janela, width=1043, height=303,background=cor1, pady=20, relief=FLAT)
frameMeio.grid(row=1, column=0, pady=1,padx=0, sticky=NSEW)

frameBaixo = Frame(janela, width=1043, height=303,background=cor1, relief=FLAT)
frameBaixo.grid(row=2, column=0, pady=0,padx=1, sticky=NSEW)


# Criando funcoes ===============================================================================================================================================
global tree

#nome, fornecedor, valor_da_compra, preco_revenda, data_da_compra, validade, codigo, imagem
# Funcao Inserir
def inserir():
    global imagem, imagem_string, l_imagem

    nome = e_nome.get()
    fornecedor = e_fornecedor.get()
    valorCompra = e_valorCompra.get()
    precoRevenda = e_precoRevenda.get()
    data = e_calendario.get()
    validade = e_validade.get()
    codigo = e_codigo.get()
    imagem = imagem_string

    lista_inserir = [nome, fornecedor, valorCompra, precoRevenda, data, validade, codigo, imagem]

    for i in lista_inserir:
        if i =='':
            messagebox.showerror('Erro', 'Preencha corretamente todos os campos')
            return
    inserir_form(lista_inserir)

    messagebox  .showinfo('Sucesso','Os dados foram inseridos com sucesso')


    e_nome.delete(0,'end')
    e_fornecedor.delete(0,'end')
    e_valorCompra.delete(0,'end')
    e_precoRevenda.delete(0,'end')
    e_calendario.delete(0,'end')
    e_validade.delete(0,'end')
    e_codigo.delete(0,'end') 


    mostrar()



# Funçao atualizar
def atualizar():
    global imagem, imagem_string, l_imagem
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']

        valor = treev_lista[0]

        e_nome.delete(0,'end')
        e_fornecedor.delete(0,'end')
        e_valorCompra.delete(0,'end')
        e_precoRevenda.delete(0,'end')
        e_calendario.delete(0,'end')
        e_validade.delete(0,'end')
        e_codigo.delete(0,'end') 

        id = int(treev_lista[0])
        e_nome.insert(0,treev_lista[1])
        e_fornecedor.insert(0,treev_lista[2])
        e_valorCompra.insert(0,treev_lista[3])
        e_precoRevenda.insert(0,treev_lista[4])
        e_calendario.insert(0,treev_lista[5])
        e_validade.insert(0,treev_lista[6])
        e_codigo.insert(0,treev_lista[7]) 
        imagem_string = treev_lista[8]



        def update():
            global imagem, imagem_string, l_imagem

            nome = e_nome.get()
            fornecedor = e_fornecedor.get()
            valorCompra = e_valorCompra.get()
            precoRevenda = e_precoRevenda.get()
            data = e_calendario.get()
            validade = e_validade.get()
            codigo = e_codigo.get()
            imagem_string 
            imagem = imagem_string

            if imagem == '':
                imagem =  e_codigo.insert(0,treev_lista[7]) 

            lista_atualizar = [nome, fornecedor, valorCompra, precoRevenda, data, validade, codigo, imagem, id]

            for i in lista_atualizar:
                if i == '':
                    messagebox.showerror('Erro', 'Preencha corretamente todos os campos')
                    return  
                
            atualizar_(lista_atualizar)
            messagebox  .showinfo('Sucesso','Os dados foram atualizados com sucesso')

            e_nome.delete(0,'end')
            e_fornecedor.delete(0,'end')
            e_valorCompra.delete(0,'end')
            e_precoRevenda.delete(0,'end')
            e_calendario.delete(0,'end')
            e_validade.delete(0,'end')
            e_codigo.delete(0,'end') 

            b_confirmar.destroy()

            mostrar()

        b_confirmar = Button(frameMeio, command=update, width=13, text='  Confirmar'.upper(), overrelief=RIDGE, font=('Ivy 8 bold'), bg=cor2, fg=cor1)
        b_confirmar.place(x=325, y=150)

    except IndexError:
        messagebox.showerror('Erro', 'Selecione um dos dados da tabela')

    

# Funçao Deletar
def deletar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']

        valor = treev_lista[0]

        deletar_form([valor])
        messagebox  .showinfo('Sucesso','Os dados foram deletados com sucesso')


        mostrar()
    except IndexError:
        messagebox.showerror('Erro', 'Selecione um dos dados da tabela')

    


# Funçao para escolher uma imagem para inserir-a
global imagem, imagem_string, l_imagem

def escolher_imagem():
    global imagem, imagem_string, l_imagem

    imagem = fd.askopenfilename()
    imagem_string = imagem  

# Abrindo imagem de itens do estoque 
    imagem = Image.open(imagem)
    imagem = imagem.resize((170,170))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frameMeio, image=imagem,bg=cor1, fg=cor4)
    l_imagem.place(x=700, y=10)


# Funcao para ver imagem 
def ver_imagem():
    global imagem, imagem_string, l_imagem

    treev_dados = tree.focus()
    treev_dicionario = tree.item(treev_dados)
    treev_lista = treev_dicionario['values']

    valor = [int(treev_lista[0])]

    iten = ver_item(valor)  

    imagem = iten[0][8]

    # Abrindo imagem de icones para botoes 
    imagem = Image.open(imagem)
    imagem = imagem.resize((200,200))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frameMeio, image=imagem, bg=cor1, fg=cor4)
    l_imagem.place(x=700, y=10)





# Trabalhando no frame Cima ==================================================================================================================================

# Abrindo imagem de icones para botoes 
app_img = Image.open('inventario.png')
app_img = app_img.resize((45,45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, text=' Inventário de Estoque', width=900, compound=LEFT,relief=RAISED,anchor= NW, font=('Verdana 20 bold'),bg=cor1, fg=cor4)
app_logo.place(x=0, y=0)

 
# Trabalhando no frame Meio =================================================================================================================================

# Criando entradas
l_nome = Label(frameMeio, text='Nome', height=1, anchor=NW, font=('Ivi 10 bold'), bg=cor1, fg=cor4)
l_nome.place(x=10, y=10)
e_nome = Entry(frameMeio, width=20, justify='left', relief='solid')
e_nome.place(x=145, y=11)


l_fornecedor = Label(frameMeio, text='Fornecedor', height=1, anchor=NW, font=('Ivi 10 bold'), bg=cor1, fg=cor4)
l_fornecedor.place(x=10, y=40)
e_fornecedor = Entry(frameMeio, width=20, justify='left', relief='solid')
e_fornecedor.place(x=145, y=41)


l_valorCompra = Label(frameMeio, text='Valor Compra', height=1, anchor=NW, font=('Ivi 10 bold'), bg=cor1, fg=cor4)
l_valorCompra.place(x=10, y=70)
e_valorCompra = Entry(frameMeio, width=20, justify='left', relief='solid')
e_valorCompra.place(x=145, y=71)


l_precoRevenda = Label(frameMeio, text='Preço Revenda', height=1, anchor=NW, font=('Ivi 10 bold'), bg=cor1, fg=cor4)
l_precoRevenda.place(x=10, y=100)
e_precoRevenda = Entry(frameMeio, width=20, justify='left', relief='solid')
e_precoRevenda.place(x=145, y=101)


l_calendario = Label(frameMeio, text='Data Compra', height=1, anchor=NW, font=('Ivi 10 bold'), bg=cor1, fg=cor4)
l_calendario.place(x=10, y=130)
e_calendario = DateEntry(frameMeio, width=12, background='darkblue', borderwidth=2, year=2022)
e_calendario.place(x=145, y=131)


l_validade = Label(frameMeio, text='Validade', height=1, anchor=NW, font=('Ivi 10 bold'), bg=cor1, fg=cor4)
l_validade.place(x=10, y=160)
e_validade = DateEntry(frameMeio, width=12, background='darkblue', borderwidth=2, year=2022)
e_validade.place(x=145, y=161)


l_codigo = Label(frameMeio, text='Codigo', height=1, anchor=NW, font=('Ivi 10 bold'), bg=cor1, fg=cor4)
l_codigo.place(x=10, y=190)
e_codigo = Entry(frameMeio, width=20, justify='left', relief='solid')
e_codigo.place(x=145, y=191)


# Criando botoes

# botao carregar
l_carregar = Label(frameMeio, text='Imagem do item', height=1, anchor=NW, font=('Ivi 10 bold'), bg=cor1, fg=cor4)
l_carregar.place(x=10, y=220)
b_carregar = Button(frameMeio, command=escolher_imagem, width=20, text='carregar'.upper(), compound=CENTER, anchor=CENTER, overrelief=RIDGE, font=('Ivi 8'), bg=cor1, fg=cor0)
b_carregar.place(x=145, y=221)


# botao Adicionar
# primeiramente carregando imagem do botao
img_add = Image.open('add.png')
img_add = img_add.resize((20, 20))
img_add = ImageTk.PhotoImage(img_add)

b_inserir = Button(frameMeio, command=inserir, image=img_add, width=95, text='  Adicionar'.upper(), compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivi 8'), bg=cor1, fg=cor0)
b_inserir.place(x=325, y=10)

# Botao Atualiuzar
img_update = Image.open('atualizar.png')
img_update = img_update.resize((20, 20))
img_update = ImageTk.PhotoImage(img_update)

b_update = Button(frameMeio, command=atualizar, image=img_update, width=95, text='  Atualizar'.upper(), compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivi 8'), bg=cor1, fg=cor0)
b_update.place(x=325, y=50)

# Botao Delete
img_delete = Image.open('deletar.png')
img_delete = img_delete.resize((20, 20))
img_delete = ImageTk.PhotoImage(img_delete)

b_delete = Button(frameMeio, command=deletar, image=img_delete, width=95, text='  Deletar'   .upper(), compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivi 8'), bg=cor1, fg=cor0)
b_delete.place(x=325, y=90)

# Botao Ver imagem
img_item = Image.open('item.png')
img_item = img_item.resize((20, 20))
img_item = ImageTk.PhotoImage(img_item)

b_itemimg_item = Button(frameMeio, command = ver_imagem , image=img_item, width=95, text='  Ver item'.upper(), compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivi 8'), bg=cor1, fg=cor0)
b_itemimg_item.place(x=325, y=215)

# Labels Quantidade total e valores 
l_total = Label(frameMeio, text='', height=2, anchor=CENTER, width=13 , font=('Ivi 17 bold'), bg=cor7, fg=cor1)
l_total.place(x=465, y=17)
l_total_ = Label(frameMeio, text='    Valor total em estoque   ', height=1, anchor=NW, font=('Ivi 10 bold'), bg=cor7, fg=cor4)
l_total_.place(x=465, y=12)

l_qtd = Label(frameMeio, text='', height=2, anchor=CENTER, width=13, pady=8 , font=('Ivi 17 bold'), bg=cor7, fg=cor1)
l_qtd.place(x=465, y=90)
l_qtd_  = Label(frameMeio, text='  Quantidade total de itens', height=1, anchor=NW, font=('Ivi 10 bold'), bg=cor7, fg=cor4)
l_qtd_.place(x=465, y=96)


# tabela -----------------------------------------------------------
def mostrar():
    global tree

    # creating a treeview with dual scrollbars
    tabela_head = ['#Item','Nome',  'Fornecedor','Valor Compra', 'Preço Revenda', 'Data compra','Validade', 'Codigo']

    lista_itens = ver_form()



    tree = ttk.Treeview(frameBaixo, selectmode="extended",columns=tabela_head, show="headings")

    # vertical scrollbar
    vsb = ttk.Scrollbar(frameBaixo, orient="vertical", command=tree.yview)
    
    # horizontal scrollbar
    hsb = ttk.Scrollbar(frameBaixo, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    frameBaixo.grid_rowconfigure(0, weight=12)

    hd=["center","center","center","center","center","center","center", 'center']
    h=[55,150,100,160,130,100,100, 100]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        n+=1


    # inserindo os itens dentro da tabela
    for item in lista_itens:
        tree.insert('', 'end', values=item)


    quantidade = [0000,00]

    for iten in lista_itens:
        quantidade.append(iten[6])
    
    quantidade = [valor for valor in quantidade if isinstance(valor, int)]
    Total_valor = sum(quantidade)
    Total_itens = len(quantidade)

    l_total['text'] = 'R$ {:,.2f}'.format(Total_valor)
    l_qtd['text'] = Total_itens

mostrar()


janela.mainloop()
