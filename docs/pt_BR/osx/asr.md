---
layout: page
title: osx/asr (português (Brasil))
description: "Restaurar (copiar) uma imagem de disco em um volume."
content_hash: 6c8e0b50b4e21490232af0d1140927db789a093c
last_modified_at: 2024-01-31
related_topics:
  - title: English version
    url: /en/osx/asr.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/asr.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/osx/asr.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/asr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# asr

Restaurar (copiar) uma imagem de disco em um volume.
O nome do comando significa Apple Software Restore.
Mais informações: <https://keith.github.io/xcode-man-pages/asr.8.html>.

- Restaura uma imagem de disco para um volume de destino:

`sudo asr restore --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_imagem.dmg</span>` --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/volume</span>

- Apaga o volume de destino antes de restaurar:

`sudo asr restore --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_imagem.dmg</span>` --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/volume</span>` --erase`

- Ignora a verificação após a restauração:

`sudo asr restore --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_imagem.dmg</span>` --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/volume</span>` --noverify`

- Clona volumes sem o uso de uma imagem de disco intermediária:

`sudo asr restore --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/volume</span>` --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/volume_clonado</span>
