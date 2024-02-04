---
layout: page
title: linux/umount (Nederlands)
description: "Koppel een bestandssysteem los vanuit het mount-punt, waardoor het niet langer toegankelijk is."
content_hash: d137cad968ecdc6425d879cb11714d947cca8cbb
last_modified_at: 2024-02-04
related_topics:
  - title: English version
    url: /en/linux/umount.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/umount.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># umount

Koppel een bestandssysteem los vanuit het mount-punt, waardoor het niet langer toegankelijk is.
Een bestandssysteem kan niet losgekoppeld worden als het bezig is.
Meer informatie: <https://manned.org/umount.8>.

- Koppel een bestandssysteem los door het pad op te geven van de bron waarop het gemount is:

`umount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/apparaat_bestand</span>

- Koppel een bestandssysteem los door het pad op te geven waarop het gemount is:

`umount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/gemounte_map</span>

- Als het loskoppelen faalt, probeer het bestandssysteem dan opnieuw te koppelen in leesmodus:

`umount --read-only `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/gemounte_map</span>

- Koppel ieder gespecificeerde map recursief los:

`umount --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/gemounte_map</span>

- Koppel alle gemounte bestandssystemen los (behalve het `proc` bestandssysteem):

`umount -a`
