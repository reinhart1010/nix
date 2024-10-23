---
layout: page
title: common/7zr (हिन्दी)
description: "उच्च संपीड़न अनुपात के साथ फ़ाइल संग्रहकर्ता।"
content_hash: 2e6bd30d68cca0b242123b4e93df0227d7ef945f
last_modified_at: 2024-10-23
related_topics:
  - title: বাংলা version
    url: /bn/common/7zr.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/common/7zr.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/7zr.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/7zr.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/7zr.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/7zr.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/7zr.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/7zr.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/7zr.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/7zr.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/7zr.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/7zr.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/7zr.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/7zr.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/7zr.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/7zr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# 7zr

उच्च संपीड़न अनुपात के साथ फ़ाइल संग्रहकर्ता।
`7z` के समान, सिवाय इसके कि यह केवल 7z फ़ाइलों का समर्थन करता है।
अधिक जानकारी: <https://manned.org/7zr>.

- किसी फ़ाइल या निर्देशिका को संग्रहित करें:

`7zr a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">संग्रह.7z/का/पथ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फ़ाइल_या_निर्देशिका/का/पथ</span>

- किसी मौजूदा संग्रह को एन्क्रिप्ट करें(फ़ाइल नाम सहित):

`7zr a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">एन्क्रिप्टेड.7z/का/पथ</span>` -p`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पासवर्ड</span>` -mhe=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">संग्रह.7z/का/पथ</span>

- मूल निर्देशिका संरचना को संरक्षित करते हुए एक संग्रह निकालें:

`7zr x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">संग्रह.7z/का/पथ</span>

- किसी विशिष्ट निर्देशिका में एक संग्रह निकालें:

`7zr x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">संग्रह.7z/का/पथ</span>` -o`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">आउटपुट/का/पथ</span>

- `स्टडआउट` करने के लिए एक संग्रह निकालें:

`7zr x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">संग्रह.7z/का/पथ</span>` -so`

- किसी संग्रह की सामग्री सूचीबद्ध करें:

`7zr l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">संग्रह.7z/का/पथ</span>

- संग्रहसंपीड़न का स्तर निर्धारित करें (उच्च का अर्थ है अधिक संपीड़न, लेकिन धीमा):

`7zr a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">संग्रह.7z/का/पथ</span>` -mx=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0|1|3|5|7|9</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फ़ाइल_या_निर्देशिका/का/पथ</span>
