---
layout: page
title: common/zstd (Nederlands)
description: "Bestanden comprimeren of decomprimeren met Zstandard compressie."
content_hash: e7a2795b0c2165d97ccd4214d15741392767de98
last_modified_at: 2023-11-26
related_topics:
  - title: English version
    url: /en/common/zstd.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/zstd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# zstd

Bestanden comprimeren of decomprimeren met Zstandard compressie.
Meer informatie: <https://github.com/facebook/zstd>.

- Comprimeer een bestand naar een nieuw bestand met de `.zst` extensie:

`zstd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Decomprimeer een bestand:

`zstd --decompress `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.zst</span>

- Decomprimeer naar `stdout`:

`zstd --decompress --stdout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.zst</span>

- Comprimeer een bestand met een specifiek compressie level, waar 1=snelste, 19=langzaamste en 3=standaard:

`zstd -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">level</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Ontgrendel hogere compressieniveaus (tot en met 22) door gebruik te maken van meer geheugen (voor compressie en decompression):

`zstd --ultra -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">level</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>
