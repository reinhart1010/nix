---
layout: page
title: common/pio-org (Nederlands)
description: "Beheer PlatformIO organisaties en hun eigenaren."
content_hash: 78e82ec2b630c2212f8106b2de4461b73cdc63aa
last_modified_at: 2023-12-21
related_topics:
  - title: English version
    url: /en/common/pio-org.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pio org

Beheer PlatformIO organisaties en hun eigenaren.
Meer informatie: <https://docs.platformio.org/en/latest/core/userguide/org/>.

- Maak een nieuwe organisatie:

`pio org create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">organisatie_naam</span>

- Verwijder een organisatie:

`pio org destroy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">organisatie_naam</span>

- Voeg een gebruiker toe aan een organisatie:

`pio org add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">organisatie_naam</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruikersnaam</span>

- Verwijder een gebruiker van een organisatie:

`pio org remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">organisatie_naam</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruikersnaam</span>

- Toon alle organisaties waar de huidige gebruiker lid van is en de eigenaren:

`pio org list`

- Update de name, email of weergave naam van een organisatie:

`pio org update --orgname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nieuwe_organisatie_naam</span>` --email `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nieuw_email</span>` --displayname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nieuwe_weergave_naam</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">organisatie_naam</span>
