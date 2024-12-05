import os
from invoke import task

use_pty = os.name != "nt"

@task
def start(ctx):
    ctx.run("python src/app.py", pty=use_pty)

@task
def test(ctx):
    ctx.run("pytest src", pty=use_pty)

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src", pty=use_pty)

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=use_pty)

@task
def lint(ctx):
    ctx.run("pylint src", pty=use_pty)

@task
def build_db(ctx):
    ctx.run("python src/initialize_db.py", pty=use_pty)
