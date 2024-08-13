---
layout: page
title: windows/finger (Nederlands)
description: "Geeft informatie over gebruikers op een opgegeven systeem."
content_hash: 1722ddc0017417e2c318c91dd9f1c94502ce4478
last_modified_at: 2024-08-13
related_topics:
  - title: English version
    url: /en/windows/finger.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/finger.html
    icon: bi bi-globe
tldri18n_status: 2
---
# finger

Geeft informatie over gebruikers op een opgegeven systeem.
Het externe systeem moet de Finger-service draaien.
Meer informatie: <https://learn.microsoft.com/windows-server/administration/windows-commands/finger>.

- Toon informatie over een specifieke gebruiker:

`finger `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruiker</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Toon informatie over alle gebruikers op de opgegeven host:

`finger @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Toon informatie in een langere indeling:

`finger `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruiker</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>` -l`

- Toon helpinformatie:

`finger /?`
