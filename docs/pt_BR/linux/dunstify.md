---
layout: page
title: linux/dunstify (português (Brasil))
description: "Uma ferramenta de notificação que é uma extensão do `notify-send`, mas com mais funcionalidades baseadas em `dunst`."
content_hash: aea144f9d40811290835c278b4a987925876a997
last_modified_at: 2024-09-23
related_topics:
  - title: English version
    url: /en/linux/dunstify.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/dunstify.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dunstify

Uma ferramenta de notificação que é uma extensão do `notify-send`, mas com mais funcionalidades baseadas em `dunst`.
Aceita todas as opções do `notify-send`.
Mais informações: <https://github.com/dunst-project/dunst/wiki/Guides>.

- Mostra uma notificação com um dado título e mensagem:

`dunstify "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Título</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Mensagem</span>`"`

- Mostra uma notificação com uma urgência específica:

`dunstify "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Título</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Mensagem</span>`" -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">low|normal|critical</span>

- Especifica um ID para a mensagem (sobrescreve qualquer mensagem anterior com o mesmo ID):

`dunstify "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Título</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Mensagem</span>`" -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">123</span>

- Mostra opções de ajuda:

`dunstify --help`
