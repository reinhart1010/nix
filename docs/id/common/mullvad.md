---
layout: page
title: common/mullvad (Indonesia)
description: "Program klien antarmuka baris perintah bagi layanan jaringan virtual privat (VPN) Mullvad VPN."
content_hash: a874446e769b578372576e3b255945ca88cb181a
last_modified_at: 2024-09-27
related_topics:
  - title: English version
    url: /en/common/mullvad.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/mullvad.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mullvad

Program klien antarmuka baris perintah bagi layanan jaringan virtual privat (VPN) Mullvad VPN.
Lihat juga: `fastd`, `ivpn`, `mozillavpn`, `warp-cli`.
Informasi lebih lanjut: <https://mullvad.net/>.

- Hubungkan dengan akun Mullvad dengan nomor induk akun Anda:

`mullvad account set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nomor_induk_akun</span>

- Aktifkan akses menuju jaringan lokal (LAN) selama menikmati akses VPN:

`mullvad lan set allow`

- Hubungkan dengan layanan VPN:

`mullvad connect`

- Tampilkan status koneksi VPN:

`mullvad status`
