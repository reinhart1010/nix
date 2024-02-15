---
layout: page
title: linux/faketime (English)
description: "Fake the system time for a command."
content_hash: a3ee2aefe33345cf98428fb7eac6478c42c156c7
last_modified_at: 2024-02-15
tldri18n_status: 2
---
# faketime

Fake the system time for a command.
More information: <https://manned.org/faketime>.

- Fake the time to this evening, before printing the result of `date`:

`faketime '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">today 23:30</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">date</span>

- Open a new `bash` shell, which uses yesterday as the current date:

`faketime '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">yesterday</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash</span>

- Simulate how a program would act next Friday night:

`faketime '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">next Friday 1 am</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/program</span>
