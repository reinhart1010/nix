---
layout: page
title: linux/cewl (한국어)
description: "웹 콘텐츠에서 크래킹용 단어 목록을 만드는 URL 수집 도구."
content_hash: 792d6009f18d7564450443ea8471cc998529643c
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/cewl.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/cewl.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cewl

웹 콘텐츠에서 크래킹용 단어 목록을 만드는 URL 수집 도구.
더 많은 정보: <https://digi.ninja/projects/cewl.php>.

- 지정된 URL에서 링크 깊이 2까지 단어 목록 파일 생성:

`cewl --depth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` --write `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/단어목록.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- 지정된 URL에서 최소 5자 이상의 알파벳과 숫자로 이루어진 단어 목록 출력:

`cewl --with-numbers --min_word_length `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- 디버그 모드로 이메일 주소를 포함한 지정된 URL에서 단어 목록 출력:

`cewl --debug --email `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- HTTP 기본 또는 다이제스트 인증을 사용하여 지정된 URL에서 단어 목록 출력:

`cewl --auth_type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">basic|digest</span>` --auth_user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` --auth_pass `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- 프록시를 통해 지정된 URL에서 단어 목록 출력:

`cewl --proxy_host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>` --proxy_port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>
