---
layout: page
title: common/carbon-now (English)
description: "Create beautiful images of code."
content_hash: e6820bf84e526be1f91ef7455248d00306b2493f
last_modified_at: 2022-12-04
related_topics:
  - title: 中文 version
    url: /zh/common/carbon-now.html
    icon: bi bi-globe
---
# carbon-now

Create beautiful images of code.
More information: <https://github.com/mixn/carbon-now-cli>.

- Create an image from a file using default settings:

`carbon-now `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Create an image from a text in clipboard using default settings:

`carbon-now --from-clipboard`

- Create an image from standard input using default settings:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input</span>` | carbon-now`

- Create images interactively for custom settings and optionally save a preset:

`carbon-now -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Create images from previously saved preset:

`carbon-now -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">preset</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Start at a specified line of text:

`carbon-now -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">line</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- End at a specific line of text:

`carbon-now -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">line</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Open image in a browser instead of saving:

`carbon-now --open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
