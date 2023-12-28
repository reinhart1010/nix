---
layout: page
title: osx/asr (português (Brasil))
description: "Restaurar (copiar) uma imagem de disco em um volume."
content_hash: 46f740346bd50a0dd11934d13c5b592f6dec46d6
last_modified_at: 2023-12-28
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
Mais informações: <https://www.unix.com/man-page/osx/8/asr/>.

- Restaura uma imagem de disco para um volume de destino:

`sudo asr restore --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_imagem</span>`.dmg --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/volume</span>

- Apaga o volume de destino antes de restaurar:

`sudo asr restore --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_imagem</span>`.dmg --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/volume</span>` --erase`

- Ignora a verificação após a restauração:

`sudo asr restore --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_imagem</span>`.dmg --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/volume</span>` --noverify`

- Clona volumes sem o uso de uma imagem de disco intermediária:

`sudo asr restore --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/volume</span>` --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/volume_clonado</span>
