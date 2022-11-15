---
layout: page
title: linux/mkfs.btrfs (Indonesia)
description: "Membuat sistem file btrfs."
content_hash: f9599f24b549c4632fd011bbd8790880c5e6e42b
related_topics:
  - title: English version
    url: /en/linux/mkfs.btrfs.html
    icon: bi bi-globe
---
# mkfs.btrfs

Membuat sistem file btrfs.
Default ke `raid1`, yang menyatakan 2 salinan sebuah blok data disebar ke 2 perangkat yang berbeda.
Informasi lebih lanjut: <https://btrfs.readthedocs.io/en/latest/mkfs.btrfs.html>.

- Membuat sebuah sistem file btrfs di satu perangkat:

`sudo mkfs.btrfs --metadata single --data single `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda</span>

- Membuat sebuah sistem file btrfs di beberapa perangkat dengan raid1:

`sudo mkfs.btrfs --metadata raid1 --data raid1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdN</span>

- Mengatur sebuah label untuk sistem file:

`sudo mkfs.btrfs --label "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">label</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda</span>` [`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdN</span>`]`
