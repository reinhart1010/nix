---
layout: page
title: common/zsh (português (Brasil))
description: "Z SHell, um interpretador de linha de comando compatível com o Bash."
content_hash: 5535312339139346662af513009489e59e909f15
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/zsh.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/zsh.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/zsh.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/zsh.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/zsh.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/zsh.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/zsh.html
    icon: bi bi-globe
tldri18n_status: 2
---
# zsh

Z SHell, um interpretador de linha de comando compatível com o Bash.
Veja também `bash`, `histexpand`.
Mais informações: <https://www.zsh.org>.

- Inicie uma sessão shell interativa:

`zsh`

- Execute [c]omandos específicos:

`zsh -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo Olá Mundo</span>`"`

- Execute um script específico:

`zsh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/script.zsh</span>

- Verifica um script específico por erros de sintaxe sem executá-lo:

`zsh --no-exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/script.zsh</span>

- Executa comandos específicos da `stdin`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo Olá Mundo</span>` | zsh`

- Execute um script específico, imprimindo cada comando do script antes de executá-lo:

`zsh --xtrace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/script.zsh</span>

- Inicie uma sessão shell interativa no modo verboso, imprimindo cada comando antes de executá-lo:

`zsh --verbose`

- Executa um comando específico dentro do `zsh` com padrões glob desativados:

`noglob `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>
