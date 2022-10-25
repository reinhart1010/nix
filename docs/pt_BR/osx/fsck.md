---
layout: page
title: osx/fsck (português (Brasil))
description: "Verifica a integridade de um sistema de arquivos ou repara ele. O sistema de arquivos deve ser desmontado no momento em que o comando é executado."
content_hash: d7dbf93963eb004d8c29370d5120c1df7554d602
related_topics:
  - title: English version
    url: /en/osx/fsck.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/fsck.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># fsck

Verifica a integridade de um sistema de arquivos ou repara ele. O sistema de arquivos deve ser desmontado no momento em que o comando é executado.
É um wrapper que chama `fsck_hfs`, `fsck_apfs`, `fsck_msdos`, `fsck_exfat`, e `fsck_udf` conforme necessário.
Mais informações: <https://ss64.com/osx/fsck.html>.

- Verifica o sistema de arquivos `/dev/sdX`, relatando quaisquer blocos danificados:

`fsck `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- Verifica o sistema de arquivos `/dev/sdX` apenas se estiver limpo, relatando quaisquer blocos danificados e permitindo que o usuário interativamente escolha reparar cada um deles:

`fsck -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- Verifica o sistema de arquivos `/dev/sdX` apenas se estiver limpo, relatando quaisquer blocos danificados e reparando-os automaticamente:

`fsck -fy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- Verifica o sistema de arquivos `/dev/sdX`, informando se ele foi desmontado corretamente:

`fsck -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>
