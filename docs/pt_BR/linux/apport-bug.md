---
layout: page
title: linux/apport-bug (português (Brasil))
description: "Registra um relatório de bug no Ubuntu."
content_hash: f3d5fe079df6a0cef8fd919e15bab72704afb8a6
last_modified_at: 2024-10-05
related_topics:
  - title: Deutsch version
    url: /de/linux/apport-bug.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apport-bug.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/apport-bug.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apport-bug.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/apport-bug.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># apport-bug

Registra um relatório de bug no Ubuntu.
Mais informações: <https://wiki.ubuntu.com/Apport>.

- Relata um bug sobre todo o sistema:

`apport-bug`

- Relata um bug sobre um pacote específico:

`apport-bug `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote</span>

- Relata um bug sobre um executável específico:

`apport-bug `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/executável</span>

- Relata um bug sobre um processo específico:

`apport-bug `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PID</span>
