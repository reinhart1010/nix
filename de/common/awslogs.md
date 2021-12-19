---
layout: page
title: common/awslogs (Deutsch)
description: "CLI um Log-Gruppen, Streams und Events von Amazon CloudWatch Logs abzurufen."
content_hash: b18cbd6170f075501653327f257b9f13fb9a6363
related_topics:
  - title: English version
    url: /en/common/awslogs.html
    icon: bi bi-globe
---
# awslogs

CLI um Log-Gruppen, Streams und Events von Amazon CloudWatch Logs abzurufen.
Weitere Informationen: <https://github.com/jorgebastida/awslogs>.

- Liste alle Log-Gruppen auf:

`awslogs groups`

- Liste alle bestehenden Streams einer angegebenen Loggruppe auf:

`awslogs streams `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/var/log/syslog</span>

- Rufe alle Logs für jegliche Streams in der angegebenen Log-Gruppe für die letzten 1 bis 2 Stunden ab:

`awslogs get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/var/log/syslog</span>` --start='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2h ago</span>`' --end='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1h ago</span>`'`

- Rufe alle Logs für einen bestimmten CloudWatch-Logs Filter-Ausdruck ab:

`awslogs get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/aws/lambda/meine_lambda_gruppe</span>` --filter-pattern='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ERROR</span>`'`

- Beobachte Logs für jegliche Streams in der angegebenen Log-Gruppe:

`awslogs get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/var/log/syslog</span>` ALL --watch`
