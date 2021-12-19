---
layout: page
title: common/asar (English)
description: "A file archiver for the Electron platform."
content_hash: dda345a14cda4188a092639a76188ea9f1b8b2b7
related_topics:
  - title: Indonesia version
    url: /id/common/asar.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/asar.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/asar.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/asar.html
    icon: bi bi-globe
---
# asar

A file archiver for the Electron platform.
More information: <https://github.com/electron/asar>.

- Archive a file or directory:

`asar pack `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archived.asar</span>

- Extract an archive:

`asar extract `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archived.asar</span>

- Extract a specific file from an archive:

`asar extract-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archived.asar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- List the contents of an archive file:

`asar list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archived.asar</span>
