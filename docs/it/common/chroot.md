---
layout: page
title: common/chroot (italiano)
description: "Esegui un comando o una shell interattiva con una speciale directory root."
content_hash: f1bfa19c126511f30d7130f58283864cb7e76bdf
last_modified_at: 2024-12-12
related_topics:
  - title: Deutsch version
    url: /de/common/chroot.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/chroot.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/chroot.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/chroot.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/chroot.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/chroot.html
    icon: bi bi-globe
tldri18n_status: 2
---
# chroot

Esegui un comando o una shell interattiva con una speciale directory root.
Maggiori informazioni: <https://www.gnu.org/software/coreutils/manual/html_node/chroot-invocation.html>.

- Esegui un comando con una diversa directory root:

`chroot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/percorso/della/nuova/root</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

- Specifica utente e gruppo (ID o nome) da usare:

`chroot --userspec=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">utente:gruppo</span>
