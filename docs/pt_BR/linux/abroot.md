---
layout: page
title: linux/abroot (português (Brasil))
description: "Utilitário que fornece total imutabilidade e atomicidade ao transacionar entre 2 estados da partição raíz (A⟺B)."
content_hash: 02dfae57c1d7bd23ffc3ff522805edf5b6a52c0d
last_modified_at: 2024-10-02
related_topics:
  - title: English version
    url: /en/linux/abroot.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/abroot.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># abroot

Utilitário que fornece total imutabilidade e atomicidade ao transacionar entre 2 estados da partição raíz (A⟺B).
Atualizações são realizadas usando imagens OCI, para garantir que o sistema sempre estará em um estado consistente.
Mais informações: <https://github.com/Vanilla-OS/ABRoot>.

- Adiciona pacotes à imagem local (Nota: após executar esse comando você precisa aplicar as alterações.):

`sudo abroot pkg add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote</span>

- Remove pacotes da imagem local(Nota: após executar esse comando você precisa aplicar as alterações.):

`sudo abroot pkg remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote</span>

- Lista pacotes da imagem local:

`sudo abroot pkg list`

- Aplica mudanças à imagem local (Nota: você precisa reiniciar o sistema para que as mudanças sejam aplicadas):

`sudo abroot pkg apply`

- Reverte o sistema para o estado anterior:

`sudo abroot rollback`

- Edita/Mostra os parâmetros do kernel:

`sudo abroot kargs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">edit|show</span>

- Mostra o estado:

`sudo abroot status`

- Exibe ajuda:

`abroot --help`
