---
layout: page
title: common/virsh (português (Brasil))
description: "Gerenciar domínios de convidados do virsh. (NOTA: 'guest_id' pode ser o ID, nome ou UUID do convidado)."
content_hash: ebdbaa83d10e37eb783f4c650323e8586c9de7e8
last_modified_at: 2024-05-23
related_topics:
  - title: English version
    url: /en/common/virsh.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/virsh.html
    icon: bi bi-globe
tldri18n_status: 2
---
# virsh

Gerenciar domínios de convidados do virsh. (NOTA: 'guest_id' pode ser o ID, nome ou UUID do convidado).
Alguns subcomandos, como `virsh list`, têm sua própria documentação de uso.
Mais informações: <https://libvirt.org/manpages/virsh.html>.

- Conecta a uma sessão do hipervisor:

`virsh connect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">qemu:///system</span>

- Lista todos os domínios:

`virsh list --all`

- Despeja arquivo de configuração do convidado:

`virsh dumpxml `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">guest_id</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/convidado.xml</span>

- Cria um convidado a partir de um arquivo de configuração:

`virsh create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_de_configuracao.xml</span>

- Edita o arquivo de configuração de um convidado (o editor pode ser alterado com $EDITOR):

`virsh edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">guest_id</span>

- Inicia/reinicia/desliga/suspende/resume um convidado:

`virsh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">guest_id</span>

- Salva o estado atual de um convidado em um arquivo:

`virsh save `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">guest_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_arquivo</span>

- Exclui um convidado em execução:

`virsh destroy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">guest_id</span>` && virsh undefine `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">guest_id</span>
