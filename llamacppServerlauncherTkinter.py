import sys
import os
import json
import subprocess
import webbrowser
import tkinter as tk
from tkinter import filedialog

CONFIG_FILE = 'llama_launcher_config.json'

class LlamaLauncherApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.config = self.loadConfig()
        self.initUI()

    def initUI(self):
        self.title('Llama.cpp Server Launcher')
        self.geometry('400x400')

        self.serverLabel = tk.Label(self, text='Server Executable:')
        self.serverLabel.pack()
        self.serverEntry = tk.Entry(self, width=40)
        self.serverEntry.insert(0, self.config.get('server_path', ''))
        self.serverEntry.pack()
        self.serverButton = tk.Button(self, text='Browse...', command=self.browseServer)
        self.serverButton.pack()

        self.modelLabel = tk.Label(self, text='Model:')
        self.modelLabel.pack()
        self.modelEntry = tk.Entry(self, width=40)
        self.modelEntry.insert(0, self.config.get('model_path', ''))
        self.modelEntry.pack()
        self.modelButton = tk.Button(self, text='Browse...', command=self.browseModel)
        self.modelButton.pack()

        self.threadsLabel = tk.Label(self, text='Threads (-t):')
        self.threadsLabel.pack()
        self.threadsEntry = tk.Entry(self, width=40)
        self.threadsEntry.insert(0, self.config.get('threads', '4'))
        self.threadsEntry.pack()

        self.portLabel = tk.Label(self, text='Port:')
        self.portLabel.pack()
        self.portEntry = tk.Entry(self, width=40)
        self.portEntry.insert(0, self.config.get('port', '8080'))
        self.portEntry.pack()

        self.nPredictLabel = tk.Label(self, text='Max Tokens to Generate (-n):')
        self.nPredictLabel.pack()
        self.nPredictEntry = tk.Entry(self, width=40)
        self.nPredictEntry.insert(0, self.config.get('n_predict', '512'))
        self.nPredictEntry.pack()

        self.nCtxLabel = tk.Label(self, text='Context Size (-c):')
        self.nCtxLabel.pack()
        self.nCtxEntry = tk.Entry(self, width=40)
        self.nCtxEntry.insert(0, self.config.get('n_ctx', '512'))
        self.nCtxEntry.pack()

        self.nGpuLayersLabel = tk.Label(self, text='GPU Layers (-ngl):')
        self.nGpuLayersLabel.pack()
        self.nGpuLayersEntry = tk.Entry(self, width=40)
        self.nGpuLayersEntry.insert(0, self.config.get('n_gpu_layers', '0'))
        self.nGpuLayersEntry.pack()

        self.launchButton = tk.Button(self, text='Launch Server', command=self.launchServer)
        self.launchButton.pack()

    def browseServer(self):
        fileName = filedialog.askopenfilename(title="Select Server Executable", filetypes=[("Executable Files", "*.exe")])
        if fileName:
            self.serverEntry.delete(0, tk.END)
            self.serverEntry.insert(0, fileName)
            self.config['server_path'] = fileName
            self.saveConfig()

    def browseModel(self):
        fileName = filedialog.askopenfilename(title="Select Model")
        if fileName:
            self.modelEntry.delete(0, tk.END)
            self.modelEntry.insert(0, fileName)
            self.config['model_path'] = fileName
            self.saveConfig()

    def launchServer(self):
        server = self.serverEntry.get()
        model = self.modelEntry.get()
        threads = self.threadsEntry.get()
        port = self.portEntry.get()
        n_predict = self.nPredictEntry.get()
        n_ctx = self.nCtxEntry.get()
        n_gpu_layers = self.nGpuLayersEntry.get()

        self.config['threads'] = threads
        self.config['port'] = port
        self.config['n_predict'] = n_predict
        self.config['n_ctx'] = n_ctx
        self.config['n_gpu_layers'] = n_gpu_layers
        self.saveConfig()

        command = f'"{server}" --model "{model}" --threads {threads} --port {port} -n {n_predict} -c {n_ctx} -ngl {n_gpu_layers}'
        subprocess.Popen(command, shell=True)

        # Open the browser with the specified URL
        url = f'http://127.0.0.1:{port}/'
        webbrowser.open(url)

    def loadConfig(self):
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, 'r') as f:
                return json.load(f)
        else:
            return {}

    def saveConfig(self):
        with open(CONFIG_FILE, 'w') as f:
            json.dump(self.config, f)

if __name__ == '__main__':
    app = LlamaLauncherApp()
    app.mainloop()