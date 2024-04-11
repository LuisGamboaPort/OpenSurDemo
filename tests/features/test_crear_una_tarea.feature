Feature: Crear una Tarea

  Modulo 1
  id caso: 20
  Descripción: Crear una Tarea
  Test de Opensur
  Resultado esperado : Tarea creada para el activo configurado.
@scenario
  Scenario: Crear una nueva tarea
    Given Se ingresa al menú: Activo / Configuración / Tareas
    When Seleccionar el botón Nuevo
    When Completar los datos
      | nombre         | categoria_activos | activos    | preventivo | correctivo | material | cantidad | perfil_recurso | horas |
      | Tarea Prueba   | Vehículos         | Auto Prueba| true       | true       | Prueba   | 2        | Mecánico       | 4:00  |
    And Se confirma con el botón "Guardar"
    Then La tarea se crea correctamente
