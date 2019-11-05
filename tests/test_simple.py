# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import os

bugcatcher_ci = __import__('bugcatcher-ci')
ftl_sid = os.environ.get('FTL_SID') # Keep it secure!
ftl_project = os.environ.get('FTL_PROJECT') or 'BUGCATCHER CI'
ftl = bugcatcher_ci.CI(ftl_sid, ftl_project)

def test_with_bugcatcher():
    print("\nTesting codebase with BugCatcher API...")
    uploaded = ftl.push(ftl_project, ".")
    assert uploaded
    tested = ftl.test(ftl_project, 'medium')
    assert tested


def test_success():
    assert True
