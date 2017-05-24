
"""
▪ Un usuario (no hace falta login/registro/etc) puede introducir cualquier
  texto en el textfield (con un máximo de 100 caracteres)
"""

Feature: User introduces text in text box
  Scenario: User introduces "Hola Hola Hola buenos buenos dias"
    Given I have access to web http://127.0.0.1:5000/
    And I have the string "Hola Hola Hola buenos buenos dias"
    When  I introduce string "Hola Hola Hola buenos buenos dias" in the text box and press ENTER
    Then  I see the results are "[u'hola', u'3', u'buenos', u'2', u'dias', u'1']"

  Scenario: User introduces 101 characters
    Given I have access to web http://127.0.0.1:5000/
    And I have the string "b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b"
    When  I introduce string "b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b" in the text box and press ENTER
    Then  I see the results are "[u'b', u'50']"

