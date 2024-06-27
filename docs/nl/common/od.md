---
layout: page
title: common/od (Nederlands)
description: "Toon bestandsinhoud in octale, decimale of hexadecimale notatie."
content_hash: 8b6cd71478f48f9e7a5ecd9eb24d1a2400bb8d10
last_modified_at: 2024-06-27
related_topics:
  - title: English version
    url: /en/common/od.html
    icon: bi bi-globe
tldri18n_status: 2
---
# od

Toon bestandsinhoud in octale, decimale of hexadecimale notatie.
Toon optioneel de byte-offsets en/of de afdrukbare weergave voor elke regel.
Meer informatie: <https://www.gnu.org/software/coreutils/od>.

- Toon bestand met de standaardinstellingen: octale notatie, 8 bytes per regel, byte-offsets in octale notatie en dubbele regels vervangen door `*`:

`od `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Toon bestand in uitgebreide modus, d.w.z. zonder dubbele regels te vervangen door `*`:

`od -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Toon bestand in hexadecimale notatie (2-byte eenheden), met byte-offsets in decimale notatie:

`od --format=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x</span>` --address-radix=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">d</span>` -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Toon bestand in hexadecimale notatie (1-byte eenheden) en 4 bytes per regel:

`od --format=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x1</span>` --width=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Toon bestand in hexadecimale notatie samen met de tekenweergave, en toon geen byte-offsets:

`od --format=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xz</span>` --address-radix=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Lees slechts 100 bytes van een bestand vanaf de 500ste byte:

`od --read-bytes 100 --skip-bytes=500 -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>
