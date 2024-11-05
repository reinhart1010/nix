---
layout: page
title: common/hyperfine (한국어)
description: "커멘드라인 벤치마킹 도구."
content_hash: a6403d4c503102d6609187baf71e39a4fefc9093
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/hyperfine.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/hyperfine.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/hyperfine.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># hyperfine

커멘드라인 벤치마킹 도구.
더 많은 정보: <https://github.com/sharkdp/hyperfine/>.

- 최소 10회 실행하여, 기본 벤치마크를 실행:

`hyperfine '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">make</span>`'`

- 비교 벤치마크 실행:

`hyperfine '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">make target1</span>`' '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">make target2</span>`'`

- 최소 벤치마킹 실행 횟수 변경:

`hyperfine --min-runs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7</span>` '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">make</span>`'`

- 웜업으로 벤치마크 수행:

`hyperfine --warmup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">make</span>`'`

- 각 벤치마크 실행 전에 명령을 실행 (캐시 지우기, 등):

`hyperfine --prepare '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">make clean</span>`' '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">make</span>`'`

- 각 실행마다 단일 매개변수가 변경되는 벤치마크를 실행:

`hyperfine --prepare '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">make clean</span>`' --parameter-scan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스레드_수</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">make -j {스레드_수}</span>`'`
