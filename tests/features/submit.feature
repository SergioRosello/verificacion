"""
▪ Si el usuario pulsa el botón Execute y hay texto, la web deberá de
  mostrar por pantalla un listado con las palabras y el número de
  apariciones ordenadas de mayor a menor y, de igual forma, deberá
  de borrarse el texto que aparece en el textfield. En caso de que no
  hubiera ningún texto el botón no tendrá ningún efecto.
"""

Feature: User presses submit button
  Scenario: User introduces "Hola Hola Hola buenos buenos dias" and clicks on Submit
    Given I have access to web http://127.0.0.1:5000/
    Given I have the string "Hola Hola Hola buenos buenos dias"
    When  I introduce string "Hola Hola Hola buenos buenos dias" in the text box and press ENTER
    Then  I see the results are "[u'hola', u'3', u'buenos', u'2', u'dias', u'1']"
    Then  I see the text-box is empty

  Scenario: There is a result and user clicks on Submit
    Given I have access to web http://127.0.0.1:5000/
    Given I have the string "Hola Hola Hola buenos buenos dias"
    When  I introduce string "Hola Hola Hola buenos buenos dias" in the text box and press ENTER
    Then  I see the results are "[u'hola', u'3', u'buenos', u'2', u'dias', u'1']"
    When  I click the Submit button
    Then  I see the results are "[u'hola', u'3', u'buenos', u'2', u'dias', u'1']"

  Scenario: There is nothing in text-box and user click on Submit
    Given I have access to web http://127.0.0.1:5000/
    Then  I see the text-box is empty
    When  I click the Submit button
    Then  I see the text-box is empty
