---
layout: page
title: common/diffstat (italiano)
description: "Crea un istogramma dall'output del comando `diff`."
content_hash: 5ca8ac80b4890ae1bdfb0a21e67c6f3926949d5d
related_topics:
  - title: English version
    url: /en/common/diffstat.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/diffstat.html
    icon: bi bi-globe
---
# diffstat

Crea un istogramma dall'output del comando `diff`.
Maggiori informazioni: <https://manned.org/diffstat>.

- Mostra i cambiamenti in un istogramma:

`diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file2</span>` | diffstat`

- Mostra inserimenti, cancellazioni e modifiche come una tabella:

`diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file2</span>` | diffstat -t`
