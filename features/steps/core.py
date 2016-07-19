import shlex
import subprocess
from testfixtures import compare
from behave import *
from io import BytesIO


@given('user executes "{cmd}" using fixture as stdin')
def execute(context, cmd):
    with file('features/fixtures/manifest.yaml') as fixture:
        proc = subprocess.Popen(
            shlex.split(cmd),
            stdin=fixture,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
    context.pipes = proc.communicate()
    context.returncode = proc.returncode


@then('the output should be')
def assert_stdout(context):
    compare(context.pipes[0], context.text)


@then('the exit code should be {returncode}')
def asset_exitcode(context, returncode):
    compare(context.returncode, int(returncode))
