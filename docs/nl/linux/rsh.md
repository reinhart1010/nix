---
layout: page
title: linux/rsh (Nederlands)
description: "Voer commando's uit op een externe host."
content_hash: 8c547861145522d9c225aa38cfb7557ff3bc49e6
last_modified_at: 2024-06-26
related_topics:
  - title: English version
    url: /en/linux/rsh.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rsh

Voer commando's uit op een externe host.
Meer informatie: <https://www.gnu.org/software/inetutils/manual/html_node/rsh-invocation.html>.

- Voer een commando uit op een externe host:

`rsh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_host</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls -l</span>

- Voer een commando uit op een externe host met een specifieke gebruikersnaam:

`rsh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_host</span>` -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruikersnaam</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls -l</span>

- Redirect `stdin` naar `/dev/null` bij het uitvoeren van een commando op een externe host:

`rsh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_host</span>` --no-err `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls -l</span>
