---
layout: page
title: common/adb-reverse (Indonesia)
description: "Android Debug Bridge Reverse: membalik koneksi socket dari emulator Android atau perangkat Android terhubung."
content_hash: 17be09f2bd1d824fe9aeb275b04ad531f933c1bd
related_topics:
  - title: English version
    url: /en/common/adb-reverse.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/adb-reverse.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/adb-reverse.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/adb-reverse.html
    icon: bi bi-globe
---
# adb reverse

Android Debug Bridge Reverse: membalik koneksi socket dari emulator Android atau perangkat Android terhubung.
Informasi lebih lanjut: <https://developer.android.com/studio/command-line/adb>.

- Daftar semua koneksi socket terbalik dari emulator dan perangkat:

`adb reverse --list`

- Membalik port TCP dari emulator/perangkat ke localhost:

`adb reverse tcp:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port_jarak_jauh</span>` tcp:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port_lokal</span>

- Melepas koneksi socket terbalik dari emulator/perangkat:

`adb reverse --remove tcp:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port_jarak_jauh</span>

- Melepas semua koneksi socket terbalik dari semua emulator dan perangkat:

`adb reverse --remove-all`
