import openpyxl
import pyautogui

arquio_xls = openpyxl.load_workbook('vendas_de_produtos.xlsx')
planilha = arquio_xls['vendas']

for linha in planilha.iter_rows(min_row=2):
    pyautogui.click(653,359, duration=1)
    pyautogui.write(linha[0].value)
    pyautogui.click(658,386, duration=1)
    pyautogui.write(linha[1].value)
    pyautogui.click(675,412, duration=1)
    pyautogui.write(str(linha[2].value))
    pyautogui.click(671,437, duration=1)
    pyautogui.write(linha[3].value)
    pyautogui.click(612,464, duration=1)
    pyautogui.click(630,424, duration=1)