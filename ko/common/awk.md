---
layout: page
title: common/awk (한국어)
description: "파일 작업을 위한 다목적 프로그래밍 언어."
content_hash: fe73bbec74a5264c7a800ed93706444f5285a820
related_topics:
  - title: English version
    url: /en/common/awk.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/awk.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/awk.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/awk.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/awk.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/awk.html
    icon: bi bi-globe
---
# awk

파일 작업을 위한 다목적 프로그래밍 언어.
더 많은 정보: <https://github.com/onetrueawk/awk>.

- 공백으로 구분 된 파일의 다섯 번째 열 (일명 필드)를 출력하기:

`awk '{print $5}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- 공백으로 구분 된 파일에서 `foo`을 포함한 두 번째 열 출력하기:

`awk '/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>`/ {print $2}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- 공백이 아닌 쉼표를 필드 구분 기호로 사용한 파일에서 각 줄의 마지막 열을 출력하기:

`awk -F ',' '{print $NF}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- 파일의 첫 번째 열에 있는 값을 더하고 합계를 출력:

`awk '{s+=$1} END {print s}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- 첫 번째 열에 있는 값을 더하고 값들을 출력하고 합계를 출력:

`awk '{s+=$1; print $1} END {print "--------"; print s}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- 첫 번째 줄부터 시작하여 세 번째 줄까지 모두 출력:

`awk 'NR%3==1' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- 세 번째 열부터 시작하여 모든 값을 출력:

`awk '{ s = ""; for (i=3; i <= NF; i++) s = s $i " "; print s }'`

- 조건에 따라 다른 값을 출력:

`awk '{if ($1 == "foo") print "Exact match foo"; else if ($1 ~ "bar") print "Partial match bar"; else print "Baz"}'`
