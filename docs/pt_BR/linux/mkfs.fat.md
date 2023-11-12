---
layout: page
title: linux/mkfs.fat (português (Brasil))
description: "Cria um sistema de arquivos MS-DOS dentro de uma partição."
content_hash: 8eab7c72c41fa58a8aedb5119f3f6c1b7673f9f2
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/mkfs.fat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mkfs.fat

Cria um sistema de arquivos MS-DOS dentro de uma partição.
Mais informações: <https://manned.org/mkfs.fat>.

- Cria um sistema de arquivos fat dentro da partição 1 do dispositivo b (`sdb1`):

`mkfs.fat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>

- Cria um sistema de arquivos com um nome de volume:

`mkfs.fat -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_de_volume</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>

- Cria um sistema de arquivos com um id de volume:

`mkfs.fat -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_de_volume</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>

- Usa 5 em vez de 2 tabelas de alocação de arquivos:

`mkfs.fat -f 5 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>
