---
layout: page
title: common/mkcert (한국어)
description: "로컬에서 신뢰할 수 있는 개발 인증서 생성."
content_hash: b2c3aa3cb2597e198fe540c59dac555a117c15af
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/mkcert.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/mkcert.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mkcert

로컬에서 신뢰할 수 있는 개발 인증서 생성.
더 많은 정보: <https://github.com/FiloSottile/mkcert>.

- 시스템 신뢰 저장소에 로컬 CA 설치:

`mkcert -install`

- 주어진 도메인에 대한 인증서와 개인 키 생성:

`mkcert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.org</span>

- 여러 도메인에 대한 인증서와 개인 키 생성:

`mkcert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.org</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">myapp.dev</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">127.0.0.1</span>

- 주어진 도메인과 하위 도메인에 대한 와일드카드 인증서와 개인 키 생성:

`mkcert "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.example.it</span>`"`

- 로컬 CA 제거:

`mkcert -uninstall`
