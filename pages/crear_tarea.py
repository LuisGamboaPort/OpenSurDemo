"""
id caso : 20
Este modulo contiene la pagina web a testear
la pagina objeto
"""


class OpenSurMainPage:
    def __init__(self, browser):
        self.browser = browser
        # You may initialize any elements or variables needed here

    def load(self):
        # Implement code to navigate to the main page
        pass

    def click_nuevo_button(self):
        # Implement code to locate and click on the "Nuevo+" button
        pass

    def completar_datos_tarea(self, nombre, categoria_activos, activos, preventivo, correctivo, material, cantidad, perfil_recurso, horas):
        # Implement code to fill out the task data based on the provided inputs
        pass

    def click_guardar_button(self):
        # Implement code to locate and click on the "Guardar" button
        pass

