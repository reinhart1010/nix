---
layout: page
title: common/unzip (English)
description: "Extract files/directories from Zip archives."
content_hash: 21440b5469571f244b68e657712fcad71af64879
last_modified_at: 2024-09-16
related_topics:
  - title: 한국어 version
    url: /ko/common/unzip.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/unzip.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/unzip.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/unzip.html
    icon: bi bi-globe
tldri18n_status: 2
---
# unzip

Extract files/directories from Zip archives.
See also: `zip`.
More information: <https://manned.org/unzip>.

- Extract all files/directories from specific archives into the current directory:

`unzip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/archive1.zip path/to/archive2.zip ...</span>

- Extract files/directories from archives to a specific path:

`unzip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/archive1.zip path/to/archive2.zip ...</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output</span>

- Extract files/directories from archives to `stdout`:

`unzip -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/archive1.zip path/to/archive2.zip ...</span>

- Extract the contents of the file(s) to `stdout` alongside the extracted file names:

`unzip -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gbk</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/archive1.zip path/to/archive2.zip ...</span>

- List the contents of a specific archive without extracting them:

`unzip -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/archive.zip</span>

- Extract a specific file from an archive:

`unzip -j `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/archive.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1_in_archive path/to/file2_in_archive ...</span>
