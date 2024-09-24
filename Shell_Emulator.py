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

class FileSystem:
    def __init__(self, tar_path):
        self.tar_path = tar_path
        self.root = 'virtual_fs'
        self.current_dir = self.root
        self.file_system = {}
        self.load_tar()

    def load_tar(self):
        with tarfile.open(self.tar_path, 'r') as tar:
            for member in tar.getmembers():
                if member.isfile():
                    self.file_system[member.name] = {
                        'type': 'file',
                        'size': member.size,
                        'content': tar.extractfile(member).read().decode('utf-8')
                    }
                else:
                    self.file_system[member.name] = {
                        'type': 'dir',
                        'size': None,
                        'content': None
                    }
                    
    def ls(self, path=None):
        if path is None:
            path = self.current_dir
        result = []
        for key in self.file_system:
            if key.startswith(path) and key.count('/') == path.count('/') + 1:
                result.append(key.split('/')[-1])
        return result
        
    def cd(self, path):
        if path == '..':
            self.current_dir = os.path.dirname(self.current_dir)
            if self.current_dir == '':
                self.current_dir = self.root
            return ""
        elif path == '/':
            self.current_dir = self.root
            return ""
        elif path in self.ls(self.current_dir):
            self.current_dir += f'/{path}'
            return ""
        else:
            return f'No such files or directories\n'
            
    def uname(self):
        return 'Linux'

    def pwd(self):
        return self.current_dir

class ShellGUI:
    def __init__(self, config):
        self.config = config
        self.file_system = FileSystem(self.config.tar_path)
        self.root = tk.Tk()
        self.root.title('Shell Emulator')

        self.output_frame = tk.Frame(self.root)
        self.output_frame.pack(fill=tk.BOTH, expand=True)

        self.output_text = tk.Text(self.output_frame, wrap=tk.WORD)
        self.output_text.pack(fill=tk.BOTH, expand=True)

        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(fill=tk.X)

        self.input_entry = tk.Entry(self.input_frame)
        self.input_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

        self.input_entry.insert(tk.END, f'${self.file_system.current_dir}>')

        self.input_entry.bind('<Return>', self.execute_command)

        self.output_text.insert(tk.END, f'Welcome to Shell Emulator\n')

        self.root.mainloop()

    def execute_command(self, event=None):
        command = self.input_entry.get().split('>')[1]
        self.history.append(command)
        self.history_index = len(self.history)
        self.input_entry.delete(0, tk.END)
        self.output_text.insert(tk.END, f'${self.file_system.current_dir}>{command}\n')

        if command.strip() == 'exit':
            self.root.destroy()
            exit(0)
        elif command.strip() == 'ls':
            files = self.file_system.ls()
            for file in files:
                self.output_text.insert(tk.END, f'{file}\n')
        elif command.startswith('cd'):
            if command.strip() == 'cd':
                self.output_text.insert(tk.END, f'No such files or directories\n')
            elif command[2] != ' ':
                self.output_text.insert(tk.END, 'Invalid command\n')
            else :
                path = command.split(' ')[1]
                self.output_text.insert(tk.END, f'{self.file_system.cd(path)}')
        elif command.strip() == 'uname':
            self.output_text.insert(tk.END, f'{self.file_system.uname()}\n')
        elif command.strip() == 'pwd':
            self.output_text.insert(tk.END, f'{self.file_system.pwd()}\n')
        else:
            self.output_text.insert(tk.END, 'Invalid command\n')

        self.input_entry.insert(tk.END, f'${self.file_system.current_dir}>')

if __name__ == '__main__':
    config = Config('config.xml')
    shell_gui = ShellGUI(config)
