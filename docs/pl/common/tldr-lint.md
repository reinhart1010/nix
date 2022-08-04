---
layout: page
title: common/tldr-lint (polski)
description: "Waliduj i formatuj strony dokumentacji `tldr`."
content_hash: 556543425905d10ba687d021c1114967363804a7
related_topics:
  - title: English version
    url: /en/common/tldr-lint.html
    icon: bi bi-globe
  - title: sh version
    url: /sh/common/tldr-lint.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/tldr-lint.html
    icon: bi bi-globe
---
# tldr-lint

Waliduj i formatuj strony dokumentacji `tldr`.
Więcej informacji: <https://github.com/tldr-pages/tldr-lint>.

- Waliduj wszystkie strony:

`tldr-lint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">katalog_ze_stronami</span>

- Formatuj stronę na standardowe wyjście:

`tldr-lint --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">strona.md</span>

- Formatuj wszystkie strony w miejscu:

`tldr-lint --format --in-place `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">katalog_ze_stronami</span>
