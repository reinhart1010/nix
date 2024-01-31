---
layout: page
title: osx/drutil (português (Brasil))
description: "Interage com gravadores de DVD."
content_hash: fc779ddb01762b496fd71c83a96b4bc130278067
last_modified_at: 2024-01-31
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
Mais informações: <https://keith.github.io/xcode-man-pages/drutil.1.html>.

- Ejeta um disco da unidade:

`drutil eject`

- Grava um diretório como um sistema de arquivos ISO9660 em um DVD. Não verifica, e ejeta quando terminar:

`drutil burn -noverify -eject -iso9660`
