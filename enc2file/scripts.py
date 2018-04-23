# -*- coding: utf-8 -*-
from enc2file import Enc2File
import click

# Common strs.
hk = 'Encryption key to use.'
hkf = 'Path to the file with the encryption key to use.'
he = 'Encoding to use. Default is UTF-8.'
de = 'utf-8'
optk = '--key'
optkf = '--key_file'
optenc = '--encoding'


@click.group()
def cli():
    pass


@cli.command()
def gen_key():
    """Generates an encryption key to use with enc2file commands."""
    click.echo(Enc2File().get_encryption_key())


# Auxiliary functions to check the options set.
def gen_enc2file(key, key_file, encoding):
    ef = Enc2File(encoding=encoding)
    if key is not None:
        ef.set_encryption_key(key)
    elif key_file is not None:
        ef.key_from_file(key_file)
    return ef


def validate_key(key, key_file):
    if key is None and key_file is None:
        raise click.BadOptionUsage('No key specified.')
    elif key is not None and key_file is not None:
        raise click.BadOptionUsage('Only one key source can be used at once.')


def validate_src(src_file, message):
    if src_file is None and message is None:
        raise click.BadOptionUsage('No text to decrypt given.')
#


@cli.command()
@click.option(optk, help=hk)
@click.option(optkf, help=hkf, type=click.Path())
@click.option('--dest_file', help='Path to the file where the encrypted message will be stored.', type=click.Path())
@click.option(optenc, default=de, help=he)
@click.argument('message')
def encrypt(key, key_file, dest_file, encoding, message):
    """Encrypts received MESSAGE using the specified key and stores it in a file or prints it to stdout."""
    validate_key(key, key_file)
    ef = gen_enc2file(key, key_file, encoding)
    if dest_file is None:
        click.echo(ef.encrypt(message))
    else:
        ef.enc2file(message, dest_file)


@cli.command()
@click.option(optk, help=hk)
@click.option(optkf, help=hkf, type=click.Path())
@click.option('--src_file', help='Path to the file where the encrypted message will be read from.', type=click.Path())
@click.option(optenc, default=de, help=he)
@click.option('--message', help='Encrypted text to decrypt.')
def decrypt(key, key_file, src_file, encoding, message):
    """Decrypts MESSAGE using the specified key and prints it to stdout."""
    ef = gen_enc2file(key, key_file, encoding)
    validate_key(key, key_file)
    validate_src(src_file, message)
    if src_file is None:
        click.echo(ef.decrypt(message))
    else:
        click.echo(ef.decrypt_from_file(src_file))
