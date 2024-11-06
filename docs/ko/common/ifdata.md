---
layout: page
title: common/ifdata (한국어)
description: "네트워크 인터페이스에 대한 정보를 표시."
content_hash: bd004486997c3e0c2c26212c069b572cc8cc5cbb
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/ifdata.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ifdata.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ifdata

네트워크 인터페이스에 대한 정보를 표시.
더 많은 정보: <https://joeyh.name/code/moreutils/>.

- 지정된 인터페이스의 전체 구성을 표시:

`ifdata -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- 종료 코드를 통해 지정된 인터페이스의 존재([e]xistence)를 나타냄:

`ifdata -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- 지정된 인터페이스의 IPv4 주소([a]ddress)와 넷마스크([n]etmask)를 표시:

`ifdata -pa -pn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- 네트워크([N]etwork) 주소, 브로드캐스트([b]roadcast) 주소 및 지정된 인터페이스의 MTU를 표시:

`ifdata -pN -pb -pm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- 도움말 표시:

`ifdata`
