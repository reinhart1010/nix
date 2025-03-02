---
layout: page
title: common/dirname (English)
description: "Calculates the parent directory of a file or directory path."
content_hash: e86004624e952caf57abce9a813cd24c4f7dd5fe
last_modified_at: 2025-03-02
related_topics:
  - title: italiano version
    url: /it/common/dirname.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/dirname.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/dirname.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/dirname.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dirname

Calculates the parent directory of a file or directory path.
More information: <https://www.gnu.org/software/coreutils/manual/html_node/dirname-invocation.html>.

- Calculate the parent directory of a given path:

`dirname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Calculate the parent directory of multiple paths:

`dirname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory1 path/to/file_or_directory2 ...</span>

- Delimit output with a NUL character instead of a newline (useful when combining with `xargs`):

`dirname --zero `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory1 path/to/file_or_directory2 ...</span>
