---
layout: page
title: linux/ufw (português (Brasil))
description: "Firewall Descomplicado."
content_hash: 0893716b76cd7a433066030a5f633f356a330c3a
last_modified_at: 2023-11-12
related_topics:
  - title: català version
    url: /ca/linux/ufw.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/ufw.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/ufw.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/ufw.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/ufw.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ufw

Firewall Descomplicado.
Frontend para `iptables` com o objetivo de facilitar a configuração de um firewall.
Mais informações: <https://wiki.ubuntu.com/UncomplicatedFirewall>.

- Habilitar ufw:

`ufw enable`

- Desabilitar ufw:

`ufw disable`

- Mostrar regras ufw, juntamente com seus números:

`ufw status numbered`

- Permitir tráfego de entrada na porta 5432 nesse host com um que identifique o serviço:

`ufw allow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5432</span>` comment "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Service</span>`"`

- Permitir apenas tráfego TCP de 192.168.0.4 pra qualquer endereço deste host, na porta 22 :

`ufw allow proto `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tcp</span>` from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.0.4</span>` to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">any</span>` port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">22</span>

- Negar tráfego na porta 80 desse host :

`ufw deny `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80</span>

- Negar todo o tráfego UDP para portas no intervalo 8412:8500:

`ufw deny proto `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">udp</span>` from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">any</span>` to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">any</span>` port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8412:8500</span>

- Deletar uma regra particular. O número da regra pode ser recuperado com o `ufw status numbered` comando:

`ufw delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rule_number</span>
