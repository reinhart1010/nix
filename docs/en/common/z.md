---
layout: page
title: common/z (English)
description: "Tracks the most used (by frequency) directories and enables quickly navigating to them using string patterns or regular expressions."
content_hash: d4eaa7c52a23d7fb636ff12d87eb9cde8c2d62cb
last_modified_at: 2024-11-08
related_topics:
  - title: français version
    url: /fr/common/z.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/z.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/z.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/z.html
    icon: bi bi-globe
tldri18n_status: 2
---
# z

Tracks the most used (by frequency) directories and enables quickly navigating to them using string patterns or regular expressions.
More information: <https://github.com/rupa/z>.

- Go to a directory that contains "foo" in the name:

`z `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>

- Go to a directory that contains "foo" and then "bar":

`z `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bar</span>

- Go to the highest-ranked directory matching "foo":

`z -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>

- Go to the most recently accessed directory matching "foo":

`z -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>

- List all directories in `z`'s database matching "foo":

`z -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>

- Remove the current directory from `z`'s database:

`z -x`

- Restrict matches to subdirectories of the current directory:

`z -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>
