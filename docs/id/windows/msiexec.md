---
layout: page
title: windows/msiexec (Indonesia)
description: "Memasang, memperbarui, memperbaiki, atau menghapus program Windows melalui file MSI dan MSP yang tersedia."
content_hash: 1c871186fae9347f179120d9d8de3c41922110c2
related_topics:
  - title: English version
    url: /en/windows/msiexec.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># msiexec

Memasang, memperbarui, memperbaiki, atau menghapus program Windows melalui file MSI dan MSP yang tersedia.
Informasi lebih lanjut: <https://docs.microsoft.com/windows-server/administration/windows-commands/msiexec>.

- Memasang sebuah program melalui file MSI:

`msiexec /package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file.msi</span>

- Memasang file MSI dari internet:

`msiexec /package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/installer.msi</span>

- Memasang pembaruan program melalui file MSP:

`msiexec /update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file.msp</span>

- Menghapus pemasangan atau pembaruan program melalui file MSI atau MSP yang tersedia:

`msiexec /uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file</span>
