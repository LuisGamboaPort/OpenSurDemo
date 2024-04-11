from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OpenSurMainPage:
    URL = "https://servicios.opensur.com/grpuya-fbc996b6-15e4-4818-a03c-a909061e2885/web/login?db=GRPUy_Test_automatizado"
    USER = "configurador.mantenimiento"
    PASSWORD = "1234"

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)
    # Login system
    def login(self):
        username_input = self.browser.find_element(By.XPATH,"//input[@id='login']")
        password_input = self.browser.find_element(By.XPATH,"//input[@id='password']")
        login_button = self.browser.find_element(By.XPATH,"//button[@type='submit']")

        username_input.send_keys(self.USER)
        password_input.send_keys(self.PASSWORD)
        login_button.click()

    #
    def click_nuevo_button(self):
        menu_open = self.browser.find_element(By.XPATH," //div[@class='burger-menu']//*[name()='svg']")
        menu_open.click()
        menu_click = self.browser.find_element(By.XPATH,"//span[normalize-space()='Mantenimiento']")
        menu_click.click()
        menu_click = self.browser.find_element(By.XPATH, "//ul[@id='menu_372']//span[@class='dropdown-item__name'][normalize-space()='Configuración']")
        menu_click.click()
        menu_plan = self.browser.find_element(By.XPATH, "//span[normalize-space()='Planificación']")
        menu_plan.click()
        menu_tarea = self.browser.find_element(By.XPATH,"//span[normalize-space()='Tareas']")
        menu_tarea.click()
        menu_nuevo_button = self.browser.find_element(By.CSS_SELECTOR,"div[class='d-xl-none o_control_panel_collapsed_create'] button:nth-child(1")
        menu_nuevo_button.click()


    def completar_datos_tarea(self, nombre, categoria_activos, activos, preventivo, correctivo, material, cantidad, perfil_recurso, horas):
        pass

    def click_guardar_button(self):
        pass

