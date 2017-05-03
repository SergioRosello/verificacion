
"""
▪ Un usuario (no hace falta login/registro/etc) puede introducir cualquier
  texto en el textfield (con un máximo de 100 caracteres)
▪ Si el usuario pulsa el botón Reset todo el texto que haya en
  textfield deberá de desaparecer. En caso de que no hubiera texto
  escrito el botón Reset no deberá de hacer nada.
▪ Si el usuario pulsa el botón Execute y hay texto, la web deberá de
  mostrar por pantalla un listado con las palabras y el número de
  apariciones ordenadas de mayor a menor y, de igual forma, deberá
  de borrarse el texto que aparece en el textfield. En caso de que no
  hubiera ningún texto el botón no tendrá ningún efecto.

"""

Feature: User introduces text in text box
  Scenario: User introduces "Hola buenos dias"
    Given I have access to web http://127.0.0.1:5000/
    Given I have the string "Hola Hola Hola buenos buenos dias"
    When I introduce string "Hola Hola Hola buenos buenos dias" in the text box and press ENTER
    Then I see the results to "Hola Hola Hola buenos buenos dias"