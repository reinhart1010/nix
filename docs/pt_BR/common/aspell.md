---
layout: page
title: common/aspell (português (Brasil))
description: "Verificador ortográfico interativo."
content_hash: 743eecbb3c73f3fe3d0247b39afe5e3bf61f6a4c
last_modified_at: 2024-08-14
related_topics:
  - title: Deutsch version
    url: /de/common/aspell.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/aspell.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/common/aspell.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/aspell.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/aspell.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aspell

Verificador ortográfico interativo.
Mais informações: <http://aspell.net/>.

- Verifica a ortografia do texto de um arquivo:

`aspell check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo</span>

- Exibe as palavras escritas incorretamente no terminal:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo</span>` | aspell list`

- Exibe os dicionários disponíveis:

`aspell dicts`

- Executa `aspell` utilizando uma língua diferente (informe o código ISO 639 da língua):

`aspell --lang=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cs</span>

- Exibe os erros ortográficos no terminal e ignorando as palavras da lista pessoal:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo</span>` | aspell --personal=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lista_pessoal.pws</span>` list`
