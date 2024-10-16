---
layout: page
title: common/enscript (한국어)
description: "텍스트 파일을 PostScript, HTML, RTF, ANSI 및 겹쳐쓰기로 변환."
content_hash: ce41722387e92eb00f5e16fca530c2f4f8df2442
last_modified_at: 2024-10-16
related_topics:
  - title: English version
    url: /en/common/enscript.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/enscript.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/enscript.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># enscript

텍스트 파일을 PostScript, HTML, RTF, ANSI 및 겹쳐쓰기로 변환.
더 많은 정보: <https://www.gnu.org/software/enscript>.

- 텍스트 파일에서 PostScript 파일:

`enscript `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일</span>` --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일</span>

- PostScript와 다른 언어로 파일을 생성:

`enscript `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일</span>` --language=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">html|rtf|...</span>` --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일</span>

- 페이지를 열(최대 9개)로 분할하여 가로 레이아웃으로 PostScript 파일을 생성:

`enscript `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일</span>` --columns=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">숫자</span>` --landscape --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일</span>

- 사용 가능한 구문 강조 언어 및 파일 형식 표시:

`enscript --help-highlight`

- 지정된 언어에 대한 구문 강조 및 색상을 사용하여 PostScript 파일을 생성:

`enscript `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일</span>` --color=1 --highlight=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">언어</span>` --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일</span>
