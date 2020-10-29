# Importar as bibliotecas
from selenium import webdriver
import time

from selenium.webdriver.firefox.options import Options
from selenium.webdriver import FirefoxProfile
from selenium.webdriver.common.keys import Keys
# navegar até o Watsapp web 

profile = webdriver.FirefoxProfile(r'C:\Users\Mauricio\AppData\Roaming\Mozilla\Firefox\Profiles\tl3nuwfc.default-release')
driver = webdriver.Firefox(profile)

#driver = webdriver.Firefox(executable_path=r'C:\Users\Mauricio\Desktop\geckodriver.exe', Firefox_options=options)
driver.get('https://web.whatsapp.com/')
time.sleep(30)
# Definir contatos e grupos e mensagem a ser enviada
contatos = ['GRUPO TESTE 1', 'GRUPO TESTE 2']
mensagem = "*Parabéns Angela Jeunon de Alencar e Rangel* a sua inscrição foi efetuada com SUCESSO!" + Keys.SHIFT + Keys.ENTER + Keys.SHIFT + "Seja muito bem vindo(a) ao *Curso Lasers de Alta & Baixa Potência na Odontologia!*" + Keys.SHIFT + Keys.ENTER + Keys.SHIFT + "Não esqueça de fazer sua solicitação para o *Grupo de Inteligencia do Parlamento!* \n""*Parabéns Angela Jeunon de Alencar e Rangel* a sua inscrição foi efetuada com SUCESSO!" + Keys.SHIFT + Keys.ENTER + Keys.SHIFT + "Seja muito bem vindo(a) ao *Curso Lasers de Alta & Baixa Potência na Odontologia!*" + Keys.SHIFT + Keys.ENTER + Keys.SHIFT + "Não esqueça de fazer sua solicitação para o *Grupo de Inteligencia do Parlamento!* \n""*Parabéns Angela Jeunon de Alencar e Rangel* a sua inscrição foi efetuada com SUCESSO!" + Keys.SHIFT + Keys.ENTER + Keys.SHIFT + "Seja muito bem vindo(a) ao *Curso Lasers de Alta & Baixa Potência na Odontologia!*" + Keys.SHIFT + Keys.ENTER + Keys.SHIFT + "Não esqueça de fazer sua solicitação para o *Grupo de Inteligencia do Parlamento!* \n""*Curso Online Lasers de Alta & Baixa Potência na Odontologia*"+ Keys.SHIFT + Keys.ENTER + Keys.SHIFT + "*Ainda temos algumas vagas!*"+ Keys.SHIFT + Keys.ENTER + Keys.SHIFT +"Não perca tempo e mude a sua vida profissional agora mesmo." + Keys.SHIFT + Keys.ENTER + Keys.SHIFT +"Colocamos esse limite de vagas para ter uma *interação maior é atender melhor o suporte do parlamento.* Se você ainda não fez a sua inscrição aproveite pra fazer agora.🥼🦷"+ Keys.SHIFT + Keys.ENTER + Keys.SHIFT +"Clique no link abaixo e se inscreva agora mesmo. *As vagas estão acabando, não perca essa oportunidade!*"+ Keys.SHIFT + Keys.ENTER + Keys.SHIFT +"➡https://iknowodonto.com/inscricao-whatsapp"

# Buscar contatos/grupos


def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)


def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    campo_mensagem[1].click()
    time.sleep(3)
    campo_mensagem[1].send_keys(mensagem)
    time.sleep(2)
    campo_mensagem[1].send_keys(Keys.ENTER)

for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem(mensagem)
# Campo de pesquisa 'copyable-text selectable-text'
# Campo de mensagem privada 'copyable-text selectable-text'
# Enviar mensagens para o contato/grupo
