---
layout: page
title: linux/toolbox-rmi (தமிழ்)
description: "ஒன்று அல்லது அதற்கு மேற்பட்ட `toolbox` படங்களை அகற்றவும்."
content_hash: 5f435eb7927346a66301259d839f00daa7ff7037
related_topics:
  - title: English version
    url: /en/linux/toolbox-rmi.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># toolbox rmi

ஒன்று அல்லது அதற்கு மேற்பட்ட `toolbox` படங்களை அகற்றவும்.
மேலும் பார்க்கவும்: `toolbox rm`.
மேலும் விவரத்திற்கு: <https://manned.org/toolbox-rmi.1>.

- `toolbox` படத்தை அகற்றவும்:

`toolbox rmi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">படம்_பெயர்</span>

- அனைத்து `toolbox` படங்களையும் அகற்றவும்:

`toolbox rmi --all`

- தற்போது கன்டெய்னரால் பயன்படுத்தப்படும் `toolbox` படத்தை அகற்றுமாறு கட்டாயப்படுத்துங்கள் (கண்டெய்னரும் அகற்றப்படும்):

`toolbox rmi --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">படம்_பெயர்</span>
