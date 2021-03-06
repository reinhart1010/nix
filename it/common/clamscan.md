---
layout: page
title: common/clamscan (italiano)
description: "Scanner antivirus da linea di comando."
content_hash: d972f8ecae854a5c4295aa3652873f12983e6c00
related_topics:
  - title: English version
    url: /en/common/clamscan.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/clamscan.html
    icon: bi bi-globe
---
# clamscan

Scanner antivirus da linea di comando.
Maggiori informazioni: <https://www.clamav.net>.

- Analizza un file cercando vulnerabilità:

`clamscan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file</span>

- Analizza ricorsivamente tutti i file in una specifica directory:

`clamscan -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/alla/directory</span>

- Analizza dati da standard input:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` | clamscan -`

- Specifica un file o directory di file da usare come database virus:

`clamscan --database `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/a/file_o_directory</span>

- Analizza la directory corrente e mostra in output solo i file infetti:

`clamscan --infected`

- Scrivi il risultato di uno scan in un file di log:

`clamscan --log `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/a/file_log</span>

- Sposta i file infetti in una specifica directory:

`clamscan --move `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/a/directory_quarantena</span>

- Elimina i file infetti:

`clamscan --remove yes`
