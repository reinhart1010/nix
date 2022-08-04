---
layout: page
title: linux/logwatch (Deutsch)
description: "Fasst viele verschiedene Logs für gängige Dienste (z.B. Apache, pam_unix, sshd, usw.) in einem einzelnen Bericht zusammen."
content_hash: b70b794c9baa50bb098b2fe68881287d05960045
related_topics:
  - title: English version
    url: /en/linux/logwatch.html
    icon: bi bi-globe
---
# logwatch

Fasst viele verschiedene Logs für gängige Dienste (z.B. Apache, pam_unix, sshd, usw.) in einem einzelnen Bericht zusammen.
Weitere Informationen: <https://manned.org/logwatch>.

- Analysiere Logs für einen Zeitraum mit einer bestimmten Detailtiefe:

`logwatch --range `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">yesterday|today|all|help</span>` --detail `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">low|medium|others</span>`'`

- Beschränke den Bericht auf Informationen zu einem ausgewählten Dienst:

`logwatch --range `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">all</span>` --service `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">apache|pam_unix|etc</span>
