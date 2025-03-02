---
layout: page
title: common/unexpand (English)
description: "Convert spaces to tabs."
content_hash: f956a58a65761e4ae332923602db417d9439df81
last_modified_at: 2025-03-02
related_topics:
  - title: 한국어 version
    url: /ko/common/unexpand.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/unexpand.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/unexpand.html
    icon: bi bi-globe
tldri18n_status: 2
---
# unexpand

Convert spaces to tabs.
More information: <https://www.gnu.org/software/coreutils/manual/html_node/unexpand-invocation.html>.

- Convert blanks in each file to tabs, writing to `stdout`:

`unexpand `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Convert blanks to tabs, reading from `stdout`:

`unexpand`

- Convert all blanks, instead of just initial blanks:

`unexpand -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Convert only leading sequences of blanks (overrides -a):

`unexpand --first-only `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Have tabs a certain number of characters apart, not 8 (enables -a):

`unexpand -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
