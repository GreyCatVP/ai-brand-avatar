import os
import yaml
from pathlib import Path

class AvatarAgent:
    def __init__(self):
        self.role = "pr"
        self.cfg_path = Path("brand_core/brand.yaml")
        self.config = self._load_yaml()

    def _load_yaml(self):
        with open(self.cfg_path, encoding="utf-8") as f:
            return yaml.safe_load(f)

    def set_role(self, role: str):
        self.role = role

    def chat(self, user_input: str) -> str:
        # здесь будет вызов router-chain (следующий файл)
        return f"[{self.role}] {user_input} → ответ в стиле {self.config['name']}"
