---
layout: page
title: common/nm (Nederlands)
description: "Toon symbool namen in object bestanden."
content_hash: b79285b397a022f88163d5b499758301dd719741
last_modified_at: 2023-11-26
related_topics:
  - title: English version
    url: /en/common/nm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nm

Toon symbool namen in object bestanden.
Meer informatie: <https://manned.org/nm>.

- Toon globale (externe) functies in een bestand (voorafgegaan door T):

`nm -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.o</span>

- Toon alleen ongedefinieerde symbolen in een bestand:

`nm -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.o</span>

- Toon alle symbolen, ook debugging symbolen:

`nm -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.o</span>

- Transformeer C++ symbolen (maak ze leesbaar):

`nm --demangle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.o</span>
