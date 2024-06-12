---
layout: page
title: common/amass-intel (Indonesia)
description: "Kumpulkan data pendukung pengintaian bersumber terbuka (OSI) terhadap suatu organisasi, seperti domain pangkal dan informasi Nomor Sistem Otonom (ASN)."
content_hash: 2120a671cfe8937e43d9ea8f9a8deaf103a11c4e
last_modified_at: 2024-06-12
related_topics:
  - title: English version
    url: /en/common/amass-intel.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/amass-intel.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/amass-intel.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/amass-intel.html
    icon: bi bi-globe
tldri18n_status: 2
---
# amass intel

Kumpulkan data pendukung pengintaian bersumber terbuka (OSI) terhadap suatu organisasi, seperti domain pangkal dan informasi Nomor Sistem Otonom (ASN).
Informasi lebih lanjut: <https://github.com/owasp-amass/amass/blob/master/doc/user_guide.md#the-intel-subcommand>.

- Cari para domain pangkal yang berkaitan dengan rentang alamat ([addr]ess) IP:

`amass intel -addr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.0.1-254</span>

- Gunakan metode pengintaian secara aktif:

`amass intel -active -addr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.0.1-254</span>

- Cari para domain pangkal yang berkaitan dengan suatu [d]omain:

`amass intel -whois -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_domain</span>

- Cari para pihak ASN yang berkaitan dengan suatu [org]anisasi:

`amass intel -org `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_organisasi</span>

- Cari daftar domain yang dipegang oleh suatu pihak Nomor Sistem Otonom (ASN) berdasarkan nomornya:

`amass intel -asn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nomor_asn</span>

- Simpan hasil pencarian ke dalam suatu berkas teks:

`amass intel -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">berkas_output</span>` -whois -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_domain</span>

- Tampilkan daftar sumber pencarian data:

`amass intel -list`
