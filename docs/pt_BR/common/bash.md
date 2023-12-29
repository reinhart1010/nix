---
layout: page
title: common/bash (português (Brasil))
description: "Bourne-Again SHell, um interpretador de linha de comando compatível com `sh`."
content_hash: 598e8ea6db482cbd800146c992c0e8d32766424e
last_modified_at: 2023-12-29
related_topics:
  - title: Deutsch version
    url: /de/common/bash.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/bash.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/bash.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/bash.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/bash.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/bash.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/bash.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/bash.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/bash.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bash

Bourne-Again SHell, um interpretador de linha de comando compatível com `sh`.
Veja também: `zsh`, `histexpand` (expansão do histórico).
Mais informações: <https://www.gnu.org/software/bash/>.

- Inicia uma sessão interativa do shell:

`bash`

- Inicia uma sessão interativa do shell sem carregar as configurações de inicialização:

`bash --norc`

- Executa [c]omandos específicos:

`bash -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo 'bash é executado'</span>`"`

- Executa um script específico:

`bash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/script.sh</span>

- Executa um script específico exibindo cada comando antes de executá-lo:

`bash -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/script.sh</span>

- Executa um script específico e para no primeiro [e]rro:

`bash -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/script.sh</span>

- Executa comandos específicos da `stdin`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "echo 'bash é executado'"</span>` | bash`

- Inicia uma sessão do shell [r]estrita:

`bash -r`
