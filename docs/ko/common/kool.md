---
layout: page
title: common/kool (한국어)
description: "소프트웨어 개발 환경을 구축."
content_hash: 55e7a0e6e77942d3dc4ee99307f2eada51e41cbb
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/kool.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/kool.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># kool

소프트웨어 개발 환경을 구축.
더 많은 정보: <https://kool.dev/docs/>.

- 특정 프리셋을 사용하여 프로젝트 생성:

`kool create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프리셋</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로젝트_이름</span>

- 현재 디렉토리의 `kool.yml` 파일에 정의된 특정 스크립트 실행:

`kool run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스크립트</span>

- 현재 디렉토리의 서비스 시작/중지:

`kool `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start|stop</span>

- 현재 디렉토리의 서비스 상태 표시:

`kool status`

- 최신 버전으로 업데이트:

`kool self-update`

- 지정된 셸에 대한 자동 완성 스크립트 출력:

`kool completion `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash|fish|powershell|zsh</span>
