---
layout: page
title: linux/semanage-permissive (Nederlands)
description: "Beheer persistente SELinux permissieve domeinen."
content_hash: 613f2984bd2d433b941f5a891166a454712670a0
last_modified_at: 2024-06-26
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
Meer informatie: <https://manned.org/man/semanage-permissive>.

- Toon alle procestypen (ook wel domeinen genoemd) die in permissieve modus zijn:

`sudo semanage permissive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-l|--list</span>

- Stel de permissieve modus in of uit voor een domein:

`sudo semanage permissive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-a|--add|-d|--delete</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">httpd_t</span>
