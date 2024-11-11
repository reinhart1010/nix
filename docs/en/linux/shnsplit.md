---
layout: page
title: linux/shnsplit (English)
description: "Splits audio files according to a `.cue` file."
content_hash: 895084e20021ac5bfd28740552b604a3053ab63d
last_modified_at: 2024-11-11
related_topics:
  - title: Nederlands version
    url: /nl/linux/shnsplit.html
    icon: bi bi-globe
tldri18n_status: 2
---
# shnsplit

Splits audio files according to a `.cue` file.
More information: <http://shnutils.freeshell.org/shntool/>.

- Split a `.wav` + `.cue` file into multiple files:

`shnsplit -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.cue</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.wav</span>

- Show supported formats:

`shnsplit -a`

- Split a `.flac` file into multiple files:

`shnsplit -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.cue</span>` -o flac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.flac</span>

- Split a `.wav` file into files of the form "track-number - album - title":

`shnsplit -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.cue</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.wav</span>` -t "%n - %a - %t"`
