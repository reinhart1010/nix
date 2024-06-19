---
layout: page
title: osx/locate (Nederlands)
description: "Vind snel bestandsnamen."
content_hash: 8601c9de1e1433e4fc6cc25fd57647f2bf061300
last_modified_at: 2024-06-19
related_topics:
  - title: English version
    url: /en/osx/locate.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/locate.html
    icon: bi bi-globe
tldri18n_status: 2
---
# locate

Vind snel bestandsnamen.
Meer informatie: <https://keith.github.io/xcode-man-pages/locate.1.html>.

- Zoek naar een patroon in de database. Opmerking: de database wordt periodiek herberekend (meestal wekelijks of dagelijks):

`locate "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">patroon</span>`"`

- Zoek naar een bestand op basis van de exacte bestandsnaam (een patroon zonder glob-tekens wordt geïnterpreteerd als `*patroon*`):

`locate */`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bestandsnaam</span>

- Herbereken de database. Dit moet je doen als je recent toegevoegde bestanden wilt vinden:

`sudo /usr/libexec/locate.updatedb`
