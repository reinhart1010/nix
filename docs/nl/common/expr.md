---
layout: page
title: common/expr (Nederlands)
description: "Evalueer expressies en manipuleer string."
content_hash: 87a96fbdc1d77951d81d9aea6a686b9e0967ceae
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/expr.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/expr.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/expr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# expr

Evalueer expressies en manipuleer string.
Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/expr-invocation.html>.

- Krijg de lengte van een specifieke string:

`expr length "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>`"`

- Krijg de substring van een string met een specifieke lengte:

`expr substr "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">van</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lengte</span>

- Vergelijk een specifieke substring met een verankerd patroon:

`expr match "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>`" '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">patroon</span>`'`

- Verkrijg de eerste karakterpositie van een specifieke set in een tekenreeks:

`expr index "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">karakters</span>`"`

- Bereken een specifieke mathematische expressie:

`expr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expressie1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">+|-|*|/|%</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expressie2</span>

- Bekijk de eerste expressie als de waarde niet nul is en niet null, anders de tweede:

`expr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expressie1</span>` \| `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expressie2</span>

- Bekijk de eerste expressie als beide expressies niet nul zijn en niet null, anders 0:

`expr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expressie1</span>` \& `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expressie2</span>
