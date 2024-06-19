---
layout: page
title: common/arping (Indonesia)
description: "Cari dan selidiki para host jaringan melalui protokol ARP."
content_hash: 60501a0b5563cac91dd132ef2b588a912df1bc8c
last_modified_at: 2024-06-19
related_topics:
  - title: Deutsch version
    url: /de/common/arping.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/arping.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/arping.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/arping.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/arping.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/arping.html
    icon: bi bi-globe
tldri18n_status: 2
---
# arping

Cari dan selidiki para host jaringan melalui protokol ARP.
Bermanfaat untuk mencari alamat MAC dalam jaringan.
Informasi lebih lanjut: <https://github.com/ThomasHabets/arping>.

- Ping suatu host dengan megirimkan paket permintaan ARP:

`arping `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alamat_ip_host</span>

- Ping suatu host melalui antarmuka jaringan tertentu (contoh: `eth0`):

`arping -I `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">antarmuka_jaringan</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alamat_ip_host</span>

- Ping suatu host dan hentikan jika sang host mulai membalasnya:

`arping -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alamat_ip_host</span>

- Ping suatu host untuk jumlah kesempatan tertentu:

`arping -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jumlah_kesempatan</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alamat_ip_host</span>

- Sebarluaskan paket permintaan ARP kepada host apapun untuk membantu memutakhirkan informasi ARP dalam host tetangga:

`arping -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alamat_ip_untuk_disebarluaskan</span>

- [D]eteksi adanya alamat IP duplikat dalam jaringan ini dengan mengirimkan permintaan ARP dengan jangka waktu habis (timeout) sebanyak 3 detik:

`arping -D -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alamat_ip_untuk_diperiksa</span>
