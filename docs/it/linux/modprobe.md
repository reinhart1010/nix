---
layout: page
title: linux/modprobe (italiano)
description: "Aggiunge o rimuove moduli del kernel Linux."
content_hash: 9e78c486eab258fad53f3030c5a6966f5a5eae00
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/modprobe.html
    icon: bi bi-globe
tldri18n_status: 2
---
# modprobe

Aggiunge o rimuove moduli del kernel Linux.
Maggiori informazioni: <https://manned.org/modprobe>.

- Fa finta di carica un modulo nel kernel, ma non lo fa veramente:

`sudo modprobe --dry-run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_del_modulo</span>

- Carica un modulo nel kernel:

`sudo modprobe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_del_modulo</span>

- Rimuove un modulo dal kernel:

`sudo modprobe --remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_del_modulo</span>

- Rimuove dal kernel un modulo e quelli che dipendono da quest'ultimo:

`sudo modprobe --remove-dependencies `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_del_modulo</span>

- Mostra le dipendenza di un modulo del kernel:

`sudo modprobe --show-depends `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_del_modulo</span>
