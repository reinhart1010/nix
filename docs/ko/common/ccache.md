---
layout: page
title: common/ccache (한국어)
description: "C/C++ 컴파일러 캐시."
content_hash: 6d3ef2baec93664449b9ba5297066a7bac268ea1
last_modified_at: 2024-09-30
related_topics:
  - title: English version
    url: /en/common/ccache.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ccache.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ccache

C/C++ 컴파일러 캐시.
참고: 패키지는 일반적으로 `/usr/lib/ccache/bin`에 컴파일러에 대한 심볼릭 링크를 제공. 자동으로 `ccache`를 사용하려면 이 디렉토리를 `$PATH` 앞에 추가.
더 많은 정보: <https://ccache.dev/manual/latest.html>.

- 현재 캐시 통계 표시([s]tatistics):

`ccache --show-stats`

- 모든 캐시 지우기([C]lear):

`ccache --clear`

- 통계 재설정 ([z]ero) (캐시 자체는 아님):

`ccache --zero-stats`

- C 코드를 컴파일하고 컴파일된 출력을 캐시 (모든 `gcc` 호출에서 `ccache`를 사용하려면, 위를 참고):

`ccache gcc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.c</span>
