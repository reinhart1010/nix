---
layout: page
title: common/gocryptfs (italiano)
description: "Filesystem crittografato scritto in Go."
content_hash: a72a3070c1fd1ab11b2653458c0176aa6b006577
related_topics:
  - title: English version
    url: /en/common/gocryptfs.html
    icon: bi bi-globe
---
# gocryptfs

Filesystem crittografato scritto in Go.
Maggiori informazioni: <https://github.com/rfjakob/gocryptfs>.

- Inizializzare un filesystem crittografato:

`gocryptfs -init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/cifrata</span>

- Montare un filesystem crittografato:

`gocryptfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/cartella/cifrata</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/punto/di/mount</span>

- Montare un filesystem usando la master key invece della password:

`gocryptfs --masterkey `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/cartella/cifrata</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/punto/di/mount</span>

- Cambiare la password:

`gocryptfs --passwd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/cartella/cifrata</span>

- Generare uno snapshot cifrato di una cartella:

`gocryptfs --reverse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/cartella/cifrata</span>
