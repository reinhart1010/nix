---
layout: page
title: linux/cat (English)
description: "Print and concatenate files."
content_hash: f7781badf22f771267f27834517177fbc1a19514
last_modified_at: 2025-03-02
related_topics:
  - title: español version
    url: /es/linux/cat.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/cat.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/cat.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/linux/cat.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/cat.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/cat.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/cat.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/cat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cat

Print and concatenate files.
More information: <https://www.gnu.org/software/coreutils/manual/html_node/cat-invocation.html>.

- Print the contents of a file to `stdout`:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Concatenate several files into an output file:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file</span>

- Append several files to an output file:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>` >> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file</span>

- Write `stdin` to a file:

`cat - > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- [n]umber all output lines:

`cat -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Display non-printable and whitespace characters (with `M-` prefix if non-ASCII):

`cat -v -t -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
