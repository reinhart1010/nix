---
layout: page
title: common/touch (português (Portugal))
description: "Atualizar as timestamps de um ficheiro para a hora atual."
content_hash: 04e4d6c851f28552143273b6a409122da4209f62
last_modified_at: 2023-12-28
related_topics:
  - title: català version
    url: /ca/common/touch.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/touch.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/touch.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/touch.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/touch.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/touch.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/touch.html
    icon: bi bi-globe
tldri18n_status: 2
---
# touch

Atualizar as timestamps de um ficheiro para a hora atual.
Se o ficheiro não existir, cria um ficheiro vazio, a menos que seja passado o parâmetro -c ou -h.
Mais informações: <https://manned.org/man/freebsd-13.1/touch>.

- Cria um novo ficheiro vazio, ou atualizar as timestamps para a hora atual:

`touch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ficheiro</span>

- Define as timestamps de um ficheiro para a hora especificada:

`touch -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YYYYMMDDHHMM.SS</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ficheiro</span>

- Usa as timestamps do ficheiro1 para definir as timestamps do ficheiro2:

`touch -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ficheiro1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ficheiro2</span>

- Altera as timestamps de um ficheiro. Não cria novo ficheiro se não existir:

`touch -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ficheiro</span>
