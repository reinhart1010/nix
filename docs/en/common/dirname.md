---
layout: page
title: common/dirname (English)
description: "Calculates the parent directory of a given file or directory path."
content_hash: f98578a63ec26c7010a236d4eed8eb9df3d6009b
last_modified_at: 2024-01-31
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
tldri18n_status: 2
---
# dirname

Calculates the parent directory of a given file or directory path.
More information: <https://www.gnu.org/software/coreutils/dirname>.

- Calculate the parent directory of a given path:

`dirname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Calculate the parent directory of multiple paths:

`dirname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory1 path/to/file_or_directory2 ...</span>

- Delimit output with a NUL character instead of a newline (useful when combining with `xargs`):

`dirname --zero `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory1 path/to/file_or_directory2 ...</span>
