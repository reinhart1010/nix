---
layout: page
title: common/moro (English)
description: "Track work time."
content_hash: fde2a0ded9a0d74333887053c6eaa8fcf7fb3c22
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# moro

Track work time.
More information: <https://moro.js.org>.

- Invoke `moro` without parameters, to set the current time as the start of the working day:

`moro`

- Specify a custom time for the start of the working day:

`moro hi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">09:30</span>

- Invoke `moro` without parameters a second time, to set the current time at the end of the working day:

`moro`

- Specify a custom time for the end of the working day:

`moro bye `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">17:30</span>

- Add a note on the current working day:

`moro note `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3 hours on project Foo</span>

- Show a report of time logs and notes for the current working day:

`moro report`

- Show a report of time logs and notes for all working days on record:

`moro report --all`
