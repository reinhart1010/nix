---
layout: page
title: common/visudo (Nederlands)
description: "Bewerk veilig het sudoers-bestand."
content_hash: c70e757d1076dcf2c74a400992ce7b30cc4e1a87
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/visudo.html
    icon: bi bi-globe
  - title: svenska version
    url: /sv/common/visudo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# visudo

Bewerk veilig het sudoers-bestand.
Meer informatie: <https://www.sudo.ws/docs/man/visudo.man>.

- Bewerk sudoers-bestand:

`sudo visudo`

- Controleer sudoers-bestand op fouten:

`sudo visudo -c`

- Bewerk het sudoers-bestand met een specifieke editor:

`sudo EDITOR=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">editor</span>` visudo`

- Toon versie informatie:

`visudo --version`
