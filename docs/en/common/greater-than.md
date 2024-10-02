---
layout: page
title: common/greater-than (English)
description: "Redirect output to a file."
content_hash: 5316ae041de586b8908e45aaa922e7ba62799b4d
last_modified_at: 2024-10-02
tldri18n_status: 2
---
# Greater than

Redirect output to a file.
More information: <https://gnu.org/software/bash/manual/bash.html#Redirecting-Output>.

- Redirect `stdout` to a file:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Append to a file:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` >> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Redirect both `stdout` and `stderr` to a file:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` &> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Redirect both `stdout` and `stderr` to `/dev/null` to keep the terminal output clean:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` &> /dev/null`
