---
layout: page
title: common/virsh (português (Brasil))
description: "Gerenciar domínios de convidados do virsh. (NOTA: 'guest_id' pode ser o ID, nome ou UUID do convidado)."
content_hash: df46cd59c652ef026651d4d589c3d037e0d9931f
last_modified_at: 2023-09-18
related_topics:
  - title: English version
    url: /en/common/virsh.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># virsh

Gerenciar domínios de convidados do virsh. (NOTA: 'guest_id' pode ser o ID, nome ou UUID do convidado).
Alguns subcomandos, como `virsh list`, têm sua própria documentação de uso.
Mais informações: <https://libvirt.org/virshcmdref.html>.

- Conectar-se a uma sessão do hipervisor:

`virsh connect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">qemu:///system</span>

- Listar todos os domínios:

`virsh list --all`

- Despejar arquivo de configuração do convidado:

`virsh dumpxml `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">guest_id</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/convidado.xml</span>

- Criar um convidado a partir de um arquivo de configuração:

`virsh create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_de_configuracao.xml</span>

- Editar o arquivo de configuração de um convidado (o editor pode ser alterado com $EDITOR):

`virsh edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">guest_id</span>

- Iniciar/reiniciar/desligar/suspender/resumir um convidado:

`virsh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">guest_id</span>

- Salvar o estado atual de um convidado em um arquivo:

`virsh save `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">guest_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_arquivo</span>

- Excluir um convidado em execução:

`virsh destroy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">guest_id</span>` && virsh undefine `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">guest_id</span>
