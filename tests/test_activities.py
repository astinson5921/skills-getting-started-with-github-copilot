import src.app as appmodule

# Arrange-Act-Assert style tests

def test_get_activities(client):
    # Arrange
    # Act
    resp = client.get('/activities')
    # Assert
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, dict)
    assert 'Chess Club' in data

def test_signup_success(client):
    # Arrange
    activity = 'Chess Club'
    email = 'newstudent@mergington.edu'
    # Act
    resp = client.post(f"/activities/{activity}/signup?email={email}")
    # Assert
    assert resp.status_code == 200
    assert email in resp.json().get('message', '')
    assert email in appmodule.activities[activity]['participants']

def test_signup_duplicate(client):
    # Arrange
    activity = 'Chess Club'
    email = 'michael@mergington.edu'
    # Act
    resp = client.post(f"/activities/{activity}/signup?email={email}")
    # Assert
    assert resp.status_code == 400

def test_signup_activity_not_found(client):
    # Arrange
    activity = 'Nonexistent'
    email = 'nobody@mergington.edu'
    # Act
    resp = client.post(f"/activities/{activity}/signup?email={email}")
    # Assert
    assert resp.status_code == 404

def test_unregister_success(client):
    # Arrange
    activity = 'Chess Club'
    email = 'daniel@mergington.edu'
    # Act
    resp = client.delete(f"/activities/{activity}/participants?email={email}")
    # Assert
    assert resp.status_code == 200
    assert email not in appmodule.activities[activity]['participants']

def test_unregister_not_found(client):
    # Arrange
    activity = 'Chess Club'
    email = 'notfound@mergington.edu'
    # Act
    resp = client.delete(f"/activities/{activity}/participants?email={email}")
    # Assert
    assert resp.status_code == 404
