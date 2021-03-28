import json
from datetime import date
f = open('paw.json')
st = f.read()
output_st = ''
Ls = []
for _st in st.split('\n'):
    if len(_st) < 2:
        continue
    obj = json.loads(_st)
    _time = date.fromtimestamp(obj['create_time']).isoformat()
    url = obj['link']
    title = obj['title']
    max_title_length = 40
    if len(title) > max_title_length:
        title = title[:max_title_length]
    Ls.append([_time, title, url])
Ls.sort(key=lambda x:x[0], reverse=True)
for item in Ls:
    _time, title, url = item
    format_str = '* [{0}-{1}]({2}) \n'.format(_time, title, url)
    output_st += format_str
open('paw.md', 'w').write(output_st)