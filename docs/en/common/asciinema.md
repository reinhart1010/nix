---
layout: page
title: common/asciinema (English)
description: "Record and replay terminal sessions, and optionally share them on <https://asciinema.org>."
content_hash: d53456d409e39ce84f778d9ed3ecbb6c6fa3e623
last_modified_at: 2024-09-25
related_topics:
  - title: español version
    url: /es/common/asciinema.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/asciinema.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/asciinema.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/asciinema.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/asciinema.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/asciinema.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/asciinema.html
    icon: bi bi-globe
tldri18n_status: 2
---
# asciinema

Record and replay terminal sessions, and optionally share them on <https://asciinema.org>.
See also: `terminalizer`.
More information: <https://docs.asciinema.org/manual/cli/usage>.

- Associate the local install of `asciinema` with an asciinema.org account:

`asciinema auth`

- Make a new recording (finish it with `Ctrl+D` or type `exit`, and then choose to upload it or save it locally):

`asciinema rec`

- Make a new recording and save it to a local file:

`asciinema rec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/recording.cast</span>

- Replay a terminal recording from a local file:

`asciinema play `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/recording.cast</span>

- Replay a terminal recording hosted on <https://asciinema.org>:

`asciinema play https://asciinema.org/a/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cast_id</span>

- Make a new recording, limiting any [i]dle time to at most 2.5 seconds:

`asciinema rec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-i|--idle-time-limit</span>` 2.5`

- Print the full output of a locally saved recording:

`asciinema cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/recording.cast</span>

- Upload a locally saved terminal session to asciinema.org:

`asciinema upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/recording.cast</span>
