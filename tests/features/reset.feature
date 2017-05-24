"""
▪ Si el usuario pulsa el botón Reset todo el texto que haya en
  textfield deberá de desaparecer. En caso de que no hubiera texto
  escrito el botón Reset no deberá de hacer nada.
"""

Feature: User presses Reset button
  Scenario: There is text in the text-box
    Given I have access to web http://127.0.0.1:5000/
    And I have the string "Hola Hola Hola buenos buenos dias"
    When  I introduce string "Hola Hola Hola buenos buenos dias" in the text box and click Reset button
    Then  I see the text-box is empty

  Scenario: There is a result and user clicks on Reset
    Given I have access to web http://127.0.0.1:5000/
    And I have the string "Hola Hola Hola buenos buenos dias"
    When  I introduce string "Hola Hola Hola buenos buenos dias" in the text box and press ENTER
    Then  I see the results are "[u'hola', u'3', u'buenos', u'2', u'dias', u'1']"
    When  I click the Reset button
    Then  I see the results are "[u'hola', u'3', u'buenos', u'2', u'dias', u'1']"


  Scenario: There is nothing in text-box and user click on Reset
    Given I have access to web http://127.0.0.1:5000/
    Then  I see the text-box is empty
    When  I click the Reset button
    Then  I see the text-box is empty
