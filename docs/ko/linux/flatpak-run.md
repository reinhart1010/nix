---
layout: page
title: linux/flatpak-run (한국어)
description: "Flatpak 애플리케이션 및 런타임 실행."
content_hash: b84e8f3e7623a88f286ac1681fb2d2ccd7a8dd13
last_modified_at: 2024-10-21
related_topics:
  - title: English version
    url: /en/linux/flatpak-run.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/flatpak-run.html
    icon: bi bi-globe
tldri18n_status: 2
---
# flatpak run

Flatpak 애플리케이션 및 런타임 실행.
더 많은 정보: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak-run>.

- 설치된 애플리케이션 실행:

`flatpak run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.example.app</span>

- 특정 브랜치(예: stable, beta, master)에서 설치된 애플리케이션 실행:

`flatpak run --branch=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stable|beta|master|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.example.app</span>

- Flatpak 안에서 인터랙티브 셸 실행:

`flatpak run --command=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sh</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.example.app</span>
