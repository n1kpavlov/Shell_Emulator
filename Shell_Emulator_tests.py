import unittest
from Shell_Emulator import FileSystem, Config

class TestFileSystem(unittest.TestCase):
    def setUp(self):
        self.file_system = FileSystem('virtual_fs.tar')

    def test_ls(self):
        self.assertEqual(self.file_system.ls(), ['boot', 'dev', 'home', 'readme.txt', 'usr', 'var'])
        self.file_system.cd('usr')
        self.assertEqual(self.file_system.ls(), ['Anton', 'Artem', 'Nikita', 'Yaroslav'])

    def test_cd(self):
        self.file_system.cd('home')
        self.assertEqual(self.file_system.current_dir, 'virtual_fs/home')
        self.file_system.cd('..')
        self.assertEqual(self.file_system.current_dir, 'virtual_fs')

    def test_uname(self):
        self.assertEqual(self.file_system.uname(), 'Linux')
        self.file_system.cd('usr')
        self.assertEqual(self.file_system.uname(), 'Linux')

    def test_pwd(self):
        self.assertEqual(self.file_system.pwd(), 'virtual_fs')
        self.file_system.cd('home')
        self.assertEqual(self.file_system.pwd(), 'virtual_fs/home')

    def test_tree(self):
        self.assertEqual(self.file_system.tree(), 'boot/\ndev/\nhome/\n  secrets/\n    dont open.txt\nreadme.txt\nusr/\n  Anton/\n  Artem/\n  Nikita/\n  Yaroslav/\nvar/\n')
        self.file_system.cd('home')
        self.assertEqual(self.file_system.tree(), 'secrets/\n  dont open.txt\n')

class TestConfig(unittest.TestCase):
    def test_load_config(self):
        config = Config('config.xml')
        self.assertEqual(config.tar_path, 'virtual_fs.tar')
        self.assertEqual(config.start_script_path, 'start.sh')

if __name__ == '__main__':
    unittest.main()
