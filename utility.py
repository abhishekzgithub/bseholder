import requests
from lxml import html
def check_availability(r,tree):
    status=True
    r_status=r.status_code
    tree = html.fromstring(r.content)
    empty=(tree.xpath("//td[contains(text(),'Category of shareholder')]/text()"))
    if r_status in (404,'404') and empty=='Category of shareholder':
        status=False
    return status