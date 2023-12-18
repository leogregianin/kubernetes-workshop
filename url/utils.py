
def valid_url(url):
    """Check if the URL is valid."""
    if not url.startswith('http'):
        return f'http://{url}'
    return url
