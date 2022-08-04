---
layout: page
title: android/dumpsys (o‘zbek)
description: "Android tizimi xizmatlari to'g'risida malumot berish."
content_hash: 444cd58573e0b1ad25476a033d773462940afec3
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
  - title: 中文 version
    url: /zh/android/dumpsys.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/android/dumpsys.html
    icon: bi bi-globe
---
# dumpsys

Android tizimi xizmatlari to'g'risida malumot berish.
Bu buyruq faqatgina `adb shell` bilan ishlatiladi.
Ko'proq malumot: <https://developer.android.com/studio/command-line/dumpsys>.

- Tizimning barcha xizmatlari haqida tahliliy malumot:

`dumpsys`

- Biron xizmat to'g'risida tahliliy malumot olish:

`dumpsys `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service</span>

- `dumpsys` buyrug'idagi barcha xizmatlarni chiqaradi:

`dumpsys -l`

- Xizmatning argumentlarini chiqaradi:

`dumpsys `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service</span>` -h`

- Tahliliy malumotlar ro'yhatidan biron xizmatni qoldirish:

`dumpsys --skip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service</span>

- Time out ni belgilash (sekundlarda):

`dumpsys -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sekund</span>
