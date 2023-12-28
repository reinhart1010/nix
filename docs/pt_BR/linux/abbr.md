---
layout: page
title: linux/abbr (português (Brasil))
description: "Gerencie abreviações para fish-shell."
content_hash: 1cbc259b18bdf26b37453762f4ed351e438524ee
last_modified_at: 2023-12-28
related_topics:
  - title: català version
    url: /ca/linux/abbr.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/abbr.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/abbr.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/abbr.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/abbr.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/abbr.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/abbr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# abbr

Gerencie abreviações para fish-shell.
Palavras definidas pelo usuário são substituídas por frases longas assim que são digitadas.
Mais informações: <https://fishshell.com/docs/current/cmds/abbr.html>.

- Adicione uma nova abreviação:

`abbr --add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_abreviacao</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">orgumentos_comando</span>

- Renomeia uma abreviação existente:

`abbr --rename `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_antigo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">novo_nome</span>

- Apaga uma abreviação existente:

`abbr --erase `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_abreviacao</span>

- Importa abreviações definidas em outro host via SSH:

`ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_host</span>` abbr --show | source`
