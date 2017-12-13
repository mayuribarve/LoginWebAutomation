# Created by mayurib at 12/7/2017
Feature: Login to Borland Insurance Web
  # Enter feature description here

  Scenario: Open Borland website
    Given User opens Borland website
    Then  print the title


  Scenario: Login to Borland website
    Given User is on the home page with login option
    When User enters username in email field
    And User enters password in Password field
    And clicks Login button
    Then Login should be successful
    And Logged in User's name should be displayed