#          COMUNIDADE SAMUEL MAGGI
#        CAIXA ELETRONICO EM PYTHON

import customtkinter as ctk

ctk.set_appearance_mode("dark")

# =========================================================
# JANELA
# =========================================================

app = ctk.CTk()
app.geometry("1120x720")
app.resizable(False, False)
app.title("Comunidade Samuel Maggi // Caixa Eletronico em Python")

BG = "#070A0F"
CARD = "#0F141C"
CARD2 = "#151B24"
BORDA = "#232C39"

BRANCO = "#F4F7FA"
CINZA = "#8491A3"

VERDE = "#32D583"
VERDE2 = "#163F2E"
AZUL = "#3B82F6"
LARANJA = "#F59E0B"
VERMELHO = "#EF4444"

app.configure(fg_color=BG)

# =========================================================
# DADOS DA CONTA
# =========================================================

saldo = 1500.00
operacao = None
entrada = ""

historico = [
    "Conta iniciada       + R$ 1.500,00"
]    


def moeda(valor):
    valor = f"{valor:,.2f}"   
    valor = valor.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {valor}" 


# =========================================================    
# LOGICA
# =========================================================

def atualizar():
    saldo_txt.configure(text=moeda(saldo))

    if entrada:    
        valor = int(entrada) / 100   
        valor_txt.configure(text=moeda(valor))      
    else:        
        valor_txt.configure(text="R$ 0,00") 

    linhas = historico[:4]       

    extrato_txt.configure(   
        text="\n".join(linhas) 
    )        


def mensagem(texto, cor=CINZA):   
    status.configure(
        text=texto,    
        text_color=cor        
    )        


def escolher(tipo):   
    global operacao, entrada

    operacao = tipo    
    entrada = ""  

    operacao_txt.configure(   
        text=tipo.upper()   
    )        

    mensagem(   
        f"Digite o valor para {tipo}." 
    )        

    atualizar()   


def digitar(numero):   
    global entrada

    if operacao is None:    
        mensagem(   
            "Escolha SACAR ou DEPOSITAR primeiro.",      
            LARANJA            
        )            
        return        

    if len(entrada) < 8:       
        entrada += str(numero)   

    atualizar()       


def valor_rapido(valor):    
    global entrada    

    if operacao is None:    
        mensagem(        
            "Escolha uma operacao primeiro.",           
            LARANJA            
        )            
        return        

    entrada = str(        
        int(valor * 100)        
    )        

    atualizar()    


def limpar():    
    global entrada    

    entrada = ""   
    mensagem("Valor apagado.")   
    atualizar()    


def cancelar():    
    global operacao, entrada    

    operacao = None    
    entrada = ""   

    operacao_txt.configure(    
        text="NOVA OPERACAO"      
    )        

    mensagem(   
        "Selecione uma operacao."  
    )        

    atualizar()    


def confirmar():    
    global saldo, operacao, entrada    

    if operacao is None:    
        mensagem(        
            "Escolha uma operacao.",          
            LARANJA            
        )            
        return        

    if not entrada:        
        mensagem(   
            "Digite um valor.",      
            LARANJA            
        )            
        return        

    valor = int(entrada) / 100        

    if valor <= 0:    
        mensagem(        
            "Valor invalido.",           
            VERMELHO            
        )            
        return        

    if operacao == "sacar":       

        if valor > saldo:        
            mensagem(           
                "SALDO INSUFICIENTE",          
                VERMELHO                
            )                
            return            

        saldo -= valor            

        historico.insert(        
            0,            
            f"Saque               - {moeda(valor)}"           
        )            

        mensagem(        
            "SAQUE REALIZADO COM SUCESSO",           
            VERDE            
        )            

    elif operacao == "depositar":      

        saldo += valor    

        historico.insert(        
            0,            
            f"Deposito            + {moeda(valor)}"           
        )            

        mensagem(        
            "DEPOSITO REALIZADO COM SUCESSO",           
            VERDE            
        )            

    operacao = None        
    entrada = ""   

    operacao_txt.configure(    
        text="NOVA OPERACAO"       
    )        

    atualizar()    


def consultar_saldo():    
    mensagem(    
        f"Saldo disponivel: {moeda(saldo)}",       
        VERDE        
    )        


# =========================================================    
# COMPONENTES
# =========================================================

