Feature: manifestor get

  Scenario: User get fields that all exist
    Given user executes "manifestor get /name /author/name" using fixture as stdin
    Then the output should be
      """
      /author/name: Eric
      /name: test-fixture

      """
    And the exit code should be 0

  Scenario: User requires a field that does not exist
    Given user executes "manifestor get /name /author/name /nowhere" using fixture as stdin
    Then the output should be
      """
      /nowhere: null
      /author/name: Eric
      /name: test-fixture

      """
    And the exit code should be 1
