---
layout: page
title: common/cpio (italiano)
description: "Copia file da/a archivi."
content_hash: 943266115fc5fbf13210d6bebe246dd7e2d282e3
related_topics:
  - title: English version
    url: /en/common/cpio.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cpio.html
    icon: bi bi-globe
---
# cpio

Copia file da/a archivi.
Supporta i seguenti formati di archivio: cpio binario, vecchio ASCII, nuovo ASCII, crc, HPUX binario, HPUX vecchio ASCII, vecchio tar, e tar POSIX.1.
Maggiori informazioni: <https://www.gnu.org/software/cpio>.

- Accetta una lista di nomi di file da standard input ed aggiungili ad un archivio in formato binario cpio:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file3</span>`" | cpio -o > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivio.cpio</span>

- Copia tutti i file e le directory in una directory ed aggiungili ad un archivio, in modalità verbosa:

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` | cpio -ov > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivio.cpio</span>

- Estrai file da un archivio, generando le directory necessarie, in modalità verbosa:

`cpio -idv < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivio.cpio</span>
