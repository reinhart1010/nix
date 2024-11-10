---
layout: page
title: common/sponge (한국어)
description: "입력을 출력 파일에 쓰기 전에 흡수합니다."
content_hash: e8d4c1cb6b39961018ba1aaae789cce276f80f34
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/sponge.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sponge

입력을 출력 파일에 쓰기 전에 흡수합니다.
더 많은 정보: <https://manned.org/sponge>.

- 파일 내용을 원본 파일에 추가:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` | sponge -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일에서 #으로 시작하는 모든 줄 제거:

`grep -v '^`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">#</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` | sponge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
