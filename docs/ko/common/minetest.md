---
layout: page
title: common/minetest (한국어)
description: "다중 사용자 무한 세계 블록 샌드박스."
content_hash: 521d8978a32994bafec63d4c6e355cdd572bc42d
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/minetest.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/minetest.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/minetest.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># minetest

다중 사용자 무한 세계 블록 샌드박스.
같이 보기: `minetestserver`, 서버 전용 바이너리.
더 많은 정보: <https://wiki.minetest.org/Minetest>.

- 클라이언트 모드에서 Minetest 시작:

`minetest`

- 특정 세계를 호스팅하여 서버 모드에서 Minetest 시작:

`minetest --server --world `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- 로그를 특정 파일에 기록:

`minetest --logfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 콘솔에 오류만 기록:

`minetest --quiet`
