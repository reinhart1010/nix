---
layout: page
title: linux/xmodmap (한국어)
description: "X에서 키맵과 포인터 버튼 매핑을 수정하는 유틸리티."
content_hash: 79fdf272359b5f35aaf885e4f13189874680795e
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/xmodmap.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/xmodmap.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># xmodmap

X에서 키맵과 포인터 버튼 매핑을 수정하는 유틸리티.
더 많은 정보: <https://manned.org/xmodmap>.

- 포인터에서 좌클릭과 우클릭을 교체:

`xmodmap -e 'pointer = 3 2 1'`

- 키보드의 키를 다른 키로 재할당:

`xmodmap -e 'keycode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키코드</span>` = `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키이름</span>`'`

- 키보드의 키 비활성화:

`xmodmap -e 'keycode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키코드</span>` ='`

- 지정된 파일에 있는 모든 xmodmap 표현 실행:

`xmodmap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
