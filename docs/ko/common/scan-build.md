---
layout: page
title: common/scan-build (한국어)
description: "코드베이스에 정적 분석기를 실행하여 정기 빌드의 일부로 사용하는 명령줄 도구."
content_hash: ef9b216adffa7d1f7257dd99938d863db42a0aa6
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/scan-build.html
    icon: bi bi-globe
tldri18n_status: 2
---
# scan-build

코드베이스에 정적 분석기를 실행하여 정기 빌드의 일부로 사용하는 명령줄 도구.
더 많은 정보: <https://clang-analyzer.llvm.org/scan-build.html>.

- 현재 디렉터리에서 프로젝트를 빌드하고 분석:

`scan-build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">make</span>

- 명령을 실행하고 모든 후속 옵션을 해당 명령에 전달:

`scan-build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어_인수들</span>

- 도움말 표시:

`scan-build`
