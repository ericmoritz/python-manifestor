# python-manifestor
A simple project manifest tool

## Usage

```
Usage: manifestor
  manifestor get <fields>...


Options:

  -h --help  Show help for command
```

### Fields:

A field is a JSON Pointer to a schema.org short name.

### Commands:

* get: returns a YAML document of the pointers requested. Returns non-zero if
       any fields are missing


## Example

```
$ cat << EOF
@context:
  @vocab: http://schema.org/

name: test-fixture
author:
  name: Eric
EOF | manifestor get /name /author/name /softwareVersion
/softwareVersion: null
/author/name: Eric
/name: test-fixture
$ echo $?
1
```
