---
layout: page
title: android/logcat (हिन्दी)
description: "सिस्टम संदेशों का एक लॉग डंप करें, जिसमें त्रुटि होने पर स्टैक ट्रेस और एप्लिकेशन द्वारा लॉग किए गए सूचना संदेश शामिल हों।"
content_hash: 8392a6f66cfca60ac179ecb2f0f7ce2937bd9231
last_modified_at: 2023-11-06
related_topics:
  - title: বাংলা version
    url: /bn/android/logcat.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/android/logcat.html
    icon: bi bi-globe
  - title: English version
    url: /en/android/logcat.html
    icon: bi bi-globe
  - title: español version
    url: /es/android/logcat.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/android/logcat.html
    icon: bi bi-globe
  - title: français version
    url: /fr/android/logcat.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/android/logcat.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/android/logcat.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/android/logcat.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/android/logcat.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/android/logcat.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/android/logcat.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/android/logcat.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/android/logcat.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/android/logcat.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/android/logcat.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/android/logcat.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/android/logcat.html
    icon: bi bi-globe
---
# logcat

सिस्टम संदेशों का एक लॉग डंप करें, जिसमें त्रुटि होने पर स्टैक ट्रेस और एप्लिकेशन द्वारा लॉग किए गए सूचना संदेश शामिल हों।
अधिक जानकारी: <https://developer.android.com/studio/command-line/logcat>।

- सिस्टम लॉग प्रदर्शित करें:

`logcat`

- किसी फ़ाइल में सिस्टम लॉग लिखें:

`logcat -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फ़ाइल/का/पथ</span>

- ऐसी पंक्तियाँ प्रदर्शित करें जो नियमित अभिव्यक्ति से मेल खाती हों:

`logcat --regex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">नियमित_अभिव्यक्ति</span>

- किसी विशिष्ट पीआईडी के लिए लॉग प्रदर्शित करें:

`logcat --pid=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पीआईडी</span>

- किसी विशिष्ट पैकेज की प्रक्रिया के लिए लॉग प्रदर्शित करें:

`logcat --pid=$(pidof -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पैकेज</span>`)`
