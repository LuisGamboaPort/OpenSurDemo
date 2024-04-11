"""
Modulo 1
id caso: 5
Descripción: Autorizar la orden de mantenimiento
Resultado esperado :Orden de Mantenimiento en estado "A Ejecutar"
"""
from pages.result_autorizar_orden_mant import AutorizarOrdenMantResult
from pages.autorizar_orden_mant import OpenSurAutorizarMantenimiento

def test_autorizar_orden_mantenimiento(browser):
    init_page = OpenSurAutorizarMantenimiento(browser)
    result_page = AutorizarOrdenMantResult(browser)
    PHRASE = "A aprobar"
    ESTADO = "A Ejecutar"
    # Scenario: Autorizar orden de mantenimiento
    init_page.load()
    # Given Se ingresa al menú: Activo / Ejecución de Mantenimiento / Todas las Órdenes
    # TODO
    # When Ingresar en Orden en estado "A aprobar"
    # TODO
    # And Completar datos faltantes
    # TODO
    # And Se selecciona: "Autorizar"
    # TODO
    # Then La Orden de Mantenimiento se autoriza correctamente
    # TODO
    raise Exception("Test Incompleto")

