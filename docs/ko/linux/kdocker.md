---
layout: page
title: linux/kdocker (한국어)
description: "애플리케이션을 시스템 트레이에 쉽게 도킹."
content_hash: f96b5feafe3bf76163c2206fe690ac8073f7fea5
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/kdocker.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/kdocker.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/kdocker.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># kdocker

애플리케이션을 시스템 트레이에 쉽게 도킹.
더 많은 정보: <https://github.com/user-none/KDocker>.

- 왼쪽 마우스 버튼을 누르면 창을 시스템 트레이로 보내기 위해 커서 표시 (다른 마우스 버튼을 누르면 취소):

`kdocker`

- 애플리케이션을 열고 시스템 트레이로 보내기:

`kdocker `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">애플리케이션</span>

- 포커스된 창을 시스템 트레이로 보내기:

`kdocker -f`

- 왼쪽 마우스 버튼을 누르면 사용자 지정 아이콘과 함께 창을 시스템 트레이로 보내기 위해 커서 표시:

`kdocker -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/아이콘</span>

- 애플리케이션을 열고 시스템 트레이로 보내며 포커스를 잃으면 최소화하기:

`kdocker -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">애플리케이션</span>

- 버전 표시:

`kdocker --version`
