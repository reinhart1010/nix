---
layout: page
title: common/git-push (português (Brasil))
description: "Envia commits para um repositório remoto."
content_hash: 78caebff225f2a0d408bd0946a5d2639da892fea
last_modified_at: 2023-10-15
related_topics:
  - title: Deutsch version
    url: /de/common/git-push.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-push.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-push.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-push.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-push.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-push.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-push.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git push

Envia commits para um repositório remoto.
Mais informações: <https://git-scm.com/docs/git-push>.

- Envia alterações locais na branch atual para sua contraparte remota padrão:

`git push`

- Envia alterações de uma branch local específica para sua contraparte remota:

`git push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_remoto</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_local</span>

- Envia alterações de uma branch local específica para sua contraparte remota, e define a branch remota como o destino push/pull padrão da branch local:

`git push -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_remoto</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_local</span>

- Envia alterações de uma branch local específica para uma branch remota específica:

`git push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_remoto</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_local</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_remota</span>

- Envia alterações em todas as branches locais para suas contrapartes em um determinado repositório remoto:

`git push --all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_remoto</span>

- Exclui uma branch em um repositório remoto:

`git push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_remoto</span>` --delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_remota</span>

- Remove branches remotas que não tenham uma contraparte local:

`git push --prune `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_remoto</span>

- Publica etiquetas que ainda não estão no repositório remoto:

`git push --tags`
