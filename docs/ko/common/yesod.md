---
layout: page
title: common/yesod (한국어)
description: "Haskell 기반 웹 프레임워크 Yesod의 도우미 도구."
content_hash: eb3f116510be8ba5129501bf6659c272a1230756
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/yesod.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/yesod.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># yesod

Haskell 기반 웹 프레임워크 Yesod의 도우미 도구.
모든 Yesod 명령은 `stack` 프로젝트 관리자를 통해 실행됩니다.
더 많은 정보: <https://github.com/yesodweb/yesod>.

- `my-project` 디렉토리에 SQLite를 백엔드로 하는 새로운 스캐폴딩 사이트 생성:

`stack new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my-project</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">yesod-sqlite</span>

- Yesod 스캐폴딩 사이트 내에서 Yesod CLI 도구 설치:

`stack build yesod-bin cabal-install --install-ghc`

- 개발 서버 시작:

`stack exec -- yesod devel`

- 변경된 템플릿 Haskell 의존성을 가진 파일 터치:

`stack exec -- yesod touch`

- Keter(Yesod의 배포 관리자)를 사용하여 애플리케이션 배포:

`stack exec -- yesod keter`
