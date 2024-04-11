"""
Modulo 1
id caso: 1
Descripción: Creación de Solicitudes de Mantenimiento
Test de Opensur
Resultado esperado :La Solicitud de Mantenimiento se envía
al estado "En Revisión"
"""
from pages.result_solicitud_mantenimiento import SolicitudMantenimientoResultPage
from pages.solicitud_mantenimiento import SolicitudMantenimientoPage
def test_solicitud_mantenimiento(browser):
    init_page = SolicitudMantenimientoPage(browser)
    result_page = SolicitudMantenimientoResultPage(browser)
    PHRASE = "En Revisión"
    # Scenario: Crear solicitud de mantenimiento
    init_page.load()
    # Given Se ingresa al menú: Activo / Ejecución de Mantenimiento / Solicitud de Mantenimiento
    #TODO
    #When Seleccionar el botón "+Nuevo"
    #TODO
    #And Completar los datos de la Solicitud de Mantenimiento
    #TODO
    #And Se confirma con el botón "Guardar"
    #TODO
    #And Se envía a Revisión con botón de Avanzar (Doble flecha)
    #TODO
    #Then La Solicitud de Mantenimiento se crea correctamente
    #TODO
    assert PHRASE in result_page.search(PHRASE)
    raise Exception("Test Incompleto")