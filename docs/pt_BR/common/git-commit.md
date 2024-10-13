---
layout: page
title: common/git-commit (português (Brasil))
description: "Faz um commit dos arquivos no repositório."
content_hash: 01b92b158c9ff778701365d30daf67cb540b90ba
last_modified_at: 2024-10-13
related_topics:
  - title: Deutsch version
    url: /de/common/git-commit.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-commit.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-commit.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-commit.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-commit.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-commit.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/git-commit.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-commit.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-commit.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-commit.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-commit.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git commit

Faz um commit dos arquivos no repositório.
Mais informações: <https://git-scm.com/docs/git-commit>.

- Faz um commit com os arquivos preparados no repositório com uma mensagem:

`git commit --message "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mensagem</span>`"`

- Faz um commit com os arquivos preparados com uma mensagem lida de um arquivo:

`git commit --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_de_mensagem_do_commit</span>

- Prepara automaticamente todos os arquivos modificados e excluídos e faz o commit com uma mensagem:

`git commit --all --message "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mensagem</span>`"`

- Faz um commit com os arquivos preparados e assina-os com a chave GPG especificada (ou a definida no arquivo de configuração se nenhum argumento for especificado):

`git commit --gpg-sign `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_da_chave</span>` --message "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mensagem</span>`"`

- Atualiza o último commit adicionando as alterações atualmente preparadas, alterando o hash do commit:

`git commit --amend`

- Faz um commit apenas de arquivos específicos (já preparados):

`git commit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo1 caminho/para/arquivo2 ...</span>

- Cria um commit, mesmo se não haja arquivos preparados:

`git commit --message "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mensagem</span>`" --allow-empty`
