---
layout: page
title: common/pio-ci (Nederlands)
description: "Bouw PlatformIO projects met een arbitraire broncode structuur."
content_hash: 217ac202e39137f5686287b2bd383d153bd8b06a
last_modified_at: 2023-12-21
related_topics:
  - title: English version
    url: /en/common/pio-ci.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pio ci

Bouw PlatformIO projects met een arbitraire broncode structuur.
Dit zal een tijdelijk project maken waar naartoe de broncode gekopieerd zal worden.
Meer informatie: <https://docs.platformio.org/en/latest/core/userguide/cmd_ci.html>.

- Bouw een PlatformIO project in de standaard systeem tijdelijke map en verwijder het naderhand:

`pio ci `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/project</span>

- Bouw een PlatformIO project en specificeer specifieke bibliotheken:

`pio ci --lib `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bibliotheek_map</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/project</span>

- Bouw een PlatformIO project en specificeer een specifiek board (`pio boards` toont ze allemaal):

`pio ci --board `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">board</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/project</span>

- Bouw een PlatformIO project in een specifieke map:

`pio ci --build-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bouw_map</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/project</span>

- Bouw een PlatformIO project en verwijder de bouwmap niet:

`pio ci --keep-build-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/project</span>

- Bouw een PlatformIO project met een specifiek configuratiebestand:

`pio ci --project-conf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/platformio.ini</span>
