---
layout: page
title: common/md5sum (italiano)
description: "Calcola i checksum crittografici di tipo MD5."
content_hash: ab19ea2ef875fbcf31594ac28f88797d2dde3b8d
related_topics:
  - title: English version
    url: /en/common/md5sum.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/md5sum.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/md5sum.html
    icon: bi bi-globe
---
# md5sum

Calcola i checksum crittografici di tipo MD5.
Maggiori informazioni: <https://www.gnu.org/software/coreutils/md5sum>.

- Calcolare il checksum MD5 di un file:

`md5sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file</span>

- Calcola i checksum MD5 per più di un file:

`md5sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file2</span>

- Verifica che tutti i file abbiano checksum corrispondenti al file di MD5SUM:

`md5sum -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file.md5</span>

- Calcola il checksum MD5 dal standard input:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">testo</span>`" | md5sum`
