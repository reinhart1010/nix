---
layout: page
title: common/xz (Nederlands)
description: "Comprimeren of decomprimeren van `.xz` en `.lzma` bestanden."
content_hash: 8e432da1a3c263157aecbcdd665576438d335806
last_modified_at: 2023-12-30
related_topics:
  - title: English version
    url: /en/common/xz.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/xz.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xz

Comprimeren of decomprimeren van `.xz` en `.lzma` bestanden.
Meer informatie: <https://manned.org/xz>.

- Comprimeer een bestand gebruik makend van xz file:

`xz `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Decomprimer een xz bestand:

`xz --decompress `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.xz</span>

- Comprimeer een bestand gebruik makend van lzma:

`xz --format=lzma `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Decomprimer een lzma bestand:

`xz --decompress --format=lzma `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.lzma</span>

- Decomprimer een bestand en schrijf het naar `stdout` (impliceert `--keep`):

`xz --decompress --stdout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.xz</span>

- Comprimeer een bestand, maar verwijder het origineel niet:

`xz --keep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Comprimeer een bestand, gebruik makend van de snelste compressie:

`xz -0 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Comprimeer een bestand, gebruik makend van de beste compressie:

`xz -9 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>
