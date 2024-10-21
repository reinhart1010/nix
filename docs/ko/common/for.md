---
layout: page
title: common/for (한국어)
description: "명령을 여러 번 수행."
content_hash: f62bc11060720efa7b3e002791e0b3b10266fff4
last_modified_at: 2024-10-21
related_topics:
  - title: English version
    url: /en/common/for.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/for.html
    icon: bi bi-globe
tldri18n_status: 2
---
# for

명령을 여러 번 수행.
더 많은 정보: <https://www.gnu.org/software/bash/manual/bash.html#Looping-Constructs>.

- 지정된 각 항목에 대해 지정된 명령을 실행:

`for `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">변수</span>` in `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">item1 item2 ...</span>`; do `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "Loop is executed"</span>`; done`

- 주어진 숫자 범위에 대해 반복:

`for `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">변수</span>` in `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">{from</span>`..`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">to</span>`..`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">step}</span>`; do `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "Loop is executed"</span>`; done`

- 주어진 파일 목록을 반복:

`for `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">변수</span>` in `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>`; do `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "Loop is executed"</span>`; done`

- 주어진 디렉터리 목록을 반복:

`for `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">변수</span>` in `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리1/ 경로/대상/디렉터리2/ ...</span>`; do `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "Loop is executed"</span>`; done`

- 모든 디렉터리에서 주어진 명령을 수행:

`for `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">변수</span>` in */; do (cd "$`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">변수</span>`" || continue; `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "Loop is executed"</span>`) done`
