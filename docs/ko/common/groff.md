---
layout: page
title: common/groff (한국어)
description: "`troff` 및 `nroff` 조판 유틸리티를 GNU로 대체."
content_hash: 9b868918aadafc9cca25fae042097e59bb649fe9
last_modified_at: 2024-10-31
related_topics:
  - title: English version
    url: /en/common/groff.html
    icon: bi bi-globe
tldri18n_status: 2
---
# groff

`troff` 및 `nroff` 조판 유틸리티를 GNU로 대체.
더 많은 정보: <https://www.gnu.org/software/groff>.

- PostScript 프린터의 출력 형식을 지정하고, 출력을 파일에 저장:

`groff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력파일.roff</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력파일.ps</span>

- ASCII 출력 장치를 사용하여 매뉴얼 페이지를 렌더링하고, 호출기를 사용하여 표시:

`groff -man -T ascii `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상//manpage.1</span>` | less --RAW-CONTROL-CHARS`

- 매뉴얼 페이지를 HTML 파일로 렌더링:

`groff -man -T html `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상//manpage.1</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상//manpage.html</span>

- [me] 매크로 세트를 사용하여 테이블([t]ables) 및 그림([p]ictures)이 포함된 roff 파일을 PDF로 조판하고, 출력을 저장:

`groff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-t</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-p</span>` -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">me</span>` -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력파일.me</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력파일.pdf</span>

- `grog` 유틸리티에서 추측한 전처리기 및 매크로 옵션을 사용하여 `groff` 명령을 실행:

`eval "$(grog -T utf8 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력파일.me</span>`)"`
