---
layout: page
title: common/aapt (हिन्दी)
description: "एंड्रॉइड एसेट पैकेजिंग टूल।"
content_hash: 4ff3ffbaf19bec1591e57fbf890ba44191ac26c3
last_modified_at: 2023-10-26
related_topics:
  - title: Deutsch version
    url: /de/common/aapt.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/aapt.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/aapt.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/aapt.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/aapt.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/aapt.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/aapt.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/aapt.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/aapt.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/aapt.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/aapt.html
    icon: bi bi-globe
---
# aapt

एंड्रॉइड एसेट पैकेजिंग टूल।
एंड्रॉइड ऐप के संसाधनों को संकलित और पैकेज करें।
अधिक जानकारी: <https://elinux.org/Android_aapt>.

- APK संग्रह में शामिल फ़ाइलों की सूची बनाएं:

`aapt list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ऐप.apk/का/पथ</span>

- किसी ऐप का मेटाडेटा (संस्करण, अनुमतियाँ, आदि) प्रदर्शित करें:

`aapt dump badging `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ऐप.apk/का/पथ</span>

- निर्दिष्ट निर्देशिका से फ़ाइलों के साथ एक नया APK संग्रह बनाएं:

`aapt package -F `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ऐप.apk/का/पथ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">निर्देशिका/का/पथ</span>
