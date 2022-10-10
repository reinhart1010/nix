---
layout: page
title: osx/drutil (português (Brasil))
description: "Interage com gravadores de DVD."
content_hash: b037dad1adbe47e442d0d8110cbd8f33f021d3a3
related_topics:
  - title: English version
    url: /en/osx/drutil.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/drutil.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># drutil

Interage com gravadores de DVD.
Mais informações: <https://ss64.com/osx/drutil.html>.

- Ejeta um disco da unidade:

`drutil eject`

- Grava um diretório como um sistema de arquivos ISO9660 em um DVD. Não verifica, e ejeta quando terminar:

`drutil burn -noverify -eject -iso9660`
