---
layout: page
title: sunos/svccfg (தமிழ்)
description: "சேவை உள்ளமைவுகளை இறக்குமதி செய்யவும், ஏற்றுமதி செய்யவும் மற்றும் மாற்றவும்."
content_hash: e92e4805e9bb3b95201f5a137ef184d4c3fa798d
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/sunos/svccfg.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/sunos/svccfg.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/sunos/svccfg.html
    icon: bi bi-globe
tldri18n_status: 2
---
# svccfg

சேவை உள்ளமைவுகளை இறக்குமதி செய்யவும், ஏற்றுமதி செய்யவும் மற்றும் மாற்றவும்.
மேலும் விவரத்திற்கு: <https://www.unix.com/man-page/linux/1m/svccfg>.

- உள்ளமைவு கோப்பை சரிபார்க்கவும்:

`svccfg validate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">smf.xml</span>

- கோப்பிற்கு சேவை உள்ளமைவுகளை ஏற்றுமதி செய்யவும்:

`svccfg export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">சேவை_பெயர்</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">smf.xml</span>

- கோப்பிலிருந்து சேவை உள்ளமைவுகளை இறக்குமதி/புதுப்பித்தல்:

`svccfg import `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">smf.xml</span>
