---
layout: page
title: common/detox (English)
description: "Renames files to make them easier to work with."
content_hash: 4576d2b32626af2379001b5d5ed91c32507d37a2
related_topics:
  - title: italiano version
    url: /it/common/detox.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/detox.html
    icon: bi bi-globe
---
# detox

Renames files to make them easier to work with.
It removes spaces and other such annoyances like duplicate underline characters.
More information: <https://github.com/dharple/detox>.

- Remove spaces and other undesirable characters from a file's name:

`detox `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Show how detox would rename all the files in a directory tree:

`detox --dry-run -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">directory</span>

- Remove spaces and other undesirable characters from all files in a directory tree:

`detox -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">directory</span>
