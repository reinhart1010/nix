---
layout: page
title: common/histexpand (English)
description: "Reuse and expand the shell history in `sh`, Bash, Zsh, `rbash` and `ksh`."
content_hash: 8abb4fcac082fb41bcf724db890ecaec7a93fe6f
last_modified_at: 2024-03-10
related_topics:
  - title: español version
    url: /es/common/histexpand.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/histexpand.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/histexpand.html
    icon: bi bi-globe
tldri18n_status: 2
---
# history expansion

Reuse and expand the shell history in `sh`, Bash, Zsh, `rbash` and `ksh`.
More information: <https://www.gnu.org/software/bash/manual/html_node/History-Interaction>.

- Run the previous command as root (`!!` is replaced by the previous command):

`sudo !!`

- Run a command with the last argument of the previous command:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` !$`

- Run a command with the first argument of the previous command:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` !^`

- Run the Nth command of the history:

`!`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>

- Run the command `n` lines back in the history:

`!-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>

- Run the most recent command containing `string`:

`!?`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>`?`

- Run the previous command, replacing `string1` with `string2`:

`^`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string1</span>`^`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string2</span>`^`

- Perform a history expansion, but print the command that would be run instead of actually running it:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">!-n</span>`:p`
