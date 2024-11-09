---
layout: page
title: linux/pacstall (한국어)
description: "Ubuntu용 AUR 패키지 관리자."
content_hash: 438c4b4dd45819f7548ec9a3b9aefa588f4962fe
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/pacstall.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/pacstall.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pacstall

Ubuntu용 AUR 패키지 관리자.
더 많은 정보: <https://github.com/pacstall/pacstall>.

- 패키지 이름으로 패키지 데이터베이스 검색:

`pacstall --search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색어</span>

- 패키지 설치:

`pacstall --install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 패키지 제거:

`pacstall --remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 저장소를 데이터베이스에 추가 (GitHub 및 GitLab만 지원):

`pacstall --add-repo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_저장소_위치</span>

- pacstall 스크립트 업데이트:

`pacstall --update`

- 모든 패키지 업데이트:

`pacstall --upgrade`

- 패키지 정보 표시:

`pacstall --cache-info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 설치된 모든 패키지 나열:

`pacstall --list`
