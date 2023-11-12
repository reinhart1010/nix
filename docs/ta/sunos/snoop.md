---
layout: page
title: sunos/snoop (தமிழ்)
description: "நெட்வொர்க் பாக்கெட் ஸ்னிஃபர்."
content_hash: 5af44e61c86f65f2d6d8010e190994a31d6b525e
last_modified_at: 2023-11-12
related_topics:
  - title: বাংলা version
    url: /bn/sunos/snoop.html
    icon: bi bi-globe
  - title: English version
    url: /en/sunos/snoop.html
    icon: bi bi-globe
  - title: français version
    url: /fr/sunos/snoop.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/sunos/snoop.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/sunos/snoop.html
    icon: bi bi-globe
tldri18n_status: 2
---
# snoop

நெட்வொர்க் பாக்கெட் ஸ்னிஃபர்.
tcpdump சமமான SunOS.
மேலும் விவரத்திற்கு: <https://www.unix.com/man-page/sunos/1m/snoop>.

- ஒரு குறிப்பிட்ட பிணைய இடைமுகத்தில் பாக்கெட்டுகளைப் பிடிக்கவும்:

`snoop -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">e1000g0</span>

- கைப்பற்றப்பட்ட பாக்கெட்டுகளைக் காட்டுவதற்குப் பதிலாக ஒரு கோப்பில் சேமிக்கவும்:

`snoop -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்புப்_பெயர்</span>

- ஒரு கோப்பிலிருந்து பாக்கெட்டுகளின் வெர்போஸ் புரோட்டோகால் லேயர் சுருக்கத்தைக் காண்பி:

`snoop -V -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்புப்_பெயர்</span>

- ஹோஸ்ட்பெயரில் இருந்து வரும் நெட்வொர்க் பாக்கெட்டுகளைப் பிடித்து, கொடுக்கப்பட்ட போர்ட்டிற்குச் செல்லவும்:

`snoop to port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">போர்ட்</span>` from host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">புரவலன்_பெயர்</span>

- இரண்டு ஐபி முகவரிகளுக்கு இடையே பரிமாற்றம் செய்யப்பட்ட நெட்வொர்க் பாக்கெட்டுகளின் ஹெக்ஸ்-டம்ப்பைப் பிடித்துக் காட்டவும்:

`snoop -x0 -p4 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ஐபி_முகவரி_1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ஐபி_முகவரி_2</span>
