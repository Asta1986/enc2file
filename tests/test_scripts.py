from enc2file import Enc2File, scripts
from click.testing import CliRunner
import unittest


class TestScripts(unittest.TestCase):

    def setUp(self):
        self.runner = CliRunner()
        self.ef = Enc2File()

    def test_gen_key(self):
        result = self.runner.invoke(scripts.gen_key)
        self.assertIsInstance(Enc2File(key=result.output), Enc2File)
        self.assertEqual(result.exit_code, 0)

    def test_encrypt(self):
        msg = 'tst_msg'
        result = self.runner.invoke(scripts.encrypt, ['--key', self.ef.get_encryption_key(), msg])
        self.assertNotEqual(result.output, msg)
        self.assertEqual(msg, self.ef.decrypt(result.output))
        self.assertEqual(result.exit_code, 0)

    def test_decrypt(self):
        enc_msg = self.ef.encrypt('tst_msg')
        result = self.runner.invoke(scripts.decrypt, ['--key', self.ef.get_encryption_key(), '--message', enc_msg])
        dec_msg = result.output
        self.assertNotEqual(dec_msg, enc_msg)
        self.assertEqual(dec_msg, 'tst_msg\n')
        self.assertEqual(result.exit_code, 0)
