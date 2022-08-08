---
layout: page
title: common/g++ (தமிழ்)
description: "C++ மூலக் கோப்புகளைத் தொகுக்கிறது."
content_hash: 546cd6bd66ba36f7b4793ed9a51ee55daa0fbcb7
related_topics:
  - title: Deutsch version
    url: /de/common/g++.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/g++.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/g++.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/g++.html
    icon: bi bi-globe
---
# g++

C++ மூலக் கோப்புகளைத் தொகுக்கிறது.
GCC இன் பகுதி (GNU கம்பைலர் சேகரிப்பு).
மேலும் விவரத்திற்கு: <https://gcc.gnu.org>.

- இயங்கக்கூடிய பைனரியில் ஒரு மூலக் குறியீடு கோப்பை தொகுக்கவும்:

`g++ `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/மூல.c</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/வெளியீடு_இயங்கக்கூடியது</span>

- அனைத்து பிழைகள் மற்றும் எச்சரிக்கைகள் (கிட்டத்தட்ட) காட்சி:

`g++ `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/மூல.c</span>` -Wall -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/வெளியீடு_இயங்கக்கூடியது</span>

- (C++98/C++11/C++14/C++17) தொகுக்க ஒரு மொழித் தரத்தைத் தேர்வு செய்யவும்:

`g++ `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/மூல.c</span>` -std=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">c++98|c++11|c++14|c++17</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/வெளியீடு_இயங்கக்கூடியது</span>

- மூலக் கோப்பை விட வேறு பாதையில் அமைந்துள்ள நூலகங்களைச் சேர்க்கவும்:

`g++ `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை /டு/மூல.c</span>` -o {பாதை/டு/வெளியீடு_இயங்கக்கூடியது</span>` -I`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/தலைப்பு</span>` -L`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/நூலகம்</span>` -l`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நூலகம்_பெயர்</span>
