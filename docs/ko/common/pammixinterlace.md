---
layout: page
title: common/pammixinterlace (한국어)
description: "이미지의 각 행을 인접한 두 행과 병합."
content_hash: 77408321bc899c451a57cd6da7655ae2bfbe586f
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/pammixinterlace.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pammixinterlace.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pammixinterlace

이미지의 각 행을 인접한 두 행과 병합.
같이 보기: `pamdeinterlace`.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pammixinterlace.html>.

- 이미지의 각 행을 인접한 두 행과 병합:

`pammixinterlace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.ppm</span>

- 지정된 필터링 메커니즘 사용:

`pammixinterlace -filter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">linear|fir|ffmpeg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.ppm</span>

- 적응형 필터링 모드 활성화, 즉 명백히 빗살무늬 패턴의 일부인 픽셀만 수정:

`pammixinterlace -adaptive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.ppm</span>
