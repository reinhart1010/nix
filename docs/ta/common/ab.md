---
layout: page
title: common/ab (தமிழ்)
description: "அப்பாச்சி HTTP சர்வர் தரப்படுத்தல் கருவி."
content_hash: b4445dc3bc86b1543a8194ef06becfb07c8774e5
last_modified_at: 2024-01-25
related_topics:
  - title: বাংলা version
    url: /bn/common/ab.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/common/ab.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ab.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ab.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ab.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/ab.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ab.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/ab.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ab.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ab.html
    icon: bi bi-globe
  - title: norsk version
    url: /no/common/ab.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ab.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/ab.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ab.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ab

அப்பாச்சி HTTP சர்வர் தரப்படுத்தல் கருவி.
மேலும் விவரத்திற்கு: <https://httpd.apache.org/docs/current/programs/ab.html>.

- கொடுக்கப்பட்ட முகவரிக்கு 100 HTTP GET கோரிக்கைகளை இயக்கவும்:

`ab -n 100 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">முகவரி</span>

- 100 HTTP GET கோரிக்கைகளை, ஒரே நேரத்தில் 10 தொகுதிகளில், URL முகவரிக்கு செயல்படுத்தவும்:

`ab -n 100 -c 10 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">முகவரி</span>

- ஒரு கோப்பிலிருந்து JSON பேலோடைப் பயன்படுத்தி, 100 HTTP POST கோரிக்கைகளை URL க்கு செயல்படுத்தவும்:

`ab -n 100 -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">application/json</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு.json/பாதை</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">முகவரி</span>

- HTTP [K]eep Alive ஐப் பயன்படுத்தவும், அதாவது ஒரு HTTP அமர்வுக்குள் பல கோரிக்கைகளைச் செய்யவும்:

`ab -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">முகவரி</span>

- தரப்படுத்தலுக்கு செலவிட வேண்டிய அதிகபட்ச வினாடிகளை அமைக்கவும்:

`ab -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">60</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">முகவரி</span>

- முடிவுகளை ஒரு CSV கோப்பில் எழுதவும்:

`ab -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு.csv/பாதை</span>
