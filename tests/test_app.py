from app import compare_resume

def test_matches_terms():
    assert 'python' in compare_resume('Python developer', 'Python AI engineer')['matched_terms']
