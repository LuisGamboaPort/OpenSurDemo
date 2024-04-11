"""
webdriver inizialicacion
Este modulo contiene shared fixtures.
"""
import pytest
import selenium.webdriver

@pytest.fixture
def browser():
    #Inicializa la instancia ChromeDriver
    b = selenium.webdriver.Chrome()

    # waits espera hasta 10 segundos por elemento para aparecer
    b.implicitly_wait(10)

    # Retorna la instancia webdriver a la configuracion inicial temporamente
    yield b

    # limplia la instancia webdriver
    b.quit()