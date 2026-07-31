import pyautogui as pg
import pandas as pd

pg.PAUSE = 0.5

#Abre o navegador e acessa o site:
pg.press("win")
pg.write("Google Chrome")
pg.press("enter")
pg.moveTo(x=386, y=63)
pg.click()
pg.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pg.press("enter")
pg.sleep(0.5)

#Realiza login:
pg.moveTo(x=744, y=409)
pg.click()
pg.write("email_verídico@yahoo.br")
pg.press("tab")

pg.write("senhasupermegaultraforte123#")
pg.press("enter")

#Cadastrar produtos:
pg.PAUSE = 0.3     

#Importa a base de dados dos produtos:
tabela = pd.read_csv("C:\\Users\\pichau\\Documents\\códigos\\PYTHON\\HashtagProject\\AutomaçãoTarefasBots\\produtos.csv")

#Para cada produto, faça:
for linha in tabela.index :
    pg.moveTo(x=698, y=280)
    pg.click()
    pg.write(str(tabela.loc[linha, "codigo"]))
    pg.press("tab")
    pg.write(str(tabela.loc[linha, "marca"]))
    pg.press("tab")
    pg.write(str(tabela.loc[linha, "tipo"]))
    pg.press("tab")
    pg.write(str(tabela.loc[linha, "categoria"]))
    pg.press("tab")
    pg.write(str(tabela.loc[linha, "preco_unitario"]))
    pg.press("tab")
    pg.write(str(tabela.loc[linha, "custo"]))
    pg.press("tab")
    if (str(tabela.loc[linha, "obs"]) != "nan"):
        pg.write(str(tabela.loc[linha, "obs"]))
    pg.press("tab")
    pg.press("enter")


