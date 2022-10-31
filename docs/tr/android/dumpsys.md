---
layout: page
title: android/dumpsys (Türkçe)
description: "Android sistem servisleri ile ilgili bilgi sağla."
content_hash: 967fa58686a39c122c8fd177b9265ffa7c18c0c9
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
  - title: polski version
    url: /pl/android/dumpsys.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/android/dumpsys.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/android/dumpsys.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/android/dumpsys.html
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
# dumpsys

Android sistem servisleri ile ilgili bilgi sağla.
Bu komut yalnızca `adb shell` ile kullanılabilir.
Daha fazla bilgi için: <https://developer.android.com/studio/command-line/dumpsys>.

- Tüm sistem servisleri için tanısal bir çıktı al:

`dumpsys`

- Belirtilen sistem servisi için tanısal bir çıktı al:

`dumpsys `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">servis</span>

- `dumpsys` komutunun hakkında bilgi verebileceği tüm servisleri sırala:

`dumpsys -l`

- Bir servis için servise özel argümanları sırala:

`dumpsys `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">servis</span>` -h`

- Tanı çıktısından belirtilen servisi çıkart:

`dumpsys --skip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">servis</span>

- Saniye bazında bir zaman aşımı süresi belirle (varsayılan 10 saniyedir):

`dumpsys -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">saniye</span>
