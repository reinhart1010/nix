---
layout: page
title: linux/snapper (한국어)
description: "파일 시스템 스냅샷 관리 도구."
content_hash: a4f9fcb5e200c4de96b23389fd889adf95f4a01f
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/linux/snapper.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/snapper.html
    icon: bi bi-globe
tldri18n_status: 2
---
# snapper

파일 시스템 스냅샷 관리 도구.
더 많은 정보: <http://snapper.io/manpages/snapper.html>.

- 스냅샷 구성 목록 나열:

`snapper list-configs`

- 스냅퍼 구성 생성:

`snapper -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">구성</span>` create-config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 설명과 함께 스냅샷 생성:

`snapper -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">구성</span>` create -d "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스냅샷_설명</span>`"`

- 특정 구성의 스냅샷 목록 나열:

`snapper -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">구성</span>` list`

- 스냅샷 삭제:

`snapper -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">구성</span>` delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스냅샷_번호</span>

- 스냅샷 범위 삭제:

`snapper -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">구성</span>` delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스냅샷1</span>`-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스냅샷2</span>
