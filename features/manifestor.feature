Feature: manifestor get

  Scenario: User uses get-value command on existing column
    Given user executes "manifestor get-value /name" using fixture as stdin
    Then the output should be
      """
      test-fixture
      """
    And the exit code should be 0
    
  Scenario: User uses get-value command on missing column
    Given user executes "manifestor get-value /softwareVersion" using fixture as stdin
    Then the output should be
      """
      """
    And the exit code should be 1


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
