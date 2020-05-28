"""
Run `tox -s (session-name)` to run a suite.
Run `tox` to run all suites.

If you are contributing, please run all suites and fix all
errors and warning before submitting a pull request.
"""
import nox


@nox.session
def test(session):
    """
    Run all test files in the project.
    """
    session.install("-r", "requirements/testing.txt")
    session.run("pytest",
                env={"DJANGO_SETTINGS_MODULE": "config.settings.testing"})


@nox.session
def fix(session):
    """
    Recursively formats files specified in the `modules` tuple.
    isort:  Sorts imports
    black:  Standardizes all files to a strict style
    yapf:   Makes all files conform to PEP8
    """
    modules = ("dinedash", "config", "manage.py")
    session.install("isort", "black", "yapf")
    session.run("isort", "--atomic", "-rc", *modules)
    session.run("black", *modules)
    session.run("yapf", "-i", "--recursive", *modules)


@nox.session
def lint(session):
    """
    Recursively formats files specified in the `modules` tuple.
    flake8: Checks for PEP8 syntax errors
    pylint: Checks for stylistic and logical syntax errors
    """
    modules = ("dinedash",)
    session.install("flake8", "pylint")
    session.run("flake8", *modules)
    session.run("pylint", *modules)
