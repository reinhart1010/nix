---
layout: page
title: common/tail (English)
description: "Display the last part of a file."
content_hash: 4d217ebd9f6d1c61705a60e7b046979c89dfff9e
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/tail.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/tail.html
    icon: bi bi-globe
  - title: sh version
    url: /sh/common/tail.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tail

Display the last part of a file.
See also: `head`.
More information: <https://www.gnu.org/software/coreutils/tail>.

- Show last 'count' lines in file:

`tail --lines `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">count</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Print a file from a specific line number:

`tail --lines +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">count</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Print a specific count of bytes from the end of a given file:

`tail --bytes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">count</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Print the last lines of a given file and keep reading file until `Ctrl + C`:

`tail --follow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Keep reading file until `Ctrl + C`, even if the file is inaccessible:

`tail --retry --follow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Show last 'num' lines in 'file' and refresh every 'n' seconds:

`tail --lines `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">count</span>` --sleep-interval `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">seconds</span>` --follow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
