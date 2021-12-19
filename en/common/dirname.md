---
layout: page
title: common/dirname (English)
description: "Calculates the parent directory of a given file or directory path."
content_hash: 9d379020996262be2e78023d0b5c8303fc2e034b
related_topics:
  - title: italiano version
    url: /it/common/dirname.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/dirname.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/dirname.html
    icon: bi bi-globe
---
# dirname

Calculates the parent directory of a given file or directory path.
More information: <https://www.gnu.org/software/coreutils/dirname>.

- Calculate the parent directory of a given path:

`dirname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Calculate the parent directory of multiple paths:

`dirname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_a</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory_b</span>

- Delimit output with a NUL character instead of a newline (useful when combining with `xargs`):

`dirname --zero `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory_a</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_b</span>
