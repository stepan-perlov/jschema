from invoke import task
from invoke.util import cd
import jschema


@task
def pip(ctx):
    ctx.run("rm -rf dist jschema.egg-info")
    ctx.run("./setup.py sdist")
    ctx.run("twine upload dist/jschema-{}.tar.gz".format(jschema.__version__))

@task
def doc(ctx):
    ctx.run("./setup.py build_sphinx")
    ctx.run("./setup.py upload_sphinx")

@task
def mezzo(ctx):
    ctx.run("mkdir -p build/jschema")
    ctx.run("cp -R jschema setup.py build/jschema")
    with cd("build"):
        ctx.run("tar cf jschema.tar.gz jschema")
        ctx.run("mv jschema.tar.gz /opt/mezzo/dependencies")
        ctx.run("rm -rf jschema")