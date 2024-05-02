---
layout: page
title: linux/ntpd (español)
description: "El daemon oficial de NTP (Network Time Protocol) para sincronizar el reloj del sistema con servidores de tiempo remotos o relojes de referencia locales."
content_hash: c0cad177f234a0790da478fd29fbab6601014466
last_modified_at: 2024-05-02
related_topics:
  - title: English version
    url: /en/linux/ntpd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ntpd

El daemon oficial de NTP (Network Time Protocol) para sincronizar el reloj del sistema con servidores de tiempo remotos o relojes de referencia locales.
Más información: <https://manned.org/ntpd>.

- Inicia el daemon:

`sudo ntpd`

- Sincroniza la hora del sistema con servidores remotos una sola vez (sale después de sincronizar):

`sudo ntpd --quit`

- Sincroniza una sola vez permitiendo "grandes" ajustes:

`sudo ntpd --panicgate --quit`
