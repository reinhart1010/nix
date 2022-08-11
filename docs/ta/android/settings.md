---
layout: page
title: android/settings (தமிழ்)
description: "ஆண்ட்ராய்டு ஓஎஸ் பற்றிய தகவல்களைப் பெறுங்கள்."
content_hash: bae2e652464813a106e33c341e3bb7c6106224e5
related_topics:
  - title: Deutsch version
    url: /de/android/settings.html
    icon: bi bi-globe
  - title: English version
    url: /en/android/settings.html
    icon: bi bi-globe
  - title: français version
    url: /fr/android/settings.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/android/settings.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/android/settings.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/android/settings.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/android/settings.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/android/settings.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># settings

ஆண்ட்ராய்டு ஓஎஸ் பற்றிய தகவல்களைப் பெறுங்கள்.
மேலும் விவரத்திற்கு: <https://adbinstaller.com/commands/adb-shell-settings-5b670d5ee7958178a2955536>.

- `குளோபல்` பெயர்வெளியில் அமைப்புகளின் பட்டியலைக் காண்பி:

`settings list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">குளோபல்</span>

- ஒரு குறிப்பிட்ட அமைப்பின் மதிப்பைப் பெறவும்:

`settings get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">குளோபல்</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">விமானம்_முறை_ஆன்</span>

- அமைப்பின் மதிப்பை அமைக்கவும்:

`settings put `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">குளோபல்</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">திரை_பிரகாசம்</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">42</span>

- Delete a specific setting:

`settings delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதுகாப்பான</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">திரை_சேமிப்பான்_இயக்கப்பட்டது</span>
