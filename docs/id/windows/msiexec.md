---
layout: page
title: windows/msiexec (Indonesia)
description: "Pasang, perbarui, perbaiki, atau hapus program Windows melalui berkas MSI dan MSP yang tersedia."
content_hash: 09fc1668d2d4a87d91c7040a16f7e22f34b4dd2a
last_modified_at: 2024-10-03
related_topics:
  - title: English version
    url: /en/windows/msiexec.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/windows/msiexec.html
    icon: bi bi-globe
tldri18n_status: 2
---
# msiexec

Pasang, perbarui, perbaiki, atau hapus program Windows melalui berkas MSI dan MSP yang tersedia.
Informasi lebih lanjut: <https://learn.microsoft.com/windows-server/administration/windows-commands/msiexec>.

- Pasang suatu program melalui berkas MSI:

`msiexec /package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan\menuju\berkas.msi</span>

- Pasang berkas MSI dari suatu situs web:

`msiexec /package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/installer.msi</span>

- Pasang pembaruan suatu program melalui suatu berkas MSP:

`msiexec /update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan\menuju\berkas.msp</span>

- Menghapus pemasangan atau pembaruan suatu program melalui file MSI atau MSP yang tersedia:

`msiexec /uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan\menuju\berkas</span>
