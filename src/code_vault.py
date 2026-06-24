import json
from dataclasses import dataclass
from typing import List

@dataclass
class Project:
    name: str
    code: str
    payment_status: str

class CodeVault:
    def __init__(self):
        self.projects = []

    def add_project(self, project: Project):
        self.projects.append(project)

    def get_projects(self) -> List[Project]:
        return self.projects

    def view_code(self, project_name: str) -> str:
        for project in self.projects:
            if project.name == project_name:
                return project.code
        return None

    def download_code(self, project_name: str) -> str:
        code = self.view_code(project_name)
        if code:
            return code
        else:
            raise ValueError("Project not found")

    def confirm_payment(self, project_name: str) -> bool:
        for project in self.projects:
            if project.name == project_name:
                project.payment_status = "paid"
                return True
        return False
