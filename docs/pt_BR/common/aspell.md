---
layout: page
title: common/aspell (português (Brasil))
description: "Verificador ortográfico interativo."
content_hash: 743eecbb3c73f3fe3d0247b39afe5e3bf61f6a4c
last_modified_at: 2024-08-13
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/aspell.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># aspell

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
