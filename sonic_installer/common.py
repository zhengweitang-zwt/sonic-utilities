"""
Module holding common functions and constants used by sonic-installer and its
subpackages.
"""

import subprocess
import sys

import click

from .exception import SonicRuntimeException

HOST_PATH = '/host/boot'
IMAGE_PREFIX = 'SONiC-OS-'
IMAGE_DIR_PREFIX = 'image-'

# Run bash command and print output to stdout
def run_command(command):
    click.echo(click.style("Command: ", fg='cyan') + click.style(command, fg='green'))

    proc = subprocess.Popen(command, shell=True, text=True, stdout=subprocess.PIPE)
    (out, _) = proc.communicate()

    click.echo(out)

    if proc.returncode != 0:
        sys.exit(proc.returncode)

# Run bash command and return output, raise if it fails
def run_command_or_raise(argv):
    click.echo(click.style("Command: ", fg='cyan') + click.style(' '.join(argv), fg='green'))

    proc = subprocess.Popen(argv, text=True, stdout=subprocess.PIPE)
    out, _ = proc.communicate()

    if proc.returncode != 0:
        raise SonicRuntimeException("Failed to run command '{0}'".format(argv))

    return out.rstrip("\n")
