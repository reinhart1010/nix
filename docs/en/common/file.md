---
layout: page
title: common/file (English)
description: "Determine file type."
content_hash: 954bcae5869f9517eeaa9a2cf3f2a217c76fae90
related_topics:
  - title: Deutsch version
    url: /de/common/file.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/file.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/file.html
    icon: bi bi-globe
---
# file

Determine file type.
More information: <https://manned.org/file>.

- Give a description of the type of the specified file. Works fine for files with no file extension:

`file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Look inside a zipped file and determine the file type(s) inside:

`file -z `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo.zip</span>

- Allow file to work with special or device files:

`file -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Don't stop at first file type match; keep going until the end of the file:

`file -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Determine the MIME encoding type of a file:

`file -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>
