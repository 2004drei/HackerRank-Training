import requests
import pytest

# 1. CONFIGURATION (The "Address" of the patient)
# If you run this locally, it's localhost. In a CI/CD pipeline, this would be a staging URL.
BASE_URL = "http://localhost:5000"

# 2. TEST 1: Check if the Homepage is alive
def test_homepage():
    # Act: Send a GET request to the root "/"
    response = requests.get(f"{BASE_URL}/")
    
    # Assert (Diagnosis): Check if the doctor got a response
    assert response.status_code == 200, "Homepage didn't load!"
    
    # Assert: Check if the response contains the welcome message
    data = response.json()
    assert "message" in data, "Welcome message missing!"
    assert data["message"] == "Welcome to the Health Check API", "Wrong welcome message!"
    print("✅ Homepage test passed!")

# 3. TEST 2: Check the Health Endpoint (The "Temperature" Check)
def test_health():
    response = requests.get(f"{BASE_URL}/health")
    
    # Check HTTP status
    assert response.status_code == 200, "Health endpoint is down!"
    
    data = response.json()
    # Check the content
    assert data["status"] == "healthy", f"Expected 'healthy' but got {data['status']}"
    assert "timestamp" in data, "Timestamp missing from health check!"
    
    print("✅ Health check passed!")

# 4. TEST 3: Check the Info Endpoint (The "Identity" Check)
def test_info():
    response = requests.get(f"{BASE_URL}/info")
    
    assert response.status_code == 200, "Info endpoint is down!"
    
    data = response.json()
    # In Docker, the hostname is usually the container ID
    assert "hostname" in data, "Hostname missing!"
    assert "python_version" in data, "Python version missing!"
    
    print(f"✅ Info check passed. Hostname is: {data['hostname']}")

# 5. BONUS: How to run this script directly (not mandatory for pytest)
if __name__ == "__main__":
    # This allows you to run `python test_api.py` as a quick sanity check
    test_homepage()
    test_health()
    test_info()
    print("🎉 All tests passed successfully!")