---
layout: page
title: osx/drutil (português (Brasil))
description: "Interage com gravadores de DVD."
content_hash: b037dad1adbe47e442d0d8110cbd8f33f021d3a3
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/osx/drutil.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/drutil.html
    icon: bi bi-globe
tldri18n_status: 2
---
# drutil

Interage com gravadores de DVD.
Mais informações: <https://ss64.com/osx/drutil.html>.

- Ejeta um disco da unidade:

`drutil eject`

- Grava um diretório como um sistema de arquivos ISO9660 em um DVD. Não verifica, e ejeta quando terminar:

`drutil burn -noverify -eject -iso9660`
