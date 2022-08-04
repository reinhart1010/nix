---
layout: page
title: android/cmd (Indonesia)
description: "Manajer layanan (daemon) untuk Android."
content_hash: fe510fdc7bc7c6c2bc4540a5f5cb98ea3e9a025b
related_topics:
  - title: বাংলা version
    url: /bn/android/cmd.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/android/cmd.html
    icon: bi bi-globe
  - title: English version
    url: /en/android/cmd.html
    icon: bi bi-globe
  - title: français version
    url: /fr/android/cmd.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/android/cmd.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/android/cmd.html
    icon: bi bi-globe
  - title: o‘zbek version
    url: /uz/android/cmd.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/android/cmd.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/android/cmd.html
    icon: bi bi-globe
---
# cmd

Manajer layanan (daemon) untuk Android.
Informasi lebih lanjut: <https://cs.android.com/android/platform/superproject/+/master:frameworks/native/cmds/cmd/>.

- Melihat daftar layanan yang sedang berjalan:

`cmd -l`

- Memanggil suatu layanan tertentu:

`cmd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alarm</span>

- Memanggil layanan dengan argumen tertentu:

`cmd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vibrator</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vibrate 300</span>
