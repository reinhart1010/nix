---
layout: page
title: common/adb-reverse (Indonesia)
description: "Android Debug Bridge Reverse: membalik koneksi socket dari emulator Android atau perangkat Android terhubung."
content_hash: 8c70637e7627abd4c37c306f82dd10e4beabbb04
last_modified_at: 2024-02-22
related_topics:
  - title: English version
    url: /en/common/adb-reverse.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/adb-reverse.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/adb-reverse.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/adb-reverse.html
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
tldri18n_status: 2
---
# adb reverse

Android Debug Bridge Reverse: membalik koneksi socket dari emulator Android atau perangkat Android terhubung.
Informasi lebih lanjut: <https://developer.android.com/tools/adb>.

- Daftar semua koneksi socket terbalik dari emulator dan perangkat:

`adb reverse --list`

- Balikkan port TCP dari emulator/perangkat ke localhost:

`adb reverse tcp:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port_jarak_jauh</span>` tcp:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port_lokal</span>

- Lepaskan koneksi socket terbalik dari emulator/perangkat:

`adb reverse --remove tcp:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port_jarak_jauh</span>

- Lepaskan semua koneksi socket terbalik dari semua emulator dan perangkat:

`adb reverse --remove-all`
