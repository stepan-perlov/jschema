from invoke import task
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
