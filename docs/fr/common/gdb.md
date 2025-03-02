---
layout: page
title: common/gdb (français)
description: "Le débogueur GNU."
content_hash: 8039f3e29607d1712a1279361cf4b8e743de6cd1
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/common/gdb.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/gdb.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/gdb.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/gdb.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/gdb.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># gdb

Le débogueur GNU.
Plus d'informations : <https://www.gnu.org/software/gdb>.

- Débogue un exécutable :

`gdb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">exécutable</span>

- Attache un processus à gdb :

`gdb -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identifiant_processus</span>

- Débogue avec un fichier comme image mémoire :

`gdb -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">exécutable</span>

- Execute les commandes gdb données au démarrage :

`gdb -ex "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commandes</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">exécutable</span>

- Démarre gdb en passant des arguments à l'exécutable :

`gdb --args `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">exécutable</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argument1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argument2</span>
