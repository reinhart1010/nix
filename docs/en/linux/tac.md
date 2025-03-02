---
layout: page
title: linux/tac (English)
description: "Display and concatenate files with lines in reversed order."
content_hash: 9b4ac81b4c5c0095e797e19edfb60a66b03e94ae
last_modified_at: 2025-03-02
related_topics:
  - title: español version
    url: /es/linux/tac.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/tac.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/tac.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tac

Display and concatenate files with lines in reversed order.
See also: `cat`.
More information: <https://www.gnu.org/software/coreutils/manual/html_node/tac-invocation.html>.

- Concatenate specific files in reversed order:

`tac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Display `stdin` in reversed order:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cat path/to/file</span>` | tac`

- Use a specific separator:

`tac --separator `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">,</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Use a specific regex as a separator:

`tac --regex --separator `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">[,;]</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Use a separator before each file:

`tac --before `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>
