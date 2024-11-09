---
layout: page
title: common/transfersh (한국어)
description: "비공식적인 transfer.sh 명령줄 클라이언트."
content_hash: f4dfa2c5dc43b436ea078bfee2c260b52d4bd9ac
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/transfersh.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/transfersh.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># transfersh

비공식적인 transfer.sh 명령줄 클라이언트.
더 많은 정보: <https://github.com/AlpixTM/transfersh>.

- 파일을 transfer.sh에 업로드:

`transfersh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 진행 표시줄을 보여주며 파일 업로드 (Python 패키지 `requests_toolbelt` 필요):

`transfersh --progress `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 다른 파일 이름으로 파일 업로드:

`transfersh --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일명</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 사용자 지정 transfer.sh 서버에 파일 업로드:

`transfersh --servername `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">업로드.서버.이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 디렉터리의 모든 파일을 재귀적으로 업로드:

`transfersh --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더/</span>

- 특정 디렉터리를 압축되지 않은 tar로 업로드:

`transfersh -rt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>
