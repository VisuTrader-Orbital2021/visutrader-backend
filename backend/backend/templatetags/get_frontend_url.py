import re
import os

from django import template
register = template.Library()

@register.filter
def get_frontend_url ( url ): 
    backendBaseUrl = 'http://localhost:8000' if os.environ['ENV'] == 'development' else 'https://visutrader-backend.herokuapp.com'
    frontendBaseUrl = 'http://localhost:3000' if os.environ['ENV'] == 'development' else 'https://visutrader.netlify.app'

    regex = re.compile(backendBaseUrl + '/accounts/password/reset/confirm/([0-9A-Za-z_\-]+)/([0-9A-Za-z]{1,13}-[0-9A-Za-z]+)/')
    matched = regex.match(url)
    uid = matched.group(1)
    token = matched.group(2)
    return frontendBaseUrl + '/forgot-password/' + uid + '/' + token