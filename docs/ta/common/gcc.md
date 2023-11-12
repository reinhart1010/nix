---
layout: page
title: common/gcc (தமிழ்)
description: "C மற்றும் C++ மூலக் கோப்புகளை முன் செயலாக்கம் செய்து தொகுத்து, பின்னர் அவற்றைச் சேகரித்து இணைக்கவும்."
content_hash: b312cdec018256b8a7b48e58b17edfbdd3d2328c
last_modified_at: 2023-11-12
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
  - title: português (Brasil) version
    url: /pt_BR/common/gcc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gcc

C மற்றும் C++ மூலக் கோப்புகளை முன் செயலாக்கம் செய்து தொகுத்து, பின்னர் அவற்றைச் சேகரித்து இணைக்கவும்.
மேலும் விவரத்திற்கு: <https://gcc.gnu.org>.

- பல மூல கோப்புகளை இயங்கக்கூடியதாக தொகுக்கவும்:

`gcc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/மூல1.c பாதை/டு/மூல2.c ...</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/வெளியீடு_இயங்கக்கூடியது</span>

- வெளியீட்டில் எச்சரிக்கைகள் மற்றும் பிழைத்திருத்த குறியீடுகளை அனுமதிக்கவும்:

`gcc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/மூல.c</span>` -Wall -Og --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/வெளியீடு_இயங்கக்கூடியது</span>

- வேறு பாதையிலிருந்து நூலகங்களைச் சேர்க்கவும்:

`gcc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/மூல.c</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/வெளியீடு_இயங்கக்கூடியது</span>` -I`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/தலைப்பு</span>` -L`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/நூலகத்திற்கு</span>` -l`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நூலகம்_பெயர்</span>

- மூலக் குறியீட்டை அசெம்பிளர் வழிமுறைகளில் தொகுக்கவும்:

`gcc -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/மூல.c</span>

- இணைக்காமல் மூலக் குறியீட்டை தொகுக்கவும்:

`gcc -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/மூல.c</span>
