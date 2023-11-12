---
layout: page
title: windows/iscc (English)
description: "Compiler for Inno Setup installers."
content_hash: d0c725b6c7f5bcb9bd58acf24d58a4d11a7436c5
last_modified_at: 2023-11-12
related_topics:
  - title: 中文 version
    url: /zh/windows/iscc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# iscc

Compiler for Inno Setup installers.
It compiles an Inno Setup scripts into an Windows installer executable.
More information: <https://jrsoftware.org/isinfo.php>.

- Compile an Inno Setup script:

`iscc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file.iss</span>

- Quietly compile an Inno Setup installer:

`iscc /Q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file.iss</span>

- Compile a signed Inno Setup installer:

`iscc /S=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file.iss</span>
