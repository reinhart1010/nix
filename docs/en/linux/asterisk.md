---
layout: page
title: linux/asterisk (English)
description: "Run and manage telephone and exchange (phone) server instances."
content_hash: 699590841aa6ca98ce7bcc1125341d181062c5c8
last_modified_at: 2024-05-28
related_topics:
  - title: 中文 version
    url: /zh/linux/asterisk.html
    icon: bi bi-globe
tldri18n_status: 2
---
# asterisk

Run and manage telephone and exchange (phone) server instances.
More information: <https://docs.asterisk.org>.

- [R]econnect to a running server, and turn on logging 3 levels of [v]erbosity:

`asterisk -r -vvv`

- [R]econnect to a running server, run a single command, and return:

`asterisk -r -x "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>`"`

- Show chan_SIP clients (phones):

`asterisk -r -x "sip show peers"`

- Show active calls and channels:

`asterisk -r -x "core show channels"`

- Show voicemail mailboxes:

`asterisk -r -x "voicemail show users"`

- Terminate a channel:

`asterisk -r -x "hangup request `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">channel_ID</span>`"`

- Reload chan_SIP configuration:

`asterisk -r -x "sip reload"`
