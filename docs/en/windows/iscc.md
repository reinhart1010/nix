---
layout: page
title: windows/iscc (English)
description: "Compiler for Inno Setup installers."
content_hash: 5dabedf246acfcc366d21e278dfad4d1d7c7d40d
related_topics:
  - title: 中文 version
    url: /zh/windows/iscc.html
    icon: bi bi-globe
---
# iscc

Compiler for Inno Setup installers.
It compiles an Inno Setup scripts into an Windows installer executable.
More information: <https://jrsoftware.org/isinfo.php>.

- Compile an Inno Setup script:

`iscc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.iss</span>

- Quietly compile an Inno Setup installer:

`iscc /Q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.iss</span>

- Compile a signed Inno Setup installer:

`iscc /S=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.iss</span>
