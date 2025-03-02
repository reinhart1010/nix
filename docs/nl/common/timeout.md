---
layout: page
title: common/timeout (Nederlands)
description: "Voer een commando uit met een tijdslimiet."
content_hash: bf11ad4ec2cde0ef567ba63d2a19954d9e50bfce
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/timeout.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/timeout.html
    icon: bi bi-globe
tldri18n_status: 2
---
# timeout

Voer een commando uit met een tijdslimiet.
Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/timeout-invocation.html>.

- Voer `sleep 10` uit en beëindig het na 3 seconden:

`timeout 3s sleep 10`

- Stuur een [s]ignaal naar het commando nadat de tijdslimiet is verlopen (standaard `TERM`, `kill -l` om alle signalen te tonen):

`timeout --signal `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">INT|HUP|KILL|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5s</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sleep 10</span>

- Stuur [v]erbose output naar `stderr` en laat het signaal zien dat is verzonden bij een timeout:

`timeout --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.5s|1m|1h|1d|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>

- Behoud de exit status van het commando ongeacht of er een timeout is:

`timeout --preserve-status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1s|1m|1h|1d|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>

- Stuur een krachtig `KILL`-signaal na een bepaalde tijd als het commando het initiële signaal negeert bij een timeout:

`timeout --kill-after=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5m</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30s</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>
