import nox

@nox.session
def pytest(session):
    session.install('pytest', 'pytest-cov', '.')
    session.run('pytest', '--cov', 'tsquery', './tests')

@nox.session
def mypy(session):
    session.install('mypy', '.')
    session.run('mypy', '-p', 'tsquery', env={'MYPYPATH': './src'})

@nox.session
def flake8(session):
    session.install('flake8', '.')
    session.run('flake8', './src')
