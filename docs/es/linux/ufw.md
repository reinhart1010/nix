---
layout: page
title: linux/ufw (español)
description: "Cortafuegos sin complicaciones (_Uncomplicated Firewall_)."
content_hash: d0b8d7bbcaa66eeb2a6b24f3dc6ea8b6aaf4b819
related_topics:
  - title: English version
    url: /en/linux/ufw.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/ufw.html
    icon: bi bi-globe
---
# ufw

Cortafuegos sin complicaciones (_Uncomplicated Firewall_).
Interfaz de usuario de iptables para facilitar la configuración de un firewall.
Más información: <https://wiki.ubuntu.com/UncomplicatedFirewall>.

- Activa ufw:

`ufw enable`

- Desactiva ufw:

`ufw disable`

- Muestra reglas del ufw, junto con sus números:

`ufw status numbered`

- Permite el tráfico entrante en el puerto 5432 en este host con un comentario que identifique el servicio:

`ufw allow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5432</span>` comment "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">servicio</span>`"`

- Permite sólo el tráfico TCP desde 192.168.0.4 a cualquier dirección de este host, en el puerto 22:

`ufw allow proto `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tcp</span>` from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.0.4</span>` to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">any</span>` port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">22</span>

- Deniega tráfico en el puerto 80 en este host:

`ufw deny `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80</span>

- Deniega todo el tráfico al puerto 22:

`ufw deny proto `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">udp</span>` from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">any</span>` to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">any</span>` port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">22</span>

- Elimina una regla concreta. El número de la regla puede obtenerse del comando `ufw status numbered`:

`ufw delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">número_de_regla</span>
