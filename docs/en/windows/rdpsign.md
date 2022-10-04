---
layout: page
title: windows/rdpsign (English)
description: "A tool for signing Remote Desktop Protocol (RDP) files."
content_hash: 2c8cbf266606597b69b6548ec18c3c4a2752881b
related_topics:
  - title: 中文 version
    url: /zh/windows/rdpsign.html
    icon: bi bi-globe
---
# rdpsign

A tool for signing Remote Desktop Protocol (RDP) files.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/rdpsign>.

- Sign an RDP file:

`rdpsign `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.rdp</span>

- Sign an RDP file using a specific sha256 hash:

`rdpsign `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.rdp</span>` /sha265 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hash</span>

- Enable quiet output:

`rdpsign `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.rdp</span>` /q`

- Display verbose warnings, messages and statuses:

`rdpsign `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.rdp</span>` /v`

- Test the signing by displaying the output to stdout without updating the file:

`rdpsign `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.rdp</span>` /l`
