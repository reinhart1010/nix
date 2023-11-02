---
layout: page
title: common/7za (हिन्दी)
description: "उच्च संपीड़न अनुपात के साथ फ़ाइल संग्रहकर्ता।"
content_hash: d892d02fedac5c5d16f1f25a0926ab18e9348413
last_modified_at: 2023-11-02
related_topics:
  - title: বাংলা version
    url: /bn/common/7za.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/common/7za.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/7za.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/7za.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/7za.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/7za.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/7za.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/7za.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/7za.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/7za.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/7za.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/7za.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/7za.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/7za.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/7za.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/7za.html
    icon: bi bi-globe
---
# 7za

उच्च संपीड़न अनुपात के साथ फ़ाइल संग्रहकर्ता।
`7z` के समान, सिवाय इसके कि यह कम फ़ाइल प्रकारों का समर्थन करता है लेकिन क्रॉस-प्लेटफ़ॉर्म है।
अधिक जानकारी: <https://manned.org/7za>।

- किसी फ़ाइल या निर्देशिका को संग्रहित करें:

`7za a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">संग्रह.7z/का/पथ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फ़ाइल_या_निर्देशिका/का/पथ</span>

- किसी मौजूदा संग्रह को एन्क्रिप्ट करें (फ़ाइल नामों सहित):

`7za a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">एन्क्रिप्टेड.7z/का/पथ</span>` -p`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पासवर्ड</span>` -mhe=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">संग्रह.7z/का/पथ</span>

- मूल निर्देशिका संरचना को संरक्षित करते हुए एक संग्रह निकालें:

`7za x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">संग्रह.7z/का/पथ</span>

- किसी संग्रह को किसी विशिष्ट निर्देशिका में निकालें:

`7za x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">संग्रह.7z/का/पथ</span>` -o`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">आउटपुट/का/पथ</span>

- `stdout` के लिए एक संग्रह निकालें:

`7za x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">संग्रह.7z/का/पथ</span>` -so`

- एक विशिष्ट संग्रह प्रकार का उपयोग करके संग्रह करें:

`7za a -t`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7z|bzip2|gzip|lzip|tar|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">संग्रह.7z/का/पथ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फ़ाइल_या_निर्देशिका/का/पथ</span>

- किसी संग्रह की सामग्री को सूचीबद्ध करें:

`7za l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">संग्रह.7z/का/पथ</span>

- उपलब्ध संग्रह प्रकारों की सूची बनाएं:

`7za i`
