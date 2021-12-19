---
layout: page
title: linux/dnf (português (Brasil))
description: "Gerenciador de pacotes das distribuições baseadas em RHEL (substituto do yum)."
content_hash: af2cd6cfc92b566bc70dddc2f456f195d2e3cb89
related_topics:
  - title: Deutsch version
    url: /de/linux/dnf.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/dnf.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/dnf.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/dnf.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dnf

Gerenciador de pacotes das distribuições baseadas em RHEL (substituto do yum).
Mais informações: <https://dnf.readthedocs.io>.

- Instalar um novo pacote:

`sudo dnf install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_pacote</span>

- Instalar um novo pacote e responder sim para todas as questões:

`sudo dnf -y install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_pacote</span>

- Remover um pacote:

`sudo dnf remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_pacote</span>

- Atualizar todos os pacotes instalados para as versões mais recentes:

`sudo dnf upgrade`
