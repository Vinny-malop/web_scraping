from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup

driver = webdriver.Chrome(ChromeDriverManager().install())
login_url = 'https://oraculo.mentoriabet.com.br/login'
Superliga_url = 'https://oraculo.mentoriabet.com.br/competition/superliga'
CopaDoMundo_url = 'https://oraculo.mentoriabet.com.br/competition/copadomundo'
EuroCup_url = 'https://oraculo.mentoriabet.com.br/competition/eurocup'
Premiership_url = 'https://oraculo.mentoriabet.com.br/competition/premiership'


email = 'donleonn@live.com'
password = 'tipsterleo'

# fazendo login
driver.get(login_url)
time.sleep(1)
driver.find_element_by_id('email').send_keys(email)
time.sleep(1)
driver.find_element_by_id('password').send_keys(password)
driver.find_element_by_class_name('btn-primary').click()
time.sleep(1)

# funcao para coletar dados de uma determinada pagina


def get_results(url):
    driver.get(url)
    content = driver.page_source
    soup = BeautifulSoup(content, 'html.parser')
    return soup.findAll('div', {'class': 'row mb-4 justify-content-center'})


# chamando a coleta de dados para cada uma das 4 paginas diferentes em resultados
results_Superliga = get_results(Superliga_url)
results_CopaDoMundo = get_results(CopaDoMundo_url)
results_EuroCup = get_results(EuroCup_url)
results_Premiership = get_results(Premiership_url)
# print(results_Superliga[0])
# print(results_CopaDoMundo[0])
# print(results_EuroCup[0])
# print(results_Premiership[0])

# filtrando os resultados de Superliga
for result in results_Superliga:
    times = result.findAll('img', {'class': 'bm-img-time rounded'})
    time_mandante = times[0]['alt']
    time_visitante = times[1]['alt']
    placar_mandante = result.select_one(".text-success").getText()

    placar_visitante = result.select_one(".text-danger").getText()
    print(time_mandante)
    print(placar_mandante)
    print(time_visitante)
    print(placar_visitante)
    # print(time_mandante + placar_mandante + 'x' +
    #   placar_visitante + time_visitante + '\n')
