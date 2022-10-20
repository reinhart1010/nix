---
layout: page
title: common/gocryptfs (italiano)
description: "Filesystem crittografato scritto in Go."
content_hash: 6f1513c42dd9afc5c780293b7b21dfe759853528
related_topics:
  - title: English version
    url: /en/common/gocryptfs.html
    icon: bi bi-globe
---
# gocryptfs

Filesystem crittografato scritto in Go.
Maggiori informazioni: <https://github.com/rfjakob/gocryptfs>.

- Inizializzare un filesystem crittografato:

`gocryptfs -init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/directory_cifrata</span>

- Montare un filesystem crittografato:

`gocryptfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/directory_cifrata</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/punto_di_mount</span>

- Montare un filesystem usando la master key invece della password:

`gocryptfs --masterkey `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/directory_cifrata</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/punto_di_mount</span>

- Cambiare la password:

`gocryptfs --passwd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/directory_cifrata</span>

- Generare uno snapshot cifrato di una directory:

`gocryptfs --reverse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/directory_cifrata</span>
