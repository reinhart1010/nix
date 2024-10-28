---
layout: page
title: linux/zathura (한국어)
description: "vim과 유사한 모달 문서 뷰어로, 통합 명령줄을 제공합니다."
content_hash: 604831cf84afad505ab47cb2d09be485847fd0a6
last_modified_at: 2024-10-28
related_topics:
  - title: Deutsch version
    url: /de/linux/zathura.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/zathura.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/zathura.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/zathura.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/zathura.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># zathura

vim과 유사한 모달 문서 뷰어로, 통합 명령줄을 제공합니다.
백엔드(poppler, PostScript, 또는 DjVu)가 설치되었는지 확인하세요.
더 많은 정보: <https://pwmt.org/projects/zathura/>.

- 파일 열기:

`zathura `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 왼쪽/위/아래/오른쪽으로 이동:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">H|J|K|L|화살표 키</span>

- 회전:

`r`

- 색상 반전:

`<Ctrl> + R`

- 주어진 문자열로 텍스트 검색:

`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문자열</span>

- 북마크 생성/삭제:

`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bmark|bdelete</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">북마크_이름</span>

- 북마크 목록 나열:

`:blist`
