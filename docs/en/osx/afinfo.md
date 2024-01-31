---
layout: page
title: osx/afinfo (English)
description: "Audio file metadata parser for OS X."
content_hash: 561d99cb3b4509f0b11cfbf95764f339a3fa60e0
last_modified_at: 2024-01-31
related_topics:
  - title: español version
    url: /es/osx/afinfo.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/osx/afinfo.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/afinfo.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/afinfo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# afinfo

Audio file metadata parser for OS X.
Built-in command of OS X.
More information: <https://keith.github.io/xcode-man-pages/afinfo.1.html>.

- Display info of a given audio file:

`afinfo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Print a one line description of the audio file:

`afinfo --brief `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Print metadata info and contents of the audio file's InfoDictionary:

`afinfo --info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Print output in XML format:

`afinfo --xml `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Print warnings for the audio file if any:

`afinfo --warnings `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Display help:

`afinfo --help`
