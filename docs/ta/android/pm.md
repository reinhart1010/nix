---
layout: page
title: android/pm (தமிழ்)
description: "ஆண்ட்ராய்டு சாதனத்தில் பயன்பாடுகள் பற்றிய தகவலைக் காண்பி."
content_hash: 96c07795724a8c19021977e9168ecfa22a5819e0
last_modified_at: 2023-01-03
related_topics:
  - title: Deutsch version
    url: /de/android/pm.html
    icon: bi bi-globe
  - title: English version
    url: /en/android/pm.html
    icon: bi bi-globe
  - title: español version
    url: /es/android/pm.html
    icon: bi bi-globe
  - title: français version
    url: /fr/android/pm.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/android/pm.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/android/pm.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/android/pm.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/android/pm.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/android/pm.html
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
# pm

ஆண்ட்ராய்டு சாதனத்தில் பயன்பாடுகள் பற்றிய தகவலைக் காண்பி.
மேலும் விவரத்திற்கு: <https://developer.android.com/studio/command-line/adb#pm>.

- நிறுவப்பட்ட அனைத்து பயன்பாடுகளையும் பட்டியலிடுங்கள்:

`pm list packages`

- நிறுவப்பட்ட அனைத்து கணினி பயன்பாடுகளையும் பட்டியலிடுங்கள்:

`pm list packages -s`

- நிறுவப்பட்ட அனைத்து மூன்றாம் தரப்பு பயன்பாடுகளையும் பட்டியலிடுங்கள்:

`pm list packages -3`

- குறிப்பிட்ட முக்கிய வார்த்தைகளுடன் பொருந்தக்கூடிய பயன்பாடுகளை பட்டியலிடுங்கள்:

`pm list packages `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">முக்கிய_வார்த்தை1 முக்கிய_வார்த்தை2 ...</span>

- குறிப்பிட்ட பயன்பாட்டின் APK இன் பாதையைக் காண்பி:

`pm path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">செயலி</span>
