from invoke import task
from invoke.util import cd
import sys
sys.path.insert(0, "jschema")

from version import __version__


@task
def pip(ctx):
    ctx.run("rm -rf dist jschema.egg-info")
    ctx.run("python3 ./setup.py sdist")
    ctx.run("twine upload dist/jschema-{}.tar.gz".format(__version__))

@task
def doc(ctx):
    ctx.run("./setup.py build_sphinx")
    ctx.run("./setup.py upload_sphinx")

@task
def mezzo(ctx):
    ctx.run("mkdir -p build/jschema")
    ctx.run("cp -R jschema setup.py build/jschema")
    with cd("build"):
        ctx.run("tar cfz jschema.tar.gz jschema")
        ctx.run("mv jschema.tar.gz /opt/mezzo/dependencies")
        ctx.run("rm -rf jschema")

@task
def tests(ctx):
    with cd("tests"):
        ctx.run("python test_jschema.py")
