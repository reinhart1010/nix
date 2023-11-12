---
layout: page
title: common/cp (हिन्दी)
description: "फाइलों और निर्देशिकाओं की प्रतिलिपि बनाएँ।"
content_hash: 772ad11a09fd9089c1684a1ccf191354fa49d9f6
last_modified_at: 2023-11-12
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
  - title: नेपाली version
    url: /ne/common/cp.html
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

फाइलों और निर्देशिकाओं की प्रतिलिपि बनाएँ।
अधिक जानकारी: <https://www.gnu.org/software/coreutils/cp>।

- किसी फ़ाइल को दूसरे स्थान पर कॉपी करें:

`cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">स्रोत_फ़ाइल/का/पथ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">लक्ष्य_फ़ाइल/का/पथ</span>

- फ़ाइल नाम रखते हुए किसी फ़ाइल को दूसरी निर्देशिका में कॉपी करें:

`cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">स्रोत_फ़ाइल/का/पथ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">लक्ष्य_निर्देशिका/का/पथ</span>

- किसी निर्देशिका की सामग्री को किसी अन्य स्थान पर दोबारा कॉपी करें (यदि गंतव्य मौजूद है, तो निर्देशिका इसके अंदर कॉपी की गई है):

`cp -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">स्रोत_निर्देशिका/का/पथ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">लक्ष्य_निर्देशिका/का/पथ</span>

- एक निर्देशिका को पुनरावर्ती रूप से कॉपी करें, वर्बोज़ मोड में (फ़ाइलों को कॉपी किए जाने के रूप में दिखाता है):

`cp -vR `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">स्रोत_निर्देशिका/का/पथ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">लक्ष्य_निर्देशिका/का/पथ</span>

- टेक्स्ट फ़ाइलों को किसी अन्य स्थान पर इंटरेक्टिव मोड में कॉपी करें (ओवरराइटिंग से पहले उपयोगकर्ता को संकेत देता है):

`cp -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">लक्ष्य_निर्देशिका/का/पथ</span>

- कॉपी करने से पहले प्रतीकात्मक लिंक का पालन करें:

`cp -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">लिंक</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">लक्ष्य_निर्देशिका/का/पथ</span>
