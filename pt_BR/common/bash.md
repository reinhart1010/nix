---
layout: page
title: common/bash (português (Brasil))
description: "Bourne-Again SHell, um interpretador de linha de comando compatível com `sh`."
content_hash: c0550cce6efda53db142b1c9538b66658b7dbce0
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
---
# bash

Bourne-Again SHell, um interpretador de linha de comando compatível com `sh`.
Veja também `histexpand` para a expansão do histórico.
Mais informações: <https://gnu.org/software/bash/>.

- Iniciar uma seção interativa do shell:

`bash`

- Executar um comando e sair:

`bash -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>`"`

- Executar um script:

`bash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/script.sh</span>

- Executar um script, exibindo cada comando antes de executá-lo:

`bash -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/script.sh</span>

- Executar os comandos de um script, parando de executar no primeiro erro:

`bash -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/script.sh</span>

- Ler e executar comandos do stdin (entrada padrão):

`bash -s`

- Exibir a versão do Bash (`$BASH_VERSION` abrange apenas a versão sem informações da licença):

`bash --version`