def titulo(parent, texto, tamanho=14, cor=CINZA):
    return ctk.CTkLabel(
        parent,    
        text=texto,        
        font=("Segoe UI", tamanho, "bold"),   
        text_color=cor        
    )        


def botao(parent, texto, comando, cor=CARD2, largura=150):   
    return ctk.CTkButton(
        parent,    
        text=texto,        
        width=largura,        
        height=52,        
        corner_radius=12,        
        fg_color=cor,        
        hover_color="#26303D",      
        font=("Segoe UI", 15, "bold"),   
        command=comando        
    )        


# =========================================================    
# CABECALHO
# =========================================================

header = ctk.CTkFrame(
    app,
    fg_color="transparent"  
)    

header.pack(
    fill="x",
    padx=44,    
    pady=(28, 18)   
)    

ctk.CTkLabel(
    header,
    text="COMUNIDADE SAMUEL MAGGI",  
    font=("Segoe UI", 25, "bold"),
    text_color=BRANCO    
).pack(anchor="w") 

ctk.CTkLabel(
    header,
    text="ATM // PYTHON  •  SIMULACAO DIDATICA",  
    font=("Segoe UI", 13, "bold"),
    text_color=VERDE    
).pack(   
    anchor="w",
    pady=(3, 0)   
)    

# =========================================================
# CONTEUDO
# =========================================================

main = ctk.CTkFrame(
    app,
    fg_color="transparent"  
)    

main.pack(
    fill="both",
    expand=True,    
    padx=44,    
    pady=(0, 38)   
)    

main.grid_columnconfigure(0, weight=6)
main.grid_columnconfigure(1, weight=4)
main.grid_rowconfigure(0, weight=1)

# =========================================================
# PAINEL ESQUERDO
# =========================================================

esquerda = ctk.CTkFrame(
    main,
    fg_color=CARD,    
    corner_radius=24,    
    border_width=1,    
    border_color=BORDA    
)    

esquerda.grid(
    row=0,
    column=0,    
    sticky="nsew",  
    padx=(0, 12)   
)    

topo_conta = ctk.CTkFrame(
    esquerda,
    fg_color="transparent"  
)    

topo_conta.pack(
    fill="x",
    padx=32,    
    pady=(30, 8)   
)    

titulo(
    topo_conta,
    "SALDO DISPONIVEL"  
).pack(anchor="w") 

saldo_txt = ctk.CTkLabel(
    topo_conta,
    text=moeda(saldo),   
    font=("Segoe UI", 48, "bold"),
    text_color=VERDE    
)    

saldo_txt.pack(
    anchor="w",
    pady=(4, 2)   
)    

ctk.CTkLabel(
    topo_conta,
    text="Samuel Maggi  •  Conta demo 0001 / 2026",  
    font=("Segoe UI", 13), 
    text_color=CINZA    
).pack(anchor="w") 

ctk.CTkFrame(
    esquerda,
    height=1,    
    fg_color=BORDA    
).pack(   
    fill="x",
    padx=32,    
    pady=22    
)    

titulo(
    esquerda,
    "OPERACOES"  
).pack(   
    anchor="w",
    padx=32    
)    

acoes = ctk.CTkFrame(
    esquerda,
    fg_color="transparent"  
)    

acoes.pack(
    fill="x",
    padx=32,    
    pady=(8, 15)   
)    

acoes.grid_columnconfigure((0, 1), weight=1)

botao(
    acoes,
    "CONSULTAR SALDO",  
    consultar_saldo    
).grid(   
    row=0,
    column=0,    
    sticky="ew",  
    padx=(0, 6),   
    pady=6    
)    

botao(
    acoes,
    "SACAR",  
    lambda: escolher("sacar"), 
    AZUL    
).grid(   
    row=0,
    column=1,    
    sticky="ew",  
    padx=(6, 0),   
    pady=6    
)    

botao(
    acoes,
    "DEPOSITAR",  
    lambda: escolher("depositar"), 
    VERDE2    
).grid(   
    row=1,
    column=0,    
    sticky="ew",  
    padx=(0, 6),   
    pady=6    
)    

botao(
    acoes,
    "LIMPAR OPERACAO",  
    cancelar    
).grid(   
    row=1,
    column=1,    
    sticky="ew",  
    padx=(6, 0),   
    pady=6    
)    

titulo(
    esquerda,
    "ULTIMAS MOVIMENTACOES"  
).pack(   
    anchor="w",
    padx=32,    
    pady=(12, 5)   
)    

