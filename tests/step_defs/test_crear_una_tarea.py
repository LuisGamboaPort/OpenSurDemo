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

    # Scenario: Crear una nueva tarea
    # Given Se ingresa al menú: Activo / Configuración / Tareas
    init_page.load()

    # When Seleccionar el botón "Nuevo+"
    init_page.click_nuevo_button()

    # And Completar los datos
    init_page.completar_datos_tarea(
        nombre="Tarea Prueba",
        categoria_activos="Vehículos",
        activos="Auto Prueba",
        preventivo=True,
        correctivo=True,
        material="Prueba",
        cantidad=2,
        perfil_recurso="Mecánico",
        horas="4:00"
    )
    # And Se confirma con el botón "Guardar"
    init_page.click_guardar_button()

    # Then La tarea se crea correctamente
   #  assert result_page.is_tarea_creada(), "La tarea no se creó correctamente"

    # si el assert pasa, no se levanta el raise exception
    raise Exception("Test Incompleto")


