---
layout: page
title: common/ntfy (English)
description: "Send and receive HTTP POST notifications."
content_hash: b849b6750c889ec60d537d348f967f45a6c09e7a
last_modified_at: 2024-10-08
tldri18n_status: 2
---
# ntfy

Send and receive HTTP POST notifications.
More information: <https://github.com/binwiederhier/ntfy>.

- Send a message to the `security` topic:

`ntfy pub security "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Front door has been opened.</span>`"`

- Send with a title, priority and tags:

`ntfy publish --title="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Someone bought your item</span>`" --priority=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">high</span>` --tags=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">duck</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ebay</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Someone just bought your item: Platypus Sculpture</span>`"`

- Send at 8:30am:

`ntfy pub --at=8:30am `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">delayed_topic</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Time for school, sleepyhead...</span>`"`

- Trigger a webhook:

`ntfy trigger `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my_webhook</span>

- Subscribe to a topic (Ctrl-C to stop listening):

`ntfy sub `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">home_automation</span>

- Display help:

`ntfy --help`
