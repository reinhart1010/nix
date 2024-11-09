---
layout: page
title: common/snyk (한국어)
description: "코드의 취약점을 찾아 위험을 해결합니다."
content_hash: 08f2529e679a7395ecc988471a49a272947b7ca6
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/snyk.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/snyk.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># snyk

코드의 취약점을 찾아 위험을 해결합니다.
더 많은 정보: <https://snyk.io>.

- Snyk 계정에 로그인:

`snyk auth`

- 코드에서 알려진 취약점을 테스트:

`snyk test`

- 로컬 Docker 이미지에서 알려진 취약점을 테스트:

`snyk test --docker `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">docker_이미지</span>

- 종속성과 취약점 상태를 snyk.io에 기록:

`snyk monitor`

- 취약점을 자동으로 패치하고 무시:

`snyk wizard`
