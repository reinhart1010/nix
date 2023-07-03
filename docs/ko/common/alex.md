---
layout: page
title: common/alex (한국어)
description: "민감하지 않고, 사려깊지 않은 글을 잡는 도구."
content_hash: 78927623a3d8b99d3ee7e74621421a449b66ffd1
last_modified_at: 2023-07-03
related_topics:
  - title: English version
    url: /en/common/alex.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/alex.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/alex.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/alex.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/alex.html
    icon: bi bi-globe
---
# alex

민감하지 않고, 사려깊지 않은 글을 잡는 도구.
이것은 당신이 선호 성별, 양극화, 인종 관련, 종교에 대한 고려가 불분명하거나 다른 문구가 아닌 문구를 찾는데 도움이 됩니다.
더 많은 정보: <https://github.com/get-alex/alex>.

- `stdin`으로부터 텍스트 분석:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">His network looks good</span>` | alex --stdin`

- 현재 디렉토리의 모든 파일 분석:

`alex`

- 특정 파일 분석:

`alex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">textfile.md</span>

- `example.md`를 제외한 모든 Markdown 파일 분석:

`alex *.md !`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.md</span>
