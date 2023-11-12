---
layout: page
title: common/cpio (italiano)
description: "Copia file da/a archivi."
content_hash: a5a9050194788f74e8af7a82f477e6f52c70e6ba
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/cpio.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cpio.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cpio

Copia file da/a archivi.
Supporta i seguenti formati di archivio: cpio binario, vecchio ASCII, nuovo ASCII, crc, HPUX binario, HPUX vecchio ASCII, vecchio tar, e tar POSIX.1.
Maggiori informazioni: <https://www.gnu.org/software/cpio>.

- Accetta una lista di nomi di file da standard input ed aggiungili ad un archivio in formato binario cpio:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file3</span>`" | cpio -o > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivio.cpio</span>

- Copia tutti i file e le directory in una directory ed aggiungili ad un archivio, in modalità verbosa:

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/directory</span>` | cpio -ov > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivio.cpio</span>

- Estrai file da un archivio, generando le directory necessarie, in modalità verbosa:

`cpio -idv < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivio.cpio</span>
