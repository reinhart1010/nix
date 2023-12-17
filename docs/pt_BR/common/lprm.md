---
layout: page
title: common/lprm (português (Brasil))
description: "Cancela trabalhos de impressão na fila de um servidor."
content_hash: ecc011dbe3e9b3d3295e92501425b7bf5d394357
last_modified_at: 2023-12-17
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/lprm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># lprm

Cancela trabalhos de impressão na fila de um servidor.
Veja também: `lpq`.
Mais informações: <https://www.cups.org/doc/man-lprm.html>.

- Cancela o trabalho atual na impressora padrão:

`lprm`

- Cancela um trabalho de um servidor específico:

`lprm -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">servidor[:porta]</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_do_trabalho</span>

- Cancela múltiplos trabalhos com uma conexão criptografada com o servidor:

`lprm -E `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_do_trabalho1 id_do_trabalho2 ...</span>

- Cancela todos os trabalhos:

`lprm -`

- Cancela o trabalho atual de uma impressora ou classe específica:

`lprm -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destino[/instância]</span>
