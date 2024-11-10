---
layout: page
title: common/srm (한국어)
description: "파일이나 디렉터리를 안전하게 제거."
content_hash: 1149287d7f00de0dba357e922ff6256d7dae6a42
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/srm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# srm

파일이나 디렉터리를 안전하게 제거.
기존 데이터를 한 번 또는 여러 번 덮어씁니다. `rm` 명령의 대체품.
더 많은 정보: <https://srm.sourceforge.net/srm.html>.

- 파일을 한 번 무작위 데이터로 덮어쓴 후 제거:

`srm -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일을 일곱 번 무작위 데이터로 덮어쓴 후 제거:

`srm -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 디렉터리와 그 내용을 재귀적으로 제거하며 각 파일을 한 번 무작위 데이터로 덮어쓰기:

`srm -r -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 제거하기 전에 매번 확인:

`srm -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">\*</span>
