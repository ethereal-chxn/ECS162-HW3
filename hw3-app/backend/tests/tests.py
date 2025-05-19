# Unit test code written with consultation of https://www.digitalocean.com/community/tutorials/unit-test-in-flask
import sys
import os
import pytest
import requests
from dotenv import load_dotenv
from app import app

load_dotenv()

# Creates instance of client that will call flask backend server
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

'''API Key'''
# Check Flask server returns your API key as expected
def test_key(client):
    response = client.get("/api/key")
    assert response.json == {'apiKey': os.getenv('NYT_API_KEY')}

'''NYT API'''
# Check API returns data in expected format (title, article_url, multimedia, abstract, etc)
def test_nyt_info():
    api_key = os.getenv('NYT_API_KEY')
    url = f"https://api.nytimes.com/svc/search/v2/articlesearch.json?q=(Sacramento,Davis)&sort=newest&api-key={api_key}"
    response = requests.get(url); 

    # Check that HTTP request is valid
    assert response.status_code == 200
    
    articles = response.json()["response"]["docs"]
    for article in articles:
        assert "headline" in article
        assert "multimedia" in article
        assert "abstract" in article
        assert "web_url" in article

# Check that query is correct (Davis or Sacramento news)
# Websites consulted:
# https://www.geeksforgeeks.org/python-program-to-extract-a-single-value-from-json-response/
def test_nyt_query():
    api_key = os.getenv('NYT_API_KEY')
    url = f"https://api.nytimes.com/svc/search/v2/articlesearch.json?q=(Sacramento,Davis)&sort=newest&api-key={api_key}"
    response = requests.get(url); 

    assert response.status_code == 200
    
    articles = response.json()["response"]["docs"]
    for article in articles:
        keywords = article["keywords"]
        for keyword in keywords:
            if keyword["name"] != "Location":
                continue
            if keyword["value"] != "Sacramento, (Calif)" or keyword["value"] != "Davis, (Calif)":
                continue
            assert (('Location', 'Sacramento, (Calif)') in keyword.items()) or (('Location', 'Davis, (Calif)') in keyword.items())