---
layout: page
title: common/clifm (한국어)
description: "명령줄 파일 관리자."
content_hash: 3f0753539e65e68795833ae321ce3f2b4cd10427
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/common/clifm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/clifm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># clifm

명령줄 파일 관리자.
참고: `vifm`, `ranger`, `mc`, `nautilus`.
더 많은 정보: <https://github.com/leo-arch/clifm>.

- CliFM 시작:

`clifm`

- ELN (항목 목록 번호)이 12인 파일 또는 디렉터리 열기:

`12`

- 새 파일 또는 디렉터리 생성:

`n file dir/`

- 현재 디렉터리에서 PDF 파일 검색:

`/*.pdf`

- 현재 디렉터리에 있는 모든 PNG 파일을 선택:

`s *.png`

- 이전에 선택한 파일을 제거 (대신 `t`를 사용하여 파일을 휴지통으로 보냄):

`r sel`

- 도움말 표시:

`?`

- CliFM 종료:

`q`
