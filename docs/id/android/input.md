---
layout: page
title: android/input (Indonesia)
description: "Kirim sinyal input terhadap sebuah perangkat Android."
content_hash: ea43e9ee0e04d448c19334b27a2583f73172c98c
related_topics:
  - title: Deutsch version
    url: /de/android/input.html
    icon: bi bi-globe
  - title: English version
    url: /en/android/input.html
    icon: bi bi-globe
  - title: français version
    url: /fr/android/input.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/android/input.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/android/input.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/android/input.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/android/input.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/android/input.html
    icon: bi bi-globe
---
# input

Kirim sinyal input terhadap sebuah perangkat Android.
Perintah ini hanya dapat dijalankan melalui `adb shell`.
Informasi lebih lanjut: <https://developer.android.com/reference/android/view/KeyEvent.html#constants_1>.

- Masukkan input karakter (layaknya pada papan kunci / keyboard) terhadap perangkat Android:

`input keyevent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kode_event</span>

- Masukkan input teks ke dalam perangkat Android (spasi ditandai dengan `%s`):

`input text "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">teks</span>`"`

- Masukkan input sentuhan layar pada posisi tertentu:

`input tap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">posisi_x</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">posisi_y</span>

- Simulasikan gerakan usap/swipe terhadap perangkat Android:

`input swipe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">posisi_awal_x</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">posisi_awal_y</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">posisi_akhir_x</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">posisi_akhir_y</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">durasi_dalam_milidetik</span>

- Simulasikan interaksi tekan-dan-tahan terhadap perangkat Android:

`input swipe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">posisi_x</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">posisi_y</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">posisi_x</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">posisi_y</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">durasi_dalam_milidetik</span>
