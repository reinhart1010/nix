---
layout: page
title: common/asar (English)
description: "A file archiver for the Electron platform."
content_hash: facda8f42acf62cbc7b95b4108f95f4173c11fda
last_modified_at: 2023-04-14
related_topics:
  - title: español version
    url: /es/common/asar.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/asar.html
    icon: bi bi-globe
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

`asar pack `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file_or_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_archive.asar</span>

- Extract an archive:

`asar extract `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/archive.asar</span>

- Extract a specific file from an archive:

`asar extract-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/archive.asar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- List the contents of an archive file:

`asar list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/archive.asar</span>
