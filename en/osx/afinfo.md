---
layout: page
title: osx/afinfo (English)
description: "Audio file metadata parser for OS X."
content_hash: 7a01c99214fc86cd018e7abc92baf103c454385a
related_topics:
  - title: español version
    url: /es/osx/afinfo.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/osx/afinfo.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/afinfo.html
    icon: bi bi-globe
---
# afinfo

Audio file metadata parser for OS X.
Built-in command of OS X.
More information: <https://ss64.com/osx/afinfo.html>.

- Display info of a given audio file:

`afinfo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Print a one line description of the audio file:

`afinfo -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Print metadata info and contents of the audio file's InfoDictionary:

`afinfo -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Print output in XML format:

`afinfo -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Print warnings for the audio file if any:

`afinfo --warnings `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Display help for full usage:

`afinfo -h`
