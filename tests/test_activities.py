def test_get_all_activities(client, reset_activities):
    """Test retrieving all activities"""
    # Arrange
    expected_activities = ["Chess Club", "Programming Class", "Gym Class", 
                         "Basketball Team", "Tennis Club", "Drama Club", 
                         "Art Studio", "Debate Team", "Robotics Club"]
    
    # Act
    response = client.get("/activities")
    
    # Assert
    assert response.status_code == 200
    data = response.json()
    for activity in expected_activities:
        assert activity in data
        assert "description" in data[activity]
        assert "schedule" in data[activity]
        assert "max_participants" in data[activity]
        assert "participants" in data[activity]


def test_get_activities_returns_correct_structure(client, reset_activities):
    """Test that activity data has the correct structure"""
    # Arrange
    activity_name = "Chess Club"
    
    # Act
    response = client.get("/activities")
    
    # Assert
    assert response.status_code == 200
    data = response.json()
    activity = data[activity_name]
    assert isinstance(activity["description"], str)
    assert isinstance(activity["schedule"], str)
    assert isinstance(activity["max_participants"], int)
    assert isinstance(activity["participants"], list)
