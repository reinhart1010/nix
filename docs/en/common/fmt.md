---
layout: page
title: common/fmt (English)
description: "Reformat a text file by joining its paragraphs and limiting the line width to a number of characters (75 by default)."
content_hash: 6b135427027eab3c8843c014b2207d8954ae27ee
last_modified_at: 2025-03-02
related_topics:
  - title: italiano version
    url: /it/common/fmt.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/fmt.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/fmt.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/fmt.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fmt

Reformat a text file by joining its paragraphs and limiting the line width to a number of characters (75 by default).
More information: <https://www.gnu.org/software/coreutils/manual/html_node/fmt-invocation.html>.

- Reformat a file:

`fmt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Reformat a file producing output lines of (at most) `n` characters:

`fmt -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Reformat a file without joining lines shorter than the given width together:

`fmt -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Reformat a file with uniform spacing (1 space between words and 2 spaces between paragraphs):

`fmt -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
