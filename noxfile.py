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
    session.run(
        "coverage",
        "run",
        "-m",
        "pytest",
        env={"DJANGO_SETTINGS_MODULE": "config.settings.testing"},
    )
    session.run("coverage", "report", "-m")


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
    session.run("black", *modules)
    session.run("yapf", "-i", "--recursive", *modules)
    session.run("isort", "--atomic", "-rc", *modules)


@nox.session
def lint(session):
    """
    Recursively formats files specified in the `modules` tuple.
    flake8: Checks for PEP8 syntax errors
    pylint: Checks for stylistic and logical syntax errors
    """
    modules = ("dinedash", )
    session.install("flake8", "pylint")
    session.run("flake8", *modules)
    # To ignore Django errors, pylint_django needs Django and factory_boy
    session.install("pylint-django", "django", "factory_boy")
    session.run("pylint", "--load-plugins", "pylint_django", *modules)
