---
layout: page
title: common/printf (English)
description: "Format and print text."
content_hash: 887e16e2e754ed39a384333b8ec4c9e07ec5b9b3
last_modified_at: 2025-03-02
related_topics:
  - title: 한국어 version
    url: /ko/common/printf.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/printf.html
    icon: bi bi-globe
tldri18n_status: 2
---
# printf

Format and print text.
More information: <https://www.gnu.org/software/coreutils/manual/html_node/printf-invocation.html>.

- Print a text message:

`printf "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">%s\n</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hello world</span>`"`

- Print an integer in bold blue:

`printf "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">\e[1;34m%.3d\e[0m\n</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">42</span>

- Print a float number with the Unicode Euro sign:

`printf "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">\u20AC %.2f\n</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">123.4</span>

- Print a text message composed with environment variables:

`printf "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">var1: %s\tvar2: %s\n</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$VAR1</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$VAR2</span>`"`

- Store a formatted message in a variable (does not work on Zsh):

`printf -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">myvar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">"This is %s = %d\n" "a year" 2016</span>

- Print a hexadecimal, octal and scientific number:

`printf "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hex=%x octal=%o scientific=%e</span>`" 0x`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">FF</span>` 0`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">377</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100000</span>
