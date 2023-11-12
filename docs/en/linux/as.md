---
layout: page
title: linux/as (English)
description: "Portable GNU assembler."
content_hash: 2908ece6b3703029a69bfd17507821bc158536f4
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/linux/as.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/as.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/as.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/as.html
    icon: bi bi-globe
tldri18n_status: 2
---
# as

Portable GNU assembler.
Primarily intended to assemble output from `gcc` to be used by `ld`.
More information: <https://manned.org/as>.

- Assemble a file, writing the output to `a.out`:

`as `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.s</span>

- Assemble the output to a given file:

`as `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.s</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">out.o</span>

- Generate output faster by skipping whitespace and comment preprocessing. (Should only be used for trusted compilers):

`as -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.s</span>

- Include a given path to the list of directories to search for files specified in `.include` directives:

`as -I `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.s</span>
