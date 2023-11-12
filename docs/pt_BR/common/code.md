---
layout: page
title: common/code (português (Brasil))
description: "Editor de código extensível e multi plataforma."
content_hash: 3181ee996daaa9ae8c88110ef855740559491131
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/code.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/code.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/code.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/code.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/code.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/code.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/code.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/code.html
    icon: bi bi-globe
tldri18n_status: 2
---
# code

Editor de código extensível e multi plataforma.
Mais informações: <https://github.com/microsoft/vscode>.

- Inicia Visual Studio Code:

`code`

- Abre arquivos/diretórios específicos:

`code `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_ou_diretório1 caminho/para/arquivo_ou_diretório2 ...</span>

- Compara dois arquivos específicos:

`code --diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo2</span>

- Abre arquivos/diretórios específicos em uma nova janela:

`code --new-window `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_ou_diretório1 caminho/para/arquivo_ou_diretório2 ...</span>

- Instala/desinstala uma extensão específica:

`code --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">install|uninstall</span>`-extension `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">editor.extensão</span>

- Imprime as extensões instaladas:

`code --list-extensions`

- Imprime extensões instaladas com suas versões:

`code --list-extensions --show-versions`

- Inicia o editor como um superusuário (root) enquanto armazena dados do usuário em um diretório específico:

`sudo code --user-data-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório</span>
