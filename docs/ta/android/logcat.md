---
layout: page
title: android/logcat (தமிழ்)
description: "கணினி செய்திகளின் பதிவை டம்ப் செய்யவும்."
content_hash: 8b16cfeefd70ad5c342eae839e68ec95baca2754
last_modified_at: 2023-06-02
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
  - title: français version
    url: /fr/android/logcat.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/android/logcat.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/android/logcat.html
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
  - title: Türkçe version
    url: /tr/android/logcat.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/android/logcat.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/android/logcat.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/android/logcat.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># logcat

கணினி செய்திகளின் பதிவை டம்ப் செய்யவும்.
மேலும் விவரத்திற்கு: <https://developer.android.com/studio/command-line/logcat>.

- கணினி பதிவுகளைக் காண்பி:

`logcat`

- ஒரு கோப்பில் கணினி பதிவுகளை எழுதவும்:

`logcat -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/கோப்பு</span>

- வழக்கமான வெளிப்பாட்டுடன் பொருந்தக்கூடிய காட்சி வரிகள்:

`logcat --regex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">வழக்கமான_வெளிப்பாடு</span>

- ஒரு குறிப்பிட்ட PIDக்கான பதிவுகளை காண்பி:

`logcat --pid=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- ஒரு குறிப்பிட்ட தொகுப்பின் செயல்முறைக்கான பதிவுகளை காண்பி:

`logcat --pid=$(pidof -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>`)`
