"""
Modulo 1
id caso: 3
Descripción: Creación una Orden de Mantenimiento desde una Solicitud de Mantenimiento. Enviar la OM "A Aprobar"
Test de Opensur
Resultado esperado :Se visualiza la Orden de Mantenimiento Creada y en estado "A Aprobar"
 En la Solicitud de Mantenimiento quedará un nuevo campo relacionado ( "Orden mantenimiento") en pestaña "Mantenimiento".
La Solicitud de Mantenimiento pasará al estado "En Proceso".
"""
from pages.result_orden_mantenimiento import OrdenDeMantenimientoResultPage
from pages.orden_mantenimiento import OrdenDeMantenimientoPageSesion
def test_orden_mantenimiento_sol(browser):
    init_page = OrdenDeMantenimientoPageSesion(browser)
    result_page = OrdenDeMantenimientoResultPage(browser)
    ESTADO = "A Aprobar"
    PESTANA_MANTENIMIENTO = "Orden mantenimiento"
    SOLICITUD = "En Proceso"
    #Scenario: Verificar orden de mantenimiento y enviar a autorizar
    init_page.load()
    #TODO
    #Given Se ingresa al menú: Activo / Ejecución de Mantenimiento / Solicitud de Mantenimiento
    init_page.menu()
    #TODO
    #When Se selecciona la Solicitud de Mantenimiento
    init_page.previous_solicitud_checkpoint()
    #TODO
    #And Se verifica que los siguientes campos estén completados: Activo, Responsable mantenimiento, Equipo de Mantenimiento, Tipo de Mantenimiento
    init_page.formulario_orden()
    #TODO
    #And Se selecciona el botón de Crear Orden (ícono de llave inglesa)
    # init_page.find_element(By,)click()
    #TODO
    #And Seleccionar el botón "Enviar a autorizar"
    #TODO
    #Then La Solicitud de Mantenimiento se envía correctamente para autorización
    # assert title in result_page.result_link_titles()
    # assert result_page.orden_generada()
    #TODO
    raise Exception("Test Incompleto")