extrato_txt = ctk.CTkLabel(
    esquerda,
    text="",  
    justify="left",  
    font=("Consolas", 14), 
    text_color=CINZA    
)    

extrato_txt.pack(
    anchor="w",
    padx=32,    
    pady=(5, 15)   
)    

status = ctk.CTkLabel(
    esquerda,
    text="Selecione uma operacao.",  
    font=("Segoe UI", 14, "bold"),
    text_color=CINZA    
)    

status.pack(
    anchor="w",
    padx=32,    
    pady=(4, 25)   
)    

# =========================================================
# PAINEL DIREITO
# =========================================================

direita = ctk.CTkFrame(
    main,
    fg_color=CARD,    
    corner_radius=24,    
    border_width=1,    
    border_color=BORDA    
)    

direita.grid(
    row=0,
    column=1,    
    sticky="nsew",  
    padx=(12, 0)   
)    

operacao_txt = titulo(
    direita,
    "NOVA OPERACAO",  
    15    
)    

operacao_txt.pack(
    pady=(27, 3)
)    

valor_txt = ctk.CTkLabel(
    direita,
    text="R$ 0,00",  
    font=("Segoe UI", 38, "bold"),
    text_color=BRANCO    
)    

valor_txt.pack(
    pady=(0, 14)
)    

# VALORES RAPIDOS

rapidos = ctk.CTkFrame(
    direita,
    fg_color="transparent"  
)    

rapidos.pack(
    pady=(0, 12)
)    

for coluna, valor in enumerate(
    (50, 100, 200)
):    
    ctk.CTkButton(
        rapidos,    
        text=f"R$ {valor}",     
        width=92,        
        height=38,        
        corner_radius=10,        
        fg_color="#202733",      
        hover_color="#2A3543",      
        command=lambda v=valor: valor_rapido(v)       
    ).grid(       
        row=0,    
        column=coluna,        
        padx=4        
    )        

# TECLADO    

teclado = ctk.CTkFrame(
    direita,
    fg_color="transparent"  
)    

teclado.pack()

for numero in range(1, 10):

    linha = (numero - 1) // 3
    coluna = (numero - 1) % 3   

    ctk.CTkButton(   
        teclado,    
        text=str(numero),       
        width=82,        
        height=54,        
        corner_radius=11,        
        fg_color=CARD2,        
        hover_color="#27313E",      
        font=("Segoe UI", 18, "bold"),   
        command=lambda n=numero: digitar(n)       
    ).grid(       
        row=linha,    
        column=coluna,        
        padx=5,        
        pady=5        
    )        

ctk.CTkButton(   
    teclado,
    text="0",  
    width=82,    
    height=54,    
    corner_radius=11,    
    fg_color=CARD2,    
    hover_color="#27313E",  
    font=("Segoe UI", 18, "bold"),
    command=lambda: digitar(0)   
).grid(   
    row=3,
    column=1,    
    padx=5,    
    pady=5    
)    

# CONTROLES

controles = ctk.CTkFrame(
    direita,
    fg_color="transparent"  
)    

controles.pack(
    pady=(18, 0)
)    

ctk.CTkButton(
    controles,
    text="CANCELAR",  
    width=105,    
    height=46,    
    corner_radius=11,    
    fg_color=VERMELHO,    
    hover_color="#C83A3A",  
    command=cancelar    
).grid(   
    row=0,
    column=0,    
    padx=4    
)    

ctk.CTkButton(
    controles,
    text="LIMPAR",  
    width=90,    
    height=46,    
    corner_radius=11,    
    fg_color=LARANJA,    
    hover_color="#D68709",  
    command=limpar    
).grid(   
    row=0,
    column=1,    
    padx=4    
)    

ctk.CTkButton(
    controles,
    text="CONFIRMAR",  
    width=115,    
    height=46,    
    corner_radius=11,    
    fg_color=VERDE,    
    hover_color="#22AE70",  
    command=confirmar    
).grid(   
    row=0,
    column=2,    
    padx=4    
)    

ctk.CTkLabel(
    direita,
    text="Sistema demonstrativo • nenhum dado bancario real",  
    font=("Segoe UI", 11), 
    text_color="#576273"  
).pack(   
    pady=(22, 0)
)    

# =========================================================
# INICIO
# =========================================================

atualizar()

app.mainloop()