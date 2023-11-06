---
layout: page
title: common/cat (नेपाली)
description: "फाइलहरू देखाउनुहोस् र जोड्नुहोस्।"
content_hash: d9c227d868384971c06f94b70b47d2b906531df0
last_modified_at: 2023-11-06
related_topics:
  - title: Deutsch version
    url: /de/common/cat.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/cat.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/cat.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/cat.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/cat.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/cat.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/cat.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/cat.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/cat.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cat.html
    icon: bi bi-globe
  - title: norsk version
    url: /no/common/cat.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/cat.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/cat.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/cat.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/cat.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/cat.html
    icon: bi bi-globe
---
# cat

फाइलहरू देखाउनुहोस् र जोड्नुहोस्।
थप जानकारी: <https://www.gnu.org/software/coreutils/cat>।

- फाइल भित्रका कुराहरुलाई मानक आउटपुटमा देखाउनुहोस्:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फाइल/को/पथ</span>

- धेरै फाइलहरू जोडेर एउटा सिंगो आउटपुट फाइल बनाउनुहोस्:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फाइल_पहिलो/को/पथ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फाइल_दोस्रो/को/पथ</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">आउटपुट/फाइल/को/पथ</span>

- धेरै फाइलहरू जोडेर एउटा सिंगो आउटपुट फाइलमा संलग्न गर्नुहोस्:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फाइल_पहिलो/को/पथ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फाइल_दोस्रो/को/पथ</span>` >> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">आउटपुट/फाइल/को/पथ</span>

- सबै आउटपुट लाइनहरूलाइ संख्यामा देखाउनुहोस:

`cat -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फाइल/को/पथ</span>

- छाप्न नमिल्ने र सेतो खाली ठाँउका वर्णहरू देखाउनुहोस् (यदि ASCII हैनन् भने `M-` उपसर्ग लागेर देखिन्छ):

`cat -v -t -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फाइल/को/पथ</span>
