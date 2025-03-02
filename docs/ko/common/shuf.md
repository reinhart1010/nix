---
layout: page
title: common/shuf (한국어)
description: "무작위 순열 생성."
content_hash: 5df38aacd6ad54e4cdbfd0341124859d2ea04c78
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/shuf.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/shuf.html
    icon: bi bi-globe
tldri18n_status: 2
---
# shuf

무작위 순열 생성.
더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/shuf-invocation.html>.

- 파일의 줄 순서를 무작위로 섞고 결과 출력:

`shuf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 결과의 처음 5개 항목만 출력:

`shuf --head-count=5 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 출력을 다른 파일에 쓰기:

`shuf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일</span>` --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일</span>

- 1-10 범위(포함)에서 임의의 숫자 3개 생성:

`shuf --head-count=3 --input-range=1-10 --repeat`
