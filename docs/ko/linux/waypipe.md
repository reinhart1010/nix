---
layout: page
title: linux/waypipe (한국어)
description: "Wayland 컴포지터에서 그래픽 애플리케이션을 원격으로 실행."
content_hash: 87a2e0a4c20e161845f00bc87f5271455850f343
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/waypipe.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/waypipe.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/waypipe.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># waypipe

Wayland 컴포지터에서 그래픽 애플리케이션을 원격으로 실행.
더 많은 정보: <https://gitlab.freedesktop.org/mstoeckl/waypipe>.

- 그래픽 프로그램을 원격으로 실행하고 로컬에 표시:

`waypipe ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서버</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로그램</span>

- SSH 터널을 열어 프로그램을 원격으로 실행하고 로컬에 표시:

`waypipe ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서버</span>
