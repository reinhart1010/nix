---
layout: page
title: common/adb-shell (हिन्दी)
description: "एंड्रॉइड डीबग ब्रिज शेल: एंड्रॉइड एमुलेटर इंस्टेंस या कनेक्टेड एंड्रॉइड डिवाइस पर रिमोट शेल कमांड चलाएं।"
content_hash: b3075ecf5c0bee7648abc9c90de65b6d44dbc219
last_modified_at: 2024-02-22
related_topics:
  - title: English version
    url: /en/common/adb-shell.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/adb-shell.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/adb-shell.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/adb-shell.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/adb-shell.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/adb-shell.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/adb-shell.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/adb-shell.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/adb-shell.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/adb-shell.html
    icon: bi bi-globe
tldri18n_status: 2
---
# adb shell

एंड्रॉइड डीबग ब्रिज शेल: एंड्रॉइड एमुलेटर इंस्टेंस या कनेक्टेड एंड्रॉइड डिवाइस पर रिमोट शेल कमांड चलाएं।
अधिक जानकारी: <https://developer.android.com/tools/adb>।

- एम्यूलेटर या डिवाइस पर रिमोट इंटरैक्टिव शेल प्रारंभ करें:

`adb shell`

- एम्यूलेटर या डिवाइस से सभी गुण प्राप्त करें:

`adb shell getprop`

- सभी रनटाइम अनुमतियों को उनके डिफ़ॉल्ट पर वापस लाएं:

`adb shell pm reset-permissions`

- किसी एप्लिकेशन के लिए खतरनाक अनुमति रद्द करें:

`adb shell pm revoke `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पैकेज</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">अनुमति</span>

- एक महत्वपूर्ण घटना को ट्रिगर करें:

`adb shell input keyevent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">कीकोड</span>

- किसी एमुलेटर या डिवाइस पर किसी एप्लिकेशन का डेटा साफ़ करें:

`adb shell pm clear `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पैकेज</span>

- एम्यूलेटर या डिवाइस पर एक गतिविधि प्रारंभ करें:

`adb shell am start -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पैकेज</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">गतिविधि</span>

- किसी एम्यूलेटर या डिवाइस पर घरेलू गतिविधि प्रारंभ करें:

`adb shell am start -W -c android.intent.category.HOME -a android.intent.action.MAIN`
