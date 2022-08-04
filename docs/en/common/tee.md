---
layout: page
title: common/tee (English)
description: "Read from standard input and write to standard output and files (or commands)."
content_hash: 847e7401637f73cb238efbc353f1783b31ab854a
related_topics:
  - title: español version
    url: /es/common/tee.html
    icon: bi bi-globe
---
# tee

Read from standard input and write to standard output and files (or commands).
More information: <https://www.gnu.org/software/coreutils/tee>.

- Copy standard input to each file, and also to standard output:

`echo "example" | tee `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Append to the given files, do not overwrite:

`echo "example" | tee -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Print standard input to the terminal, and also pipe it into another program for further processing:

`echo "example" | tee `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/tty</span>` | `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xargs printf "[%s]"</span>

- Create a directory called "example", count the number of characters in "example" and write "example" to the terminal:

`echo "example" | tee >(xargs mkdir) >(wc -c)`
