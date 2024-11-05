---
layout: page
title: common/osv-scanner (한국어)
description: "다양한 매체에서 의존성을 스캔하고 OSV 데이터베이스와 대조합니다."
content_hash: 5f70ca35ea812bde5cb6e8963f4e092a0e8916a9
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/osv-scanner.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/osv-scanner.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># osv-scanner

다양한 매체에서 의존성을 스캔하고 OSV 데이터베이스와 대조합니다.
더 많은 정보: <https://osv.dev/about>.

- Docker 이미지를 스캔:

`osv-scanner -D `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">도커_이미지_이름</span>

- 패키지 잠금 파일을 스캔:

`osv-scanner -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/잠금파일</span>

- SBOM 파일을 스캔:

`osv-scanner -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/sbom_파일</span>

- 여러 디렉토리를 재귀적으로 스캔:

`osv-scanner -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">디렉토리1 디렉토리2 ...</span>

- Git 저장소 스캔 건너뛰기:

`osv-scanner --skip-git `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-r|-D</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상</span>

- 결과를 JSON 형식으로 출력:

`osv-scanner --json `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-D|-L|-S|-r</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상</span>
