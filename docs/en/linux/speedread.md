---
layout: page
title: linux/speedread (English)
description: "A simple terminal-based open source Spritz-alike."
content_hash: 35f66821c76d28093695e611409c47f2abf6f8fb
last_modified_at: 2023-11-26
tldri18n_status: 2
---
# speedread

A simple terminal-based open source Spritz-alike.
Shows input text as a per-word RSVP (rapid serial visual presentation) aligned on optimal reading points, which allows reading text at a much more rapid pace than usual as the eye can stay fixed on a single place.
More information: <https://github.com/pasky/speedread>.

- Read a text file at a specific speed:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.txt</span>` | speedread -wpm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">250</span>

- Resume from a specific line:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.txt</span>` | speedread -resume `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>

- Show multiple words at a time:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.txt</span>` | speedread -multiword`

- Slow down by 10% during the reading session:

`[`

- Speed up by 10% during the reading session:

`]`

- Pause, and show the last few lines as context:

`<space>`
