---
layout: page
title: windows/msiexec (English)
description: "Install, update, repair, or uninstall Windows programs using MSI and MSP package files."
content_hash: ab2a6241df2c5e0a23be7d2132b6ff942979c7a7
last_modified_at: 2023-11-12
related_topics:
  - title: Indonesia version
    url: /id/windows/msiexec.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/windows/msiexec.html
    icon: bi bi-globe
tldri18n_status: 2
---
# msiexec

Install, update, repair, or uninstall Windows programs using MSI and MSP package files.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/msiexec>.

- Install a program from its MSI package:

`msiexec /package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file.msi</span>

- Install a MSI package from a website:

`msiexec /package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/installer.msi</span>

- Install a MSP patch file:

`msiexec /update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file.msp</span>

- Uninstall a program or patch using their respective MSI or MSP file:

`msiexec /uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file</span>
