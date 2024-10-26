---
layout: page
title: common/fping (Indonesia)
description: "Utilitas ping lebih kuat yang dapat melakukan proses ping pada lebih dari satu host."
content_hash: b5b3c2d3e7f83351198af7f7d3a3fcd1c974a787
last_modified_at: 2024-10-26
related_topics:
  - title: English version
    url: /en/common/fping.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/fping.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># fping

Utilitas ping lebih kuat yang dapat melakukan proses ping pada lebih dari satu host.
Informasi lebih lanjut: <https://fping.org>.

- Tampilkan daftar status atas seluruh host pada suatu rentang alamat IP:

`fping `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.1.{1..254}</span>

- Tampilkan daftar seluruh host yang aktif dalam suatu subjaringan menurut definisi network mask (netmask):

`fping `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-a|--alive</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-g|--generate</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.1.0/24</span>

- Tampilkan daftar seluruh host yang aktif dalam suatu subjaringan berdasarkan rentang alamat IP:

`fping `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-q|--quiet</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-a|--alive</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-g|--generate</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.1.1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.1.254</span>

- Tampilkan daftar seluruh host yang tidak aktif dalam suatu subjaringan menurut definisi network mask (netmask):

`fping `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-u|--unreach</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-g|--generate</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.1.0/24</span>
