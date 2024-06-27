---
layout: page
title: linux/userdel (Nederlands)
description: "Verwijder een gebruikersaccount of verwijder een gebruiker uit een groep."
content_hash: e03af0facf2d1f9fec93c1df18d48e7125444a29
last_modified_at: 2024-06-27
related_topics:
  - title: català version
    url: /ca/linux/userdel.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/userdel.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/userdel.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/userdel.html
    icon: bi bi-globe
tldri18n_status: 2
---
# userdel

Verwijder een gebruikersaccount of verwijder een gebruiker uit een groep.
Bekijk ook: `users`, `useradd`, `usermod`.
Meer informatie: <https://manned.org/userdel>.

- Verwijder een gebruiker:

`sudo userdel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruikersnaam</span>

- Verwijder een gebruiker in een andere root-map:

`sudo userdel --root `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/andere/root</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruikersnaam</span>

- Verwijder een gebruiker samen met de thuismap en mail-spool:

`sudo userdel --remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruikersnaam</span>
