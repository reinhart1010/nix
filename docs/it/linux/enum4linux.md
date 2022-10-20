---
layout: page
title: linux/enum4linux (italiano)
description: "Strumento per ottenere informazioni da Windows e Samba da un sistema remoto."
content_hash: 936c676eb4e2fd294fb1354eb0d7b6ea0e7e04b4
related_topics:
  - title: English version
    url: /en/linux/enum4linux.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># enum4linux

Strumento per ottenere informazioni da Windows e Samba da un sistema remoto.
Maggiori informazioni: <https://labs.portcullis.co.uk/tools/enum4linux/>.

- Ottieni informazioni utilizzando tutti i metodi disponibili:

`enum4linux -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host_remoto</span>

- Ottieni informazioni utilizzando le credenziali fornite:

`enum4linux -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_utente</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host_remoto</span>

- Ottieni la lista utenti:

`enum4linux -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host_remoto</span>

- Mostra le risorse condivise:

`enum4linux -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host_remoto</span>

- Ottieni informazioni riguardo al sistema operativo:

`enum4linux -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host_remoto</span>
