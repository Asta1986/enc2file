# -*- coding: utf-8 -*-
from os import makedirs
from shutil import rmtree
import enc2file
import unittest


class TestEnc2File(unittest.TestCase):

    def setUp(self):
        makedirs('test_dir')
        self.ef = enc2file.Enc2File()
        self.msg = '@[a_test_msg_string]@'

    def test_read_key_from_file(self):
        file_path = 'test_dir/tmp_key'
        self.ef.key_to_file(file_path)
        fn = enc2file.Enc2File()
        fn.key_from_file(file_path)
        self.assertEqual(fn.decrypt(self.ef.encrypt(self.msg)), self.msg)

    def test_read_encrypted_message(self):
        self.assertEqual(self.ef.decrypt(self.ef.encrypt(self.msg)), self.msg)

    def test_read_encrypted_message_different_key(self):
        key = self.ef.get_encryption_key()
        fn = enc2file.Enc2File()
        fn.set_encryption_key(key)
        self.assertEqual(fn.decrypt(self.ef.encrypt(self.msg)), self.msg)

    def test_read_encrypted_message_from_file(self):
        file_path = 'test_dir/tmp_msg'
        self.ef.enc2file(self.msg, file_path)
        self.assertEqual(self.ef.decrypt_from_file(file_path), self.msg)

    def tearDown(self):
        rmtree('test_dir/')
