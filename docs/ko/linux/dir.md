---
layout: page
title: linux/dir (한국어)
description: "한 줄에 하나의 파일씩 디렉토리 내용을 나열하며, 특수 문자는 백슬래시 이스케이프 시퀀스로 표시됩니다."
content_hash: 560d77a3c178944f39afd34ac58fde14b657e674
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/dir.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/dir.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/dir.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dir

한 줄에 하나의 파일씩 디렉토리 내용을 나열하며, 특수 문자는 백슬래시 이스케이프 시퀀스로 표시됩니다.
`ls -C --escape`와 같이 작동합니다.
더 많은 정보: <https://manned.org/dir>.

- 숨김 파일을 포함한 모든 파일 나열:

`dir --all`

- 파일 작성자 정보를 포함하여 나열 (`-l` 필요):

`dir -l --author`

- 지정된 블롭 패턴과 일치하는 파일을 제외하고 나열:

`dir --hide=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패턴</span>

- 하위 디렉토리를 재귀적으로 나열:

`dir --recursive`

- 도움말 표시:

`dir --help`
