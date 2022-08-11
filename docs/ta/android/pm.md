---
layout: page
title: android/pm (தமிழ்)
description: "ஆண்ட்ராய்டு சாதனத்தில் ஆப்ஸ் பற்றிய தகவலைக் காட்டவும்."
content_hash: 9f4d90b01a5e85751001d861e3919961587eade9
related_topics:
  - title: Deutsch version
    url: /de/android/pm.html
    icon: bi bi-globe
  - title: English version
    url: /en/android/pm.html
    icon: bi bi-globe
  - title: français version
    url: /fr/android/pm.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/android/pm.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/android/pm.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/android/pm.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/android/pm.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/android/pm.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># pm

ஆண்ட்ராய்டு சாதனத்தில் ஆப்ஸ் பற்றிய தகவலைக் காட்டவும்.
மேலும் விவரத்திற்கு: <https://developer.android.com/studio/command-line/adb#pm>.

- நிறுவப்பட்ட அனைத்து பயன்பாடுகளின் பட்டியலை அச்சிடவும்:

`pm list packages`

- நிறுவப்பட்ட அனைத்து கணினி பயன்பாடுகளின் பட்டியலை அச்சிடவும்:

`pm list packages -s`

- நிறுவப்பட்ட அனைத்து மூன்றாம் தரப்பு பயன்பாடுகளின் பட்டியலை அச்சிடவும்:

`pm list packages -3`

- குறிப்பிட்ட முக்கிய வார்த்தைகளுடன் பொருந்தக்கூடிய பயன்பாடுகளின் பட்டியலை அச்சிடவும்:

`pm list packages `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">முக்கிய_வார்த்தைகள்</span>

- ஒரு குறிப்பிட்ட பயன்பாட்டின் APK இன் பாதையை அச்சிடவும்:

`pm path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">செயலி</span>
