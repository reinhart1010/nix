---
layout: page
title: common/ssh-agent (English)
description: "Spawn an SSH Agent process."
content_hash: fd9873092820d1d1d641e3dbd94d53f32f0d0d1a
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/ssh-agent.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ssh-agent.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ssh-agent.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ssh-agent

Spawn an SSH Agent process.
An SSH Agent holds SSH keys decrypted in memory until removed or the process is killed.
See also `ssh-add`, which can add and manage keys held by an SSH Agent.
More information: <https://man.openbsd.org/ssh-agent>.

- Start an SSH Agent for the current shell:

`eval $(ssh-agent)`

- Kill the currently running agent:

`ssh-agent -k`
