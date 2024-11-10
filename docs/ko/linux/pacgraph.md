---
layout: page
title: linux/pacgraph (한국어)
description: "설치된 패키지의 그래프를 PNG/SVG/GUI/콘솔로 그립니다."
content_hash: 0bc80c35f1b720fccaad8bea989b7213a098655c
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/pacgraph.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/pacgraph.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/pacgraph.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacgraph

설치된 패키지의 그래프를 PNG/SVG/GUI/콘솔로 그립니다.
더 많은 정보: <https://github.com/keenerd/pacgraph>.

- SVG 및 PNG 그래프 생성:

`pacgraph`

- SVG 그래프 생성:

`pacgraph --svg`

- 콘솔에 요약 출력:

`pacgraph --console`

- 기본 파일명/위치 재정의 (참고: 파일 확장자를 지정하지 마십시오):

`pacgraph --file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 의존성이 아닌 패키지의 색상 변경:

`pacgraph --top=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">색상</span>

- 패키지 의존성의 색상 변경:

`pacgraph --dep=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">색상</span>

- 그래프 배경 색상 변경:

`pacgraph --background=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">색상</span>

- 패키지 간 연결의 색상 변경:

`pacgraph --link=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">색상</span>
