
"""
▪ Un usuario (no hace falta login/registro/etc) puede introducir cualquier
  texto en el textfield (con un máximo de 100 caracteres)
"""

Feature: User introduces text in text box
  Scenario: User introduces "http://ep00.epimg.net/rss/elpais/portada.xml"
    Given I have access to web localhost:4445
      And I have the string "http://ep00.epimg.net/rss/elpais/portada.xml"
    When  I introduce string "http://ep00.epimg.net/rss/elpais/portada.xml" in the text box and press ENTER
    Then  I see there are results

  Scenario: User introduces 101 characters
    Given I have access to web localhost:4445
      And I have the string "http://ep00.epimg.net/rss/elpais/portadaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.xml"
    When  I introduce string "http://ep00.epimg.net/rss/elpais/portadaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.xml" in the text box and press ENTER
    Then  I see there are no results

  Scenario: User introduces "3 jun 2017"
    Given I have access to web localhost:4445
      And I have the string "3 jun 2017"
    When  I introduce string "3 jun 2017" in the text box and press ENTER
    Then  I see there are results

  Scenario: User introduces nonexistent data key
    Given I have access to web localhost:4445
      And I have the string "2 jun 2017"
    When  I introduce string "2 jun 2017" in the text box and press ENTER
    Then  I see there are no results
    And   I see an error code

  Scenario: User introduces nonexistent URL
    Given I have access to web localhost:4445
      And I have the string "http://ep00.epimg.net/rss/elpa/portada.xml"
    When  I introduce string "http://ep00.epimg.net/rss/elpa/portada.xml" in the text box and press ENTER
    Then  I see there are no results
    And   I see an error code

  Scenario: User introduces invalid data
    Given I have access to web localhost:4445
      And I have the string "2 jun 17"
    When  I introduce string "2 jun 17" in the text box and press ENTER
    Then  I see there are no results