---
layout: page
title: common/gcrane-gc (Nederlands)
description: "Toon images die niet getagged zijn."
content_hash: 99d0b5ea04d6cf4ba50aeb1ae51526a691feef54
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/gcrane-gc.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/gcrane-gc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gcrane gc

Toon images die niet getagged zijn.
Zal berekenen welke images opgeruimd kunnen worden met garbage-collection.
Dit kan uitgevoerd worden met `gcrane delete` om ze daadwerkelijk op te ruimen.
Meer informatie: <https://github.com/google/go-containerregistry/blob/main/cmd/gcrane/README.md>.

- Toon niet getagde images:

`gcrane gc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository</span>

- Recursief door de repositories heen:

`gcrane gc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-r|--recursive</span>

- Toon de help:

`gcrane gc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
