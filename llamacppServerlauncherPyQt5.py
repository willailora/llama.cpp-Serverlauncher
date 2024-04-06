import sys
import os
import json
import subprocess
import webbrowser
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFileDialog

CONFIG_FILE = 'llama_launcher_config.json'

class LlamaLauncherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.config = self.loadConfig()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Llama.cpp Server Launcher')
        self.setGeometry(100, 100, 400, 400)

        layout = QVBoxLayout()

        self.serverLabel = QLabel('Server Executable:')
        self.serverLineEdit = QLineEdit(self.config.get('server_path', ''))
        self.serverButton = QPushButton('Browse...')
        self.serverButton.clicked.connect(self.browseServer)
        layout.addWidget(self.serverLabel)
        layout.addWidget(self.serverLineEdit)
        layout.addWidget(self.serverButton)

        self.modelLabel = QLabel('Model:')
        self.modelLineEdit = QLineEdit(self.config.get('model_path', ''))
        self.modelButton = QPushButton('Browse...')
        self.modelButton.clicked.connect(self.browseModel)
        layout.addWidget(self.modelLabel)
        layout.addWidget(self.modelLineEdit)
        layout.addWidget(self.modelButton)

        self.threadsLabel = QLabel('Threads (-t):')
        self.threadsLineEdit = QLineEdit(self.config.get('threads', '4'))
        layout.addWidget(self.threadsLabel)
        layout.addWidget(self.threadsLineEdit)

        self.portLabel = QLabel('Port:')
        self.portLineEdit = QLineEdit(self.config.get('port', '8080'))
        layout.addWidget(self.portLabel)
        layout.addWidget(self.portLineEdit)

        self.nPredictLabel = QLabel('Max Tokens to Generate (-n):')
        self.nPredictLineEdit = QLineEdit(self.config.get('n_predict', '512'))
        layout.addWidget(self.nPredictLabel)
        layout.addWidget(self.nPredictLineEdit)

        self.nCtxLabel = QLabel('Context Size (-c):')
        self.nCtxLineEdit = QLineEdit(self.config.get('n_ctx', '512'))
        layout.addWidget(self.nCtxLabel)
        layout.addWidget(self.nCtxLineEdit)

        self.nGpuLayersLabel = QLabel('GPU Layers (-ngl):')
        self.nGpuLayersLineEdit = QLineEdit(self.config.get('n_gpu_layers', '0'))
        layout.addWidget(self.nGpuLayersLabel)
        layout.addWidget(self.nGpuLayersLineEdit)

        self.launchButton = QPushButton('Launch Server')
        self.launchButton.clicked.connect(self.launchServer)
        layout.addWidget(self.launchButton)

        self.setLayout(layout)

    def browseServer(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Select Server Executable", "", "Executable Files (*.exe)", options=options)
        if fileName:
            self.serverLineEdit.setText(fileName)
            self.config['server_path'] = fileName
            self.saveConfig()

    def browseModel(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Select Model", "", "All Files (*)", options=options)
        if fileName:
            self.modelLineEdit.setText(fileName)
            self.config['model_path'] = fileName
            self.saveConfig()

    def launchServer(self):
        server = self.serverLineEdit.text()
        model = self.modelLineEdit.text()
        threads = self.threadsLineEdit.text()
        port = self.portLineEdit.text()
        n_predict = self.nPredictLineEdit.text()
        n_ctx = self.nCtxLineEdit.text()
        n_gpu_layers = self.nGpuLayersLineEdit.text()

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
    app = QApplication(sys.argv)
    launcher = LlamaLauncherApp()
    launcher.show()
    sys.exit(app.exec_())


