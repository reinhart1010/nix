---
layout: page
title: common/pprof (한국어)
description: "프로파일 데이터의 시각화 및 분석을 위한 명령줄 도구."
content_hash: 158b42f9cde3b711e5a37416bfc02118778f6aa2
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/pprof.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pprof.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pprof

프로파일 데이터의 시각화 및 분석을 위한 명령줄 도구.
더 많은 정보: <https://github.com/google/pprof>.

- 특정 프로파일링 파일에서 텍스트 보고서 생성, fibbo 바이너리에 대해:

`pprof -top `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./fibbo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./fibbo-프로필.pb.gz</span>

- 그래프를 생성하고 웹 브라우저에서 열기:

`pprof -svg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./fibbo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./fibbo-프로필.pb.gz</span>

- 대화형 모드에서 pprof 실행하여 파일에 수동으로 `pprof` 실행 가능:

`pprof `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./fibbo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./fibbo-프로필.pb.gz</span>

- `pprof` 위에 웹 인터페이스를 제공하는 웹 서버 실행:

`pprof -http=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">localhost:8080</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./fibbo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./fibbo-프로필.pb.gz</span>

- HTTP 서버에서 프로파일을 가져와 보고서 생성:

`pprof `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://localhost:8080/debug/pprof</span>
