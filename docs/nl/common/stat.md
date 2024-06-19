---
layout: page
title: common/stat (Nederlands)
description: "Toon bestands- en bestandssysteeminformatie."
content_hash: 03132aa4a31492a229b6e5cd91d51120d624ef74
last_modified_at: 2024-06-19
related_topics:
  - title: English version
    url: /en/common/stat.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/stat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# stat

Toon bestands- en bestandssysteeminformatie.
Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/stat-invocation.html>.

- Toon eigenschappen van een specifiek bestand zoals grootte, permissies, aanmaak- en toegangsdatums en meer:

`stat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Toon eigenschappen van een specifiek bestand zoals grootte, permissies, aanmaak- en toegangsdatums en meer zonder labels:

`stat --terse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Toon informatie over het bestandssysteem waar een specifiek bestand zich bevindt:

`stat --file-system `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Toon alleen octale bestandspermissies:

`stat --format="%a %n" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Toon de eigenaar en groep van een specifiek bestand:

`stat --format="%U %G" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Toon de grootte van een specifiek bestand in bytes:

`stat --format="%s %n" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>
