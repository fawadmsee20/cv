import urllib.request, re, json
req = urllib.request.Request('https://scholar.google.com/citations?hl=en&user=_I-hc5YAAAAJ&view_op=list_works&pagesize=100', headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read().decode('utf-8')
trs = re.findall(r'<tr class="gsc_a_tr">.*?</tr>', html)
res = []
for tr in trs:
    title = re.search(r'class="gsc_a_at">([^<]+)', tr).group(1) if re.search(r'class="gsc_a_at">([^<]+)', tr) else ''
    authors = re.search(r'<div class="gs_gray">([^<]+)', tr).group(1) if re.search(r'<div class="gs_gray">([^<]+)', tr) else ''
    venue_m = re.findall(r'<div class="gs_gray">.*?</div><div class="gs_gray">([^<]+)', tr)
    venue = venue_m[0] if venue_m else ''
    year_m = re.findall(r'<span class="gsc_a_h gsc_a_hc gs_ibl">([^<]+)', tr)
    year = year_m[0] if year_m else ''
    res.append({'title': title, 'authors': authors, 'venue': venue, 'year': year})
print(json.dumps(res, indent=2))
