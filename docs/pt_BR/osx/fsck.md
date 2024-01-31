---
layout: page
title: osx/fsck (português (Brasil))
description: "Verifica a integridade de um sistema de arquivos ou repara ele. O sistema de arquivos deve ser desmontado no momento em que o comando é executado."
content_hash: 5a44c1cb1988d528d29a84589509a1c5776be714
last_modified_at: 2024-01-31
related_topics:
  - title: English version
    url: /en/osx/fsck.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/fsck.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/fsck.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fsck

Verifica a integridade de um sistema de arquivos ou repara ele. O sistema de arquivos deve ser desmontado no momento em que o comando é executado.
É um wrapper que chama `fsck_hfs`, `fsck_apfs`, `fsck_msdos`, `fsck_exfat`, e `fsck_udf` conforme necessário.
Mais informações: <https://keith.github.io/xcode-man-pages/fsck.8.html>.

- Verifica o sistema de arquivos `/dev/sdX`, relatando quaisquer blocos danificados:

`fsck `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- Verifica o sistema de arquivos `/dev/sdX` apenas se estiver limpo, relatando quaisquer blocos danificados e permitindo que o usuário interativamente escolha reparar cada um deles:

`fsck -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- Verifica o sistema de arquivos `/dev/sdX` apenas se estiver limpo, relatando quaisquer blocos danificados e reparando-os automaticamente:

`fsck -fy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- Verifica o sistema de arquivos `/dev/sdX`, informando se ele foi desmontado corretamente:

`fsck -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>
