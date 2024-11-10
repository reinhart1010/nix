---
layout: page
title: common/tsort (한국어)
description: "위상 정렬 수행."
content_hash: 47fb55cc6d0aeb12df54e298644912ae29e5d084
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/tsort.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/tsort.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tsort

위상 정렬 수행.
일반적으로 유향 비순환 그래프에서 노드의 의존성 순서를 보여주는 데 사용됨.
더 많은 정보: <https://www.gnu.org/software/coreutils/tsort>.

- 공백으로 구분된 입력의 각 줄에 대해 부분 정렬과 일치하는 위상 정렬 수행:

`tsort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 문자열에 대해 일관된 위상 정렬 수행:

`echo -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">UI Backend\nBackend Database\nDocs UI</span>`" | tsort`
