---
layout: page
title: common/uniq (Nederlands)
description: "Geef de unieke regels uit een invoer of bestand weer."
content_hash: 455de52974a8bd70272af942c9a4935e67dfc027
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/uniq.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/uniq.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/uniq.html
    icon: bi bi-globe
tldri18n_status: 2
---
# uniq

Geef de unieke regels uit een invoer of bestand weer.
Omdat het geen herhaalde regels detecteert tenzij ze naast elkaar staan, moeten we ze eerst sorteren.
Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/uniq-invocation.html>.

- Toon elke regel één keer:

`sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>` | uniq`

- Toon alleen unieke regels:

`sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>` | uniq -u`

- Toon alleen dubbele regels:

`sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>` | uniq -d`

- Toon het aantal voorkomens van elke regel samen met die regel:

`sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>` | uniq -c`

- Toon het aantal voorkomens van elke regel, gesorteerd op meest frequent:

`sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>` | uniq -c | sort -nr`
