---
layout: page
title: linux/megatools-dl (Nederlands)
description: "Download bestanden van `mega.nz`."
content_hash: be3681c50bda28b84ede7c44f3faa8d95bbe2e98
last_modified_at: 2023-11-26
related_topics:
  - title: English version
    url: /en/linux/megatools-dl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# megatools-dl

Download bestanden van `mega.nz`.
Onderdeel van de `megatools` suite.
Meer informatie: <https://megatools.megous.com/man/megatools-dl.html>.

- Download bestanden van een `mega.nz` link naar de huidige map:

`megatools-dl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://mega.nz/...</span>

- Download bestanden van eem `mega.nz` link naar een specifieke map:

`megatools-dl --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/map</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://mega.nz/...</span>

- Kies interactief welke bestanden moeten worden gedownload:

`megatools-dl --choose-files `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://mega.nz/...</span>

- Beperk de downloadsnelheid in KiB/s:

`megatools-dl --limit-speed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">speed</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://mega.nz/...</span>
