---
layout: page
title: common/flock (Nederlands)
description: "Beheer sloten van shell scripts."
content_hash: 1971b3c67e83041f4ef10124eca87bf4d22632f2
last_modified_at: 2024-01-26
related_topics:
  - title: English version
    url: /en/common/flock.html
    icon: bi bi-globe
tldri18n_status: 2
---
# flock

Beheer sloten van shell scripts.
Het kan worden gebruikt om ervoor te zorgen dat slechts één proces van een commando wordt uitgevoerd.
Meer informatie: <https://manned.org/flock>.

- Voer een commando uit met een bestandslot zodra het slot niet vereist is door anderen:

`flock `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/lock.lock</span>` --command "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>`"`

- Voer een commando uit met een bestandslot en stop als het slot niet bestaat:

`flock `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/lock.lock</span>` --nonblock --command "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>`"`

- Voer een commando uit met een bestandslot en stop met een specifieke error code als het slot niet bestaat:

`flock `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/lock.lock</span>` --nonblock --conflict-exit-code `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">error_code</span>` -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>`"`
