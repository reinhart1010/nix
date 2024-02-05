---
layout: page
title: linux/umount (Nederlands)
description: "Koppel een bestandssysteem los vanuit het mount-punt, waardoor het niet langer toegankelijk is."
content_hash: d137cad968ecdc6425d879cb11714d947cca8cbb
last_modified_at: 2024-02-05
related_topics:
  - title: English version
    url: /en/linux/umount.html
    icon: bi bi-globe
tldri18n_status: 2
---
# umount

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
