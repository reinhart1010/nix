---
layout: page
title: common/pio-account (Nederlands)
description: "Beheer jouw PlatformIO account op de command-line."
content_hash: 6a373711569a4687c2283ac119c3325fefeca823
last_modified_at: 2023-12-21
related_topics:
  - title: English version
    url: /en/common/pio-account.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pio account

Beheer jouw PlatformIO account op de command-line.
Meer informatie: <https://docs.platformio.org/en/latest/core/userguide/account/>.

- Registreer een nieuw PlatformIO account:

`pio account register --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruikersnaam</span>` --email `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">email</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wachtwoord</span>` --firstname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">voornaam</span>` --lastname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">achternaam</span>

- Verwijder permanent je PlatformIO account en gerelateerde data:

`pio account destroy`

- Log in bij je PlatformIO account:

`pio account login --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruikersnaam</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wachtwoord</span>

- Log uit bij je PlatformIO account:

`pio account logout`

- Update je PlatformIO profiel:

`pio account update --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruikersnaam</span>` --email `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">email</span>` --firstname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">voornaam</span>` --lastname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">achternaam</span>` --current-password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wachtwoord</span>

- Toon gedetailleerde informatie over je PlatformIO account:

`pio account show`

- Reset je wachtwoord door gebruik te maken van je gebruikersnaam of email:

`pio account forgot --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruikersnaam_of_email</span>
