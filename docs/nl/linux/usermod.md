---
layout: page
title: linux/usermod (Nederlands)
description: "Wijzig een gebruikersaccount."
content_hash: f0271c4d24cbf5ed0b5d5564f6201f079df794a9
last_modified_at: 2024-06-27
related_topics:
  - title: català version
    url: /ca/linux/usermod.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/usermod.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/usermod.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/usermod.html
    icon: bi bi-globe
tldri18n_status: 2
---
# usermod

Wijzig een gebruikersaccount.
Bekijk ook: `users`, `useradd`, `userdel`.
Meer informatie: <https://manned.org/usermod>.

- Verander een gebruikersnaam:

`sudo usermod --login `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nieuwe_gebruikersnaam</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruikersnaam</span>

- Verander een gebruikers-ID:

`sudo usermod --uid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruikersnaam</span>

- Verander een gebruikersshell:

`sudo usermod --shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/shell</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruikersnaam</span>

- Voeg een gebruiker toe aan aanvullende groepen (let op het ontbreken van spaties):

`sudo usermod --append --groups `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">groep1,groep2,...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruikersnaam</span>

- Verander een gebruikers thuismap:

`sudo usermod --move-home --home `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/nieuwe_thuismap</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruikersnaam</span>
