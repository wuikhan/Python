import re
from linkGrabber import Links

links = linkGrabber.Links('http://google.com')
gb = links.find(limit=4,duplicates=False,pretty=True)
print(gb)