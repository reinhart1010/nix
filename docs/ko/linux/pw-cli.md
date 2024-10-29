---
layout: page
title: linux/pw-cli (한국어)
description: "PipeWire 인스턴스의 모듈, 객체, 노드, 장치, 링크 등을 관리."
content_hash: ba088afaa1ec629daa04b2c771498be2848a9b53
last_modified_at: 2024-10-29
related_topics:
  - title: English version
    url: /en/linux/pw-cli.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/pw-cli.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pw-cli.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/pw-cli.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pw-cli

PipeWire 인스턴스의 모듈, 객체, 노드, 장치, 링크 등을 관리.
더 많은 정보: <https://docs.pipewire.org/page_man_pw-cli_1.html>.

- 모든 노드(싱크 및 소스)와 그 ID를 출력:

`pw-cli list-objects Node`

- 특정 ID를 가진 객체에 대한 정보 출력:

`pw-cli info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>

- 모든 객체의 정보 출력:

`pw-cli info all`
