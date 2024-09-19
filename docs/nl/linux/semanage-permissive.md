---
layout: page
title: linux/semanage-permissive (Nederlands)
description: "Beheer persistente SELinux permissieve domeinen."
content_hash: fb2c087fe1b56960f078c1e5558864c7a432241f
last_modified_at: 2024-09-19
related_topics:
  - title: English version
    url: /en/linux/semanage-permissive.html
    icon: bi bi-globe
tldri18n_status: 2
---
# semanage permissive

Beheer persistente SELinux permissieve domeinen.
Let op dat dit het proces effectief onbeperkt maakt. Voor langdurig gebruik wordt aanbevolen om SELinux correct te configureren.
Zie ook: `semanage`, `getenforce`, `setenforce`.
Meer informatie: <https://manned.org/semanage-permissive>.

- Toon alle procestypen (ook wel domeinen genoemd) die in permissieve modus zijn:

`sudo semanage permissive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-l|--list</span>

- Stel de permissieve modus in of uit voor een domein:

`sudo semanage permissive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-a|--add|-d|--delete</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">httpd_t</span>
