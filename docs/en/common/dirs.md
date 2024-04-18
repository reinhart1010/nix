---
layout: page
title: common/dirs (English)
description: "Display or manipulate the directory stack."
content_hash: 4a8cdde1b435b4e3343cf1800b540b684d7d245d
last_modified_at: 2024-04-18
related_topics:
  - title: Deutsch version
    url: /de/common/dirs.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/dirs.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/dirs.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/dirs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dirs

Display or manipulate the directory stack.
The directory stack is a list of recently visited directories that can be manipulated with the `pushd` and `popd` commands.
More information: <https://www.gnu.org/software/bash/manual/bash.html#Directory-Stack-Builtins>.

- Display the directory stack with a space between each entry:

`dirs`

- Display the directory stack with one entry per line:

`dirs -p`

- Display only the nth entry in the directory stack, starting at 0:

`dirs +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">N</span>

- Clear the directory stack:

`dirs -c`
