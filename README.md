# Code Vault

A simple project management system for freelance software consultants.

## Features

* Manage escrowed projects with relevant details
* View and download escrowed code
* Confirm payment for projects

## Usage

1. Create a new project: `project = Project("Test Project", "Test Code", "pending")`
2. Add the project to the code vault: `vault.add_project(project)`
3. View the project code: `vault.view_code("Test Project")`
4. Download the project code: `vault.download_code("Test Project")`
5. Confirm payment for the project: `vault.confirm_payment("Test Project")`
