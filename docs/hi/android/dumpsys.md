---
layout: page
title: android/dumpsys (हिन्दी)
description: "एंड्रॉइड सिस्टम सेवाओं के बारे में जानकारी प्रदान करें।"
content_hash: 7edc25c791cc4113619660608bacccf72bede5c2
last_modified_at: 2024-02-22
related_topics:
  - title: বাংলা version
    url: /bn/android/dumpsys.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/android/dumpsys.html
    icon: bi bi-globe
  - title: English version
    url: /en/android/dumpsys.html
    icon: bi bi-globe
  - title: español version
    url: /es/android/dumpsys.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/android/dumpsys.html
    icon: bi bi-globe
  - title: français version
    url: /fr/android/dumpsys.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/android/dumpsys.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/android/dumpsys.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/android/dumpsys.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/android/dumpsys.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/android/dumpsys.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/android/dumpsys.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/android/dumpsys.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/android/dumpsys.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/android/dumpsys.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/android/dumpsys.html
    icon: bi bi-globe
  - title: o‘zbek version
    url: /uz/android/dumpsys.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/android/dumpsys.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/android/dumpsys.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dumpsys

एंड्रॉइड सिस्टम सेवाओं के बारे में जानकारी प्रदान करें।
इस कमांड का उपयोग केवल `adb shell` के माध्यम से किया जा सकता है।
अधिक जानकारी: <https://developer.android.com/tools/dumpsys>।

- सभी सिस्टम सेवाओं के लिए नैदानिक आउटपुट प्राप्त करें:

`dumpsys`

- किसी विशिष्ट सिस्टम सेवा के लिए नैदानिक आउटपुट प्राप्त करें:

`dumpsys `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">सेवा</span>

- उन सभी सेवाओं की सूची बनाएं जिनके बारे में `dumpsys` जानकारी दे सकता है:

`dumpsys -l`

- किसी सेवा के लिए सेवा-विशिष्ट तर्कों की सूची बनाएं:

`dumpsys `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">सेवा</span>` -h`

- नैदानिक आउटपुट से एक विशिष्ट सेवा को बाहर करें:

`dumpsys --skip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">सेवा</span>

- सेकंड में टाइमआउट अवधि निर्दिष्ट करें (डिफ़ॉल्ट 10s पर):

`dumpsys -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8</span>
