---
layout: page
title: linux/ufw (català)
description: "Tallafocs sense complicacions (_Uncomplicated Firewall_)."
content_hash: 8d591fb5ed2de2d48c2f6628905bcfdc230b7a7f
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/ufw.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/ufw.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/ufw.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/ufw.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/ufw.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ufw

Tallafocs sense complicacions (_Uncomplicated Firewall_).
Interfície d'usuari de `iptables` per facilitar la configuració d'un firewall.
Més informació: <https://wiki.ubuntu.com/UncomplicatedFirewall>.

- Activa ufw:

`ufw enable`

- Desactiva ufw:

`ufw disable`

- Mostra les regles del ufw, en conjunt amb els seus números:

`ufw status numbered`

- Permet el tràfic entrant en el port 5432 en aquest host amb un comentari que indentifiqui el servei:

`ufw allow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5432</span>` comment "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">servei</span>`"`

- Permet només el tràfic TCP desde 192.168.0.4 a qualsevol direcció d'aquest host, en el port 22:

`ufw allow proto `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tcp</span>` from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.0.4</span>` to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">any</span>` port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">22</span>

- Denega el tràfic en el port 80 en aquest host:

`ufw deny `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80</span>

- Denega tot el tràfic al port 22:

`ufw deny proto `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">udp</span>` from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">any</span>` to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">any</span>` port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">22</span>

- Elimina una regla concreta. El número de la regla es pot obtenir del comanadament `ufw status numbered`:

`ufw delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">número_de_regla</span>
