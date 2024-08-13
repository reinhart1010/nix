---
layout: page
title: linux/at (Nederlands)
description: "Voert commando's uit op een gespecificeerd tijdstip."
content_hash: aad6de4c4ab67c7fb9139c20eb626fa41149bae5
last_modified_at: 2024-08-13
related_topics:
  - title: English version
    url: /en/linux/at.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/at.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/at.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/at.html
    icon: bi bi-globe
tldri18n_status: 2
---
# at

Voert commando's uit op een gespecificeerd tijdstip.
Meer informatie: <https://man.archlinux.org/man/at.1>.

- Open een `at`-prompt om een nieuwe reeks geplande commando's te maken, druk op `Ctrl + D` om op te slaan en af te sluiten:

`at `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hh:mm</span>

- Voer de commando's uit en e-mail het resultaat met behulp van een lokaal mailprogramma zoals Sendmail:

`at `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hh:mm</span>` -m`

- Voer een script uit op het opgegeven tijdstip:

`at `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hh:mm</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Toon een systeembericht om 23:00 op 18 februari:

`echo "notify-send '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Wake up!</span>`'" | at `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">11pm</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Feb 18</span>
