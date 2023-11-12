---
layout: page
title: common/sshfs (português (Brasil))
description: "Cliente de sistema de arquivos baseado em SSH."
content_hash: 846dff957b17c4d2c1aa57a000913dd8c2f27596
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/sshfs.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/sshfs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sshfs

Cliente de sistema de arquivos baseado em SSH.
Mais informações: <https://github.com/libfuse/sshfs>.

- Montar um diretório remoto:

`sshfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_usuário</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host_remoto</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">diretório_remoto</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ponto_de_montagem</span>

- Desmontar um diretório remoto:

`umount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ponto_de_montagem</span>

- Montar um diretório remoto de um servidor com uma porta específica:

`sshfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_usuário</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host_remoto</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">diretório_remoto</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2222</span>

- Usar compressão:

`sshfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_usuário</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host_remoto</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">diretório_remoto</span>` -C`

- Seguir links simbólicos:

`sshfs -o follow_symlinks `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_usuário</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host_remoto</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">diretório_remoto</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ponto_de_montagem</span>
