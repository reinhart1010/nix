---
layout: page
title: osx/fsck (Nederlands)
description: "Controleer de integriteit van een bestandssysteem of repareer het. Het bestandssysteem moet niet gemount zijn op het moment dat het commando wordt uitgevoerd."
content_hash: 34eb7e2ab9044535faa6133535b535b4aef8c3f0
last_modified_at: 2024-08-14
related_topics:
  - title: English version
    url: /en/osx/fsck.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/fsck.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/fsck.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/fsck.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fsck

Controleer de integriteit van een bestandssysteem of repareer het. Het bestandssysteem moet niet gemount zijn op het moment dat het commando wordt uitgevoerd.
Het is een wrapper die `fsck_hfs`, `fsck_apfs`, `fsck_msdos`, `fsck_exfat` en `fsck_udf` aanroept indien nodig.
Meer informatie: <https://keith.github.io/xcode-man-pages/fsck.8.html>.

- Controleer bestandssysteem `/dev/sdX` en rapporteer beschadigde blokken:

`fsck `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- Controleer bestandssysteem `/dev/sdX` alleen als het schoon is, rapporteer beschadigde blokken en laat de gebruiker interactief kiezen om elke blok te repareren:

`fsck -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- Controleer bestandssysteem `/dev/sdX` alleen als het schoon is, rapporteer beschadigde blokken en repareer ze automatisch:

`fsck -fy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- Controleer bestandssysteem `/dev/sdX` en rapporteer of het schoon is afgekoppeld:

`fsck -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>
