import sys
from pathlib import Path

from fastapi.testclient import TestClient

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from app import app, activities


def test_unregister_participant_removes_from_activity():
    client = TestClient(app)
    original_participants = activities["Chess Club"]["participants"][:]
    activities["Chess Club"]["participants"] = ["michael@mergington.edu"]

    try:
        response = client.delete(
            "/activities/Chess Club/participants/michael@mergington.edu"
        )

        assert response.status_code == 200
        assert "michael@mergington.edu" not in activities["Chess Club"]["participants"]
    finally:
        activities["Chess Club"]["participants"] = original_participants
