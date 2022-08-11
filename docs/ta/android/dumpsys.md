---
layout: page
title: android/dumpsys (தமிழ்)
description: "ஆண்ட்ராய்டு சிஸ்டம் சேவைகள் பற்றிய தகவலை வழங்கவும்."
content_hash: 307f04c1de67cacded94ed6059180f7e83ae7bf8
related_topics:
  - title: Deutsch version
    url: /de/android/dumpsys.html
    icon: bi bi-globe
  - title: English version
    url: /en/android/dumpsys.html
    icon: bi bi-globe
  - title: français version
    url: /fr/android/dumpsys.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/android/dumpsys.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/android/dumpsys.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/android/dumpsys.html
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
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># dumpsys

ஆண்ட்ராய்டு சிஸ்டம் சேவைகள் பற்றிய தகவலை வழங்கவும்.
இந்தக் கட்டளையை `adb shell` மூலம் மட்டுமே பயன்படுத்த முடியும்.
மேலும் விவரத்திற்கு: <https://developer.android.com/studio/command-line/dumpsys>.

- அனைத்து கணினி சேவைகளுக்கும் கண்டறியும் வெளியீட்டைப் பெறவும்:

`dumpsys`

- ஒரு குறிப்பிட்ட கணினி சேவைக்கான கண்டறியும் வெளியீட்டைப் பெறவும்:

`dumpsys `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">சேவை</span>

- அனைத்து சேவைகளையும் பட்டியலிடுங்கள் `dumpsys` இதைப் பற்றிய தகவல்களை வழங்க முடியும்:

`dumpsys -l`

- ஒரு சேவைக்கான சேவை சார்ந்த வாதங்களைப் பட்டியலிடுங்கள்:

`dumpsys `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">சேவை</span>` -h`

- கண்டறியும் வெளியீட்டில் இருந்து ஒரு குறிப்பிட்ட சேவையை விலக்கவும்:

`dumpsys --skip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">சேவை</span>

- நேரம் முடிவடையும் காலத்தை வினாடிகளில் குறிப்பிடவும் (இயல்புநிலையிலிருந்து 10 வினாடிகள் வரை):

`dumpsys -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">வினாடிகள்</span>
