---
layout: page
title: common/ar (English)
description: "Create, modify, and extract from Unix archives. Typically used for static libraries (`.a`) and Debian packages (`.deb`)."
content_hash: fcc807f053ff72b91f188adeac0b3cf682f1d37d
last_modified_at: 2022-12-20
related_topics:
  - title: français version
    url: /fr/common/ar.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ar.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ar.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ar.html
    icon: bi bi-globe
---
# ar

Create, modify, and extract from Unix archives. Typically used for static libraries (`.a`) and Debian packages (`.deb`).
See also: `tar`.
More information: <https://manned.org/ar>.

- E[x]tract all members from an archive:

`ar x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.a</span>

- Lis[t] contents in a specific archive:

`ar t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ar</span>

- [r]eplace or add specific files to an archive:

`ar r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.deb</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/debian-binary path/to/control.tar.gz path/to/data.tar.xz ...</span>

- In[s]ert an object file index (equivalent to using `ranlib`):

`ar s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.a</span>

- Create an archive with specific files and an accompanying object file index:

`ar rs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.a</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.o path/to/file2.o ...</span>
