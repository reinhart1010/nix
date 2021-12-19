---
layout: page
title: linux/aspell (português (Brasil))
description: "Verificador ortográfico interativo."
content_hash: 011565e355eca871f9102b64abcdb8c2afd693eb
related_topics:
  - title: Deutsch version
    url: /de/linux/aspell.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/aspell.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/linux/aspell.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/aspell.html
    icon: bi bi-globe
---
# aspell

Verificador ortográfico interativo.
Mais informações: <http://aspell.net/>.

- Verificar a ortografia do texto de um arquivo:

`aspell check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo</span>

- Exibir as palavras escritas incorretamente no terminal:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo</span>` | aspell list`

- Exibir os dicionários disponíveis:

`aspell dicts`

- Executar aspell utilizando uma língua diferente (informe o código ISO 639 da língua):

`aspell --lang=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cs</span>

- Exibir os erros ortográficos no terminal e ignorando as palavras da lista pessoal:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo</span>` | aspell --personal=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lista_pessoal.pws</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">list</span>
