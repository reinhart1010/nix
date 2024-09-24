---
layout: page
title: common/gcc (தமிழ்)
description: "C மற்றும் C++ மூலக் கோப்புகளை முன் செயலாக்கம் செய்து தொகுத்து, பின்னர் அவற்றைச் சேகரித்து இணைக்கவும்."
content_hash: cf7f724df05971702a5113bb7ddadb8a302bedc0
last_modified_at: 2024-09-24
related_topics:
  - title: Deutsch version
    url: /de/common/gcc.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/gcc.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/gcc.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/gcc.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/gcc.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/gcc.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/gcc.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># gcc

C மற்றும் C++ மூலக் கோப்புகளை முன் செயலாக்கம் செய்து தொகுத்து, பின்னர் அவற்றைச் சேகரித்து இணைக்கவும்.
மேலும் விவரத்திற்கு: <https://gcc.gnu.org>.

- பல மூல கோப்புகளை இயங்கக்கூடியதாக தொகுக்கவும்:

`gcc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">மூலம்1.c/பாதை மூலம்2.c/பாதை ...</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">வெளியீடு_இயங்கக்கூடியது/பாதை</span>

- வெளியீட்டில் எச்சரிக்கைகள் மற்றும் பிழைத்திருத்த குறியீடுகளை அனுமதிக்கவும்:

`gcc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">மூலம்.c/பாதை</span>` -Wall -g -Og -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">வெளியீடு_இயங்கக்கூடியது/பாதை</span>

- வேறு பாதையிலிருந்து நூலகங்களைச் சேர்க்கவும்:

`gcc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">மூலம்.c/பாதை</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">வெளியீடு_இயங்கக்கூடியது/பாதை</span>` -I`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">தலைப்பு</span>` -L`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நூலகத்திற்கு/பாதை</span>` -l`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நூலகம்_பெயர்</span>

- மூலக் குறியீட்டை அசெம்பிளர் வழிமுறைகளில் தொகுக்கவும்:

`gcc -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">மூலம்.c/பாதை</span>

- இணைக்காமல் மூலக் குறியீட்டை தொகுக்கவும்:

`gcc -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">மூலம்.c/பாதை</span>

- செயல்திறனுக்காக தொகுக்கப்பட்ட நிரலை மேம்படுத்தவும்:

`gcc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">மூலம்.c/பாதை</span>` -O`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|2|3|fast</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">வெளியீடு_இயங்கக்கூடியது/பாதை</span>
