---
layout: page
title: linux/groupmod (Nederlands)
description: "Wijzig bestaande gebruikersgroepen in het systeem."
content_hash: 4f5b7db7e0491f768babb1d2fc8f790ffdc30e4a
last_modified_at: 2024-06-19
related_topics:
  - title: English version
    url: /en/linux/groupmod.html
    icon: bi bi-globe
tldri18n_status: 2
---
# groupmod

Wijzig bestaande gebruikersgroepen in het systeem.
Zie ook: `groups`, `groupadd`, `groupdel`.
Meer informatie: <https://manned.org/groupmod>.

- Wijzig de groepsnaam:

`sudo groupmod --new-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nieuwe_groep</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">groepsnaam</span>

- Wijzig het groeps-ID:

`sudo groupmod --gid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nieuwe_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">groepsnaam</span>
