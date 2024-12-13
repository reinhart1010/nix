---
layout: page
title: common/cp (नेपाली)
description: "फाइलहरू र डिरेक्टोरीहरू सार्नुहोस।"
content_hash: d2860977afdfb546da03a19328c48b212674cf31
last_modified_at: 2024-12-13
related_topics:
  - title: català version
    url: /ca/common/cp.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/common/cp.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/cp.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/cp.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/cp.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/cp.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/cp.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/cp.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/cp.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/cp.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cp.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/cp.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/cp.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/cp.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/cp.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/cp.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/cp.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/cp.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># cp

फाइलहरू र डिरेक्टोरीहरू सार्नुहोस।
थप जानकारी: <https://www.gnu.org/software/coreutils/manual/html_node/cp-invocation.html>।

- एउटा स्थान बाट अर्को स्थानमा फाइलहरु सार्नुहोस:

`cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">स्रोत_फाइल.ext/को/पथ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">लक्ष्य_फाइल.ext/को/पथ</span>

- फाइलको नाम उही राखेर अर्को डिरेक्टोरीमा फाइलहरु सार्नुहोस:

`cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">स्रोत_फाइल.ext/को/पथ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">लक्षित_अभिभावक_निर्देशिका/को/पथ</span>

- पुनरावर्ती रूपमा डिरेक्टोरीमा भएका सबै चीजहरुलाइ अर्को स्थानमा सार्नुहोस(यदि स्थान पहिले देखि नै छ भने,डिरेक्टोरी भित्र सार्नुहोस):

`cp -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">स्रोत_निर्देशिका/को/पथ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">लक्ष्य_निर्देशिका/को/पथ</span>

- पुनरावर्ती रूपमा एउटा डाइरेक्टरी सार्नुहोस, शब्दमय रुपमा (फाइलहरु सार्दा सार्दै सरिरहेको पनि देखिन्छ):

`cp -vR `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">स्रोत_निर्देशिका/को/पथ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">लक्ष्य_निर्देशिका/को/पथ</span>

- अन्तरक्रियात्मक रुपमा अर्को स्थानमा पाठ्य फाइलहरू सार्नुहोस (अधिलेखन गर्नु अघि प्रयोगकर्तालाई सोध्छ):

`cp -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">लक्ष्य_निर्देशिका/को/पथ</span>

- सार्नु अघि प्रतीकात्मक लिङ्कहरू पछ्याउनुहोस्:

`cp -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">लिङ्क</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">लक्ष्य_निर्देशिका/को/पथ</span>
