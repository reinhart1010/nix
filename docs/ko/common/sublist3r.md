---
layout: page
title: common/sublist3r (한국어)
description: "침투 테스터를 위한 빠른 서브도메인 열거 도구."
content_hash: d35f5d71843229f877cc964cea6d23939a5584ef
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/sublist3r.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/sublist3r.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sublist3r

침투 테스터를 위한 빠른 서브도메인 열거 도구.
더 많은 정보: <https://github.com/aboul3la/Sublist3r>.

- 도메인의 서브도메인 찾기:

`sublist3r --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">도메인_이름</span>

- 도메인의 서브도메인을 찾고, 브루트 포스 검색도 활성화:

`sublist3r --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">도메인_이름</span>` --bruteforce`

- 찾은 서브도메인을 텍스트 파일에 저장:

`sublist3r --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">도메인_이름</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일</span>

- 도움말 표시:

`sublist3r --help`
