"""
▪ Si el usuario pulsa el botón Execute y hay texto, la web deberá de
  mostrar por pantalla un listado con las palabras y el número de
  apariciones ordenadas de mayor a menor y, de igual forma, deberá
  de borrarse el texto que aparece en el textfield. En caso de que no
  hubiera ningún texto el botón no tendrá ningún efecto.
"""

Feature: User presses submit button
  Scenario: User introduces "http://ep00.epimg.net/rss/elpais/portada.xml" and clicks on Submit
    Given I have access to web http://127.0.0.1:8000/
      And I have the string "http://ep00.epimg.net/rss/elpais/portada.xml"
    When  I introduce string "http://ep00.epimg.net/rss/elpais/portada.xml" in the text box and press ENTER
    Then  I see there are results
      And I see the text-box is empty

  Scenario: There is a result and user clicks on Submit
    Given I have access to web http://127.0.0.1:8000/
      And I have the string "http://ep00.epimg.net/rss/elpais/portada.xml"
      And I introduce string "http://ep00.epimg.net/rss/elpais/portada.xml" in the text box and press ENTER
      And I see there are results
    When  I click the Submit button
    Then  I see there are results

  Scenario: There is nothing in text-box and user click on Submit
    Given I have access to web http://127.0.0.1:8000/
      And I see the text-box is empty
    When  I click the Submit button
    Then  I see the text-box is empty
