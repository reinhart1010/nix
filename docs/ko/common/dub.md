---
layout: page
title: common/dub (한국어)
description: "D 패키지의 패키지 관리."
content_hash: e92fc8fdb807e87b4f2bd1ff53e342c4e470be1c
last_modified_at: 2024-10-16
related_topics:
  - title: English version
    url: /en/common/dub.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/dub.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dub

D 패키지의 패키지 관리.
더 많은 정보: <https://dub.pm/commandline>.

- 대화형으로 새 D 프로젝트 생성:

`dub init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로젝트_이름</span>

- 비대화형으로 새 D 프로젝트 생성:

`dub init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로젝트_이름</span>` -n`

- D 프로젝트 빌드 및 실행:

`dub`

- D 프로젝트의 `dub.json` 또는 `dub.sdl` 파일에 지정된 종속성을 설치:

`dub fetch`

- D 프로젝트의 종속성을 업데이트:

`dub upgrade`

- 도움말 표시:

`dub --help`
