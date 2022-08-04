---
layout: page
title: windows/msiexec (English)
description: "Install, update, repair, or uninstall Windows programs using MSI and MSP package files."
content_hash: 74c4af424ee962bcf9d7a70af51bdef6e2f9feea
---
# msiexec

Install, update, repair, or uninstall Windows programs using MSI and MSP package files.
More information: <https://docs.microsoft.com/windows-server/administration/windows-commands/msiexec>.

- Install a program from its MSI package:

`msiexec /package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.msi</span>

- Install a MSI package from a website:

`msiexec /package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/installer.msi</span>

- Install a MSP patch file:

`msiexec /update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.msp</span>

- Uninstall a program or patch using their respective MSI or MSP file:

`msiexec /uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
