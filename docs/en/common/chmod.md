---
layout: page
title: common/chmod (English)
description: "Change the access permissions of a file or directory."
content_hash: 2680a4295b967cf730e2afbad1e9ab42819ffdb2
related_topics:
  - title: Deutsch version
    url: /de/common/chmod.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/chmod.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/chmod.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/chmod.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/chmod.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/chmod.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/chmod.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/chmod.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/chmod.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/chmod.html
    icon: bi bi-globe
---
# chmod

Change the access permissions of a file or directory.
More information: <https://www.gnu.org/software/coreutils/chmod>.

- Give the [u]ser who owns a file the right to e[x]ecute it:

`chmod u+x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Give the [u]ser rights to [r]ead and [w]rite to a file/directory:

`chmod u+rw `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Remove e[x]ecutable rights from the [g]roup:

`chmod g-x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Give [a]ll users rights to [r]ead and e[x]ecute:

`chmod a+rx `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Give [o]thers (not in the file owner's group) the same rights as the [g]roup:

`chmod o=g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Remove all rights from [o]thers:

`chmod o= `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Change permissions recursively giving [g]roup and [o]thers the ability to [w]rite:

`chmod -R g+w,o+w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Recursively give [a]ll users [r]ead permissions to files and e[X]ecute permissions to sub-directories within a directory:

`chmod -R a+rX `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
