---
layout: page
title: linux/cgclassify (português (Brasil))
description: "Move tarefas em execução para `cgroups`."
content_hash: bc34f77e12565824d66f473fe6bcf021e0da0d40
last_modified_at: 2024-10-05
related_topics:
  - title: English version
    url: /en/linux/cgclassify.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/cgclassify.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/cgclassify.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cgclassify

Move tarefas em execução para `cgroups`.
Mais informações: <https://manned.org/cgclassify>.

- Move o processo com um PID específico para o grupo de controle estudante na hierarquia CPU:

`cgclassify -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cpu:estudante</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1234</span>

- Move o processo com um PID específico para grupos de controle baseados no arquivo de configuração `/etc/cgrules.conf`:

`cgclassify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1234</span>

- Move o processo com um PID específico para o grupo de controle estudante na hierarquia CPU. Note: o daemon do serviço `cgred` não altera `cgroups` do PID específico e seus filhos (com base em `/etc/cgrules.conf`):

`cgclassify --sticky -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cpu:/estudante</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1234</span>
