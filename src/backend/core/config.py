import json
import os
from cryptography.fernet import Fernet

class Config:
    def __init__(self):
        self.servers = {}
        self.encryption_key = Fernet.generate_key()
        self.cipher = Fernet(self.encryption_key)
        self.tor_enabled = False
        self.matrix_servers = []
        self.load_config()

    def load_config(self):
        if os.path.exists("config.json"):
            with open("config.json", "r") as f:
                data = json.load(f)
                self.servers = data.get("servers", {})
                self.tor_enabled = data.get("tor_enabled", False)
                self.matrix_servers = data.get("matrix_servers", [])

    def save_config(self):
        with open("config.json", "w") as f:
            json.dump({
                "servers": self.servers,
                "tor_enabled": self.tor_enabled,
                "matrix_servers": self.matrix_servers
            }, f)
