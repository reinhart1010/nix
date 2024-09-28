---
layout: page
title: common/fping (Indonesia)
description: "Utilitas ping lebih kuat yang dapat melakukan proses ping pada lebih dari satu host."
content_hash: d194040acde99ecdd4d37935006ee5aa70a72ab6
last_modified_at: 2024-09-28
related_topics:
  - title: English version
    url: /en/common/fping.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fping

Utilitas ping lebih kuat yang dapat melakukan proses ping pada lebih dari satu host.
Informasi lebih lanjut: <https://fping.org>.

- Tampilkan daftar seluruh host yang aktif dalam suatu subjaringan menurut definisi network mask (netmask):

`fping `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-a|--alive</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-g|--generate</span>` 192.168.1.0/24`

- Tampilkan daftar seluruh host yang aktif dalam suatu subjaringan berdasarkan rentang alamat IP:

`fping `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-a|--alive</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-g|--generate</span>` 192.168.1.1 192.168.1.254`

- Tampilkan daftar seluruh host yang tidak aktif dalam suatu subjaringan menurut definisi network mask (netmask):

`fping `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-u|--unreach</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-g|--generate</span>` 192.168.1.0/24`
