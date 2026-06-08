def test_stats_without_dataset_returns_404(client):

    response = client.get("/data/stats")

    assert response.status_code == 404