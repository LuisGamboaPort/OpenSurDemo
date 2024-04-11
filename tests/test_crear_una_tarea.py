"""
Modulo 1
id caso: 20
Descripción: Crear una Tarea
Test de Opensur
Resultado esperado : Tarea creada para el activo configurado.
"""
from pages.result_crear_tarea import CrearTareaResultPage
from pages.crear_tarea import OpenSurMainPage

def test_crear_tarea(browser):
    init_page = OpenSurMainPage(browser)
    result_page = CrearTareaResultPage(browser)
    PHRASE = ""
    #Scenario: Crear una nueva tarea
    #Given Se ingresa al menú: Activo / Configuración / Tareas
    init_page.load()
    #TODO
    #When Seleccionar el botón "Nuevo+"
    #TODO
    #And Completar los datos
    #TODO
    #And Se confirma con el botón "Guardar"
    #TODO
    #Then La tarea se crea correctamente
    #TODO
    raise Exception("Test Incompleto")

