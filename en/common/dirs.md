---
layout: page
title: common/dirs (English)
description: "Displays or manipulates the directory stack."
content_hash: b1635620e68c51fd4b8444a40e241eb8f502fe79
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
---
# dirs

Displays or manipulates the directory stack.
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
