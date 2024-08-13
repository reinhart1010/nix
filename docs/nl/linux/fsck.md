---
layout: page
title: linux/fsck (Nederlands)
description: "Controleer de integriteit van een bestandssysteem of repareer het. Het bestandssysteem moet niet gemount zijn op het moment dat het commando wordt uitgevoerd."
content_hash: e4ad6b0808b5a08db796b0353c3a15cd6614f25d
last_modified_at: 2024-08-13
related_topics:
  - title: English version
    url: /en/linux/fsck.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/fsck.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/fsck.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># fsck

Controleer de integriteit van een bestandssysteem of repareer het. Het bestandssysteem moet niet gemount zijn op het moment dat het commando wordt uitgevoerd.
Meer informatie: <https://manned.org/fsck>.

- Controleer bestandssysteem `/dev/sdXN` en rapporteer beschadigde blokken:

`sudo fsck `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>

- Controleer bestandssysteem `/dev/sdXN`, rapporteer beschadigde blokken en laat de gebruiker interactief kiezen om elke blok te repareren:

`sudo fsck -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>

- Controleer bestandssysteem `/dev/sdXN`, rapporteer beschadigde blokken en repareer ze automatisch:

`sudo fsck -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>
