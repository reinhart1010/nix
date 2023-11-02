---
layout: page
title: android/settings (हिन्दी)
description: "एंड्रॉइड ओएस के बारे में जानकारी प्राप्त करें।"
content_hash: 421fc23984a770a508feccea4f9796ad3e6bd657
last_modified_at: 2023-11-02
related_topics:
  - title: বাংলা version
    url: /bn/android/settings.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/android/settings.html
    icon: bi bi-globe
  - title: English version
    url: /en/android/settings.html
    icon: bi bi-globe
  - title: español version
    url: /es/android/settings.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/android/settings.html
    icon: bi bi-globe
  - title: français version
    url: /fr/android/settings.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/android/settings.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/android/settings.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/android/settings.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/android/settings.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/android/settings.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/android/settings.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/android/settings.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/android/settings.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/android/settings.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/android/settings.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/android/settings.html
    icon: bi bi-globe
---
# settings

एंड्रॉइड ओएस के बारे में जानकारी प्राप्त करें।
अधिक जानकारी: <https://adbinstaller.com/commands/adb-shell-settings-5b670d5ee7958178a2955536>।

- `global` नेमस्पेस में सेटिंग्स की एक सूची प्रदर्शित करें:

`settings list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">global</span>

- किसी विशिष्ट सेटिंग का मान प्राप्त करें:

`settings get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">global</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">airplane_mode_on</span>

- किसी सेटिंग का विशिष्ट मान सेट करें:

`settings put `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">system</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">screen_brightness</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">42</span>

- एक विशिष्ट सेटिंग हटाएँ:

`settings delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">secure</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">screensaver_enabled</span>
