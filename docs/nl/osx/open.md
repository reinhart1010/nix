---
layout: page
title: osx/open (Nederlands)
description: "Open bestanden, mappen en applicaties."
content_hash: 909611920d48e5c42c73a274e2c9a5abdf32269d
last_modified_at: 2024-08-21
related_topics:
  - title: Deutsch version
    url: /de/osx/open.html
    icon: bi bi-globe
  - title: English version
    url: /en/osx/open.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/open.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/osx/open.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/open.html
    icon: bi bi-globe
tldri18n_status: 2
---
# open

Open bestanden, mappen en applicaties.
Meer informatie: <https://keith.github.io/xcode-man-pages/open.1.html>.

- Open een bestand met de bijbehorende applicatie:

`open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bestand.ext</span>

- Start een grafische macOS-[a]pplicatie:

`open -a "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Applicatie</span>`"`

- Start een grafische macOS-app op basis van de [b]undle-identificator (raadpleeg `osascript` voor een eenvoudige manier om deze te verkrijgen):

`open -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.domein.applicatie</span>

- Open de huidige map in Finder:

`open .`

- Toon ([R]) een bestand in Finder:

`open -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Open alle bestanden met een bepaalde extensie in de huidige map met de bijbehorende applicatie:

`open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.ext</span>

- Open een [n]ieuw exemplaar van een applicatie gespecificeerd via de [b]undle-identificator:

`open -n -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.domein.applicatie</span>
