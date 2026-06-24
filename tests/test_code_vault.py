from code_vault import CodeVault, Project

def test_add_project():
    vault = CodeVault()
    project = Project("Test Project", "Test Code", "pending")
    vault.add_project(project)
    assert len(vault.get_projects()) == 1

def test_get_projects():
    vault = CodeVault()
    project1 = Project("Test Project 1", "Test Code 1", "pending")
    project2 = Project("Test Project 2", "Test Code 2", "pending")
    vault.add_project(project1)
    vault.add_project(project2)
    projects = vault.get_projects()
    assert len(projects) == 2
    assert projects[0].name == "Test Project 1"
    assert projects[1].name == "Test Project 2"

def test_view_code():
    vault = CodeVault()
    project = Project("Test Project", "Test Code", "pending")
    vault.add_project(project)
    code = vault.view_code("Test Project")
    assert code == "Test Code"

def test_download_code():
    vault = CodeVault()
    project = Project("Test Project", "Test Code", "pending")
    vault.add_project(project)
    code = vault.download_code("Test Project")
    assert code == "Test Code"

def test_download_code_not_found():
    vault = CodeVault()
    try:
        vault.download_code("Non-existent Project")
        assert False
    except ValueError as e:
        assert str(e) == "Project not found"

def test_confirm_payment():
    vault = CodeVault()
    project = Project("Test Project", "Test Code", "pending")
    vault.add_project(project)
    result = vault.confirm_payment("Test Project")
    assert result
    assert project.payment_status == "paid"

def test_confirm_payment_not_found():
    vault = CodeVault()
    result = vault.confirm_payment("Non-existent Project")
    assert not result
