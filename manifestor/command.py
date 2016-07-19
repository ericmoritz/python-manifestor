import sys
from pyld import jsonld
from jsonpointer import resolve_pointer
import pureyaml as yaml


def io_get(yaml_doc, pointers):
    result = {}
    returncode = 0
    for k, v in _get(_parse(yaml_doc), pointers):
        returncode = 1 if v is None else 0
        result[k] = v

    print yaml.dumps(result).strip()
    sys.exit(returncode)


###############################################################################
# Internal
###############################################################################
_CONTEXT = {
    '@vocab': 'http://schema.org/',
}


def _get(doc, pointers):
    """
    >>> from testfixtures import compare
    >>> compare(
    ...   list(_get({
    ...         'name': 'test',
    ...         'author': {
    ...           'name': 'Eric'
    ...          }
    ...        },
    ...        ['/name', '/author/name', '/nowhere']
    ...   )),
    ...   [
    ...     ('/name', 'test'),
    ...     ('/author/name', 'Eric'),
    ...     ('/nowhere', None),
    ...   ]
    ... )
    """
    return (
        (pointer, resolve_pointer(doc, pointer, None))
        for pointer in pointers
    )


def _parse(s):
    """
    >>> from testfixtures import compare
    >>> compare(
    ...   _parse('''
    ... @context:
    ...   @vocab: http://schema.org/
    ... name: test
    ... softwareVersion: 0.1.0
    ... '''),
    ...   {
    ...     '@context': {'@vocab': 'http://schema.org/'},
    ...     'name': 'test',
    ...     'softwareVersion': '0.1.0'
    ...   }
    ... )
    """
    return jsonld.compact(yaml.load(s), _CONTEXT)
