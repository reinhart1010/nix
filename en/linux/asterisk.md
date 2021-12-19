---
layout: page
title: linux/asterisk (English)
description: "Telephone and exchange (phone) server."
content_hash: f84187ceb0a287cc77ae6b5dc8e69a93e06ab731
related_topics:
  - title: 中文 version
    url: /zh/linux/asterisk.html
    icon: bi bi-globe
---
# asterisk

Telephone and exchange (phone) server.
Used for running the server itself, and managing an already running instance.
More information: <https://wiki.asterisk.org/wiki/display/AST/Home>.

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
