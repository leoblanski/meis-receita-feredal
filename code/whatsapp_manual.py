from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import urllib.parse

message = """
Olá! Me chamo Leonardo e sou o criador da plataforma chamada FastControl.

Ela ajuda pequenos empreendedores a controlar vendas, estoque, clientes de forma simples e automática.

Estou enviando essa mensagem para apresentar a ferramenta e, se fizer sentido pra você, basta acessar o link abaixo que você encontrará mais informações.

Não é necessário pagamento inicial, você poderá testar a plataforma por 30 dias sem compromisso, caso não goste, basta cancelar.

FastControl: https://fastcontrol.com.br Acesse e clique em "Iniciar 30 dias grátis" para começar a usar.

Caso tenha interesse, me avise que posso te ajudar a configurar a plataforma e tirar suas dúvidas.
"""

numbers = [
    "5511999999999",  # Substitua pelos números de telefone
]

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")
input("Escaneie o QR code e pressione Enter para continuar...")

for number in numbers:
    url = f"https://web.whatsapp.com/send?phone={number}&text={urllib.parse.quote(message)}"
    driver.get(url)
    time.sleep(10)  # espera a conversa abrir

    try:
        send_btn = driver.find_element(By.XPATH, '//span[@data-icon="send"]')
        send_btn.click()
        print(f"Mensagem enviada para {number}")
    except Exception as e:
        print(f"Erro ao enviar para {number}: {e}")
# Try, if error, remove the number from the list

    time.sleep(5)

driver.quit()