---
layout: page
title: common/htop (தமிழ்)
description: "இயங்கும் செயல்முறைகளைப் பற்றிய டைனமிக் நிகழ்நேர தகவலைக் காண்பி. `top` இன் மேம்படுத்தப்பட்ட பதிப்பு."
content_hash: 037dbb1934bb1204815363449579466bb7b619ac
last_modified_at: 2024-07-26
related_topics:
  - title: English version
    url: /en/common/htop.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/htop.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/htop.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/htop.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/htop.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/htop.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/htop.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># htop

இயங்கும் செயல்முறைகளைப் பற்றிய டைனமிக் நிகழ்நேர தகவலைக் காண்பி. `top` இன் மேம்படுத்தப்பட்ட பதிப்பு.
மேலும் விவரத்திற்கு: <https://htop.dev/>.

- htop ஐத் தொடங்கவும்:

`htop`

- ஒரு குறிப்பிட்ட பயனருக்குச் சொந்தமான htop காட்சி செயல்முறைகளைத் தொடங்கவும்:

`htop --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பயனர்பெயர்</span>

- குறிப்பிட்ட `sort_item` (வரிசை உருப்படி) மூலம் செயல்முறைகளை வரிசைப்படுத்தவும் (கிடைக்கும் விருப்பங்களுக்கு `htop --sort help` ஐப் பயன்படுத்தவும்):

`htop --sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sort_item</span>

- ஒரு நொடியில் பத்தில் ஒரு பங்கு (அதாவது 50 = 5 வினாடிகளில்) புதுப்பிப்புகளுக்கு இடையே குறிப்பிட்ட தாமதத்துடன் `htop` ஐத் தொடங்கவும்:

`htop --delay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50</span>

- htop ஐ இயக்கும்போது ஊடாடும் கட்டளைகளைப் பார்க்கவும்:

`?`

- வேறு தாவலுக்கு மாறவும்:

`tab`

- உதவியைக் காட்டு:

`htop --help`
