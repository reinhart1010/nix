---
layout: page
title: common/env (norsk)
description: "Vis miljøet eller kjør et program i et modifisert miljø."
content_hash: 7deca8d3c1f710f0950274ef2e578cabd9aee624
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/env.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/env.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/env.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/env.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/env.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/env.html
    icon: bi bi-globe
tldri18n_status: 2
---
# env

Vis miljøet eller kjør et program i et modifisert miljø.
Mer informasjon: <https://www.gnu.org/software/coreutils/manual/html_node/env-invocation.html>.

- Vis miljøet:

`env`

- Kjør et program. Ofte brukt i skript etter shebang (#!) for å slå opp stien til programmet:

`env `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program</span>

- Slett miljøet og kjør et program:

`env -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program</span>

- Fjern variabel fra miljøet og kjør et program:

`env -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variabel</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program</span>

- Angi en variabel og kjør et program:

`env `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variabel</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">verdi</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program</span>

- Angi flere variabler og kjør et program:

`env `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variabel1</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">verdi</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variabel2</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">verdi</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variabel3</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">verdi</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program</span>
