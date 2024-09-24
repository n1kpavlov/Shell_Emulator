import tarfile
import xml.etree.ElementTree as ET
import tkinter as tk
import os

class Config:
    def __init__(self, config_file):
        self.config_file = config_file
        self.tar_path = None
        self.start_script_path = None
        self.load_config()

    def load_config(self):
        tree = ET.parse(self.config_file)
        root = tree.getroot()
        self.tar_path = root.find('tar_path').text
        self.start_script_path = root.find('start_script_path').text

#class FileSystem:

#class ShellGUI:

if __name__ == '__main__':
    config = Config('config.xml')
    #shell_gui = ShellGUI(config)
