import PySimpleGUI as psg

categoria_produtos = ["Eletrônicos", "Móveis", "Eletrodomésticos", "Brinquedos",
                      "Comida", "Bebidas", "Cosméticos", "Esportes", "Jardinagem"]

def janela_cadastro():
    layout = [
        [psg.Text('Cliente'), psg.Input(key='1', size=(20,0))],
        [psg.Text('Produto'), psg.Input(key='2', size=(20,0))],
        [psg.Text('Quantidade'), psg.Input(key='3', size=(3,0))],
        [psg.Text('Categoria'), psg.Combo(categoria_produtos, key='4')],
        [psg.Button('Salvar')]
    ]
    return  psg.Window('Cadastro de Produtos', layout=layout, resizable=True, finalize=True)

window = janela_cadastro()

while True:
    event, values = window.read()
    if event == psg.WINDOW_CLOSED:
        break
    elif event == 'Salvar':
        psg.popup('Produto cadastrado com sucesso')
        window['1'].update('')
        window['2'].update('')
        window['3'].update('')
        window['4'].update('')