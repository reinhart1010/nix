---
layout: page
title: common/g++ (தமிழ்)
description: "C++ மூலக் கோப்புகளைத் தொகுக்கிறது."
content_hash: 15b7c1836752e8ab1480fcbac504ae113eaf481b
last_modified_at: 2024-09-24
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
  - title: 한국어 version
    url: /ko/common/g++.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/g++.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># g++

C++ மூலக் கோப்புகளைத் தொகுக்கிறது.
GCC இன் பகுதி (GNU கம்பைலர் சேகரிப்பு).
மேலும் விவரத்திற்கு: <https://gcc.gnu.org>.

- இயங்கக்கூடிய பைனரியில் ஒரு மூலக் குறியீடு கோப்பை தொகுக்கவும்:

`g++ `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">மூலம்.cpp/பாதை</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">வெளியீடு_இயங்கக்கூடியது/பாதை</span>

- அனைத்து பிழைகள் மற்றும் எச்சரிக்கைகள் (கிட்டத்தட்ட) காட்சி:

`g++ `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">மூலம்.cpp/பாதை</span>` -Wall -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">வெளியீடு_இயங்கக்கூடியது/பாதை</span>

- (C++98/C++11/C++14/C++17) தொகுக்க ஒரு மொழித் தரத்தைத் தேர்வு செய்யவும்:

`g++ `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">மூலம்.cpp/பாதை</span>` -std=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">c++98|c++11|c++14|c++17</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">வெளியீடு_இயங்கக்கூடியது/பாதை</span>

- மூலக் கோப்பை விட வேறு பாதையில் அமைந்துள்ள நூலகங்களைச் சேர்க்கவும்:

`g++ `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">மூலம்.cpp/பாதை</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">வெளியீடு_இயங்கக்கூடியது/பாதை</span>` -I`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">தலைப்பு/பாதை</span>` -L`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நூலகம்/பாதை</span>` -l`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நூலகம்_பெயர்</span>

- பல மூலக் குறியீடு கோப்புகளை ஒரு இயங்கக்கூடிய பைனரியில் தொகுத்து இணைக்கவும்:

`g++ -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">மூலம்_1.cpp/பாதை மூலம்_2.cpp/பாதை ...</span>` && g++ -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">வெளியீடு_செயல்படுத்தக்கூடியது/பாதை</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">மூலம்_1.o/பாதை மூலம்_2.o/பாதை ...</span>

- செயல்திறனுக்காக தொகுக்கப்பட்ட நிரலை மேம்படுத்தவும்:

`g++ `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">மூலம்.cpp/பாதை</span>` -O`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|2|3|fast</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">வெளியீடு_இயங்கக்கூடியது/பாதை</span>

- பதிப்பைக் காட்டு:

`g++ --version`
