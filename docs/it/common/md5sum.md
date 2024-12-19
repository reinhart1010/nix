---
layout: page
title: common/md5sum (italiano)
description: "Calcola i checksum crittografici di tipo MD5."
content_hash: 2cbb51603b72fdfdaed1d7fbfbb34cede407ea74
last_modified_at: 2024-12-19
related_topics:
  - title: English version
    url: /en/common/md5sum.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/md5sum.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/md5sum.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/md5sum.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/md5sum.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># md5sum

Calcola i checksum crittografici di tipo MD5.
Maggiori informazioni: <https://www.gnu.org/software/coreutils/manual/html_node/md5sum-invocation.html>.

- Calcolare il checksum MD5 di un file:

`md5sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file</span>

- Calcola i checksum MD5 per più di un file:

`md5sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file2</span>

- Verifica che tutti i file abbiano checksum corrispondenti al file di MD5SUM:

`md5sum -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file.md5</span>

- Calcola il checksum MD5 dal standard input:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">testo</span>`" | md5sum`
