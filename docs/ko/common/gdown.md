---
layout: page
title: common/gdown (한국어)
description: "Google Drive 및 기타 URL에서 파일을 다운로드."
content_hash: 246a95eb7fdfc362132d50f75e122a9fc29c9e15
last_modified_at: 2024-10-21
related_topics:
  - title: English version
    url: /en/common/gdown.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/gdown.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gdown

Google Drive 및 기타 URL에서 파일을 다운로드.
더 많은 정보: <https://github.com/wkentaro/gdown>.

- URL에서 파일 다운로드:

`gdown `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">주소</span>

- 파일 ID를 사용하여 다운로드:

`gdown `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일_아이디</span>

- 퍼지 파일 ID 추출을 사용하여 다운로드 (<https://docs.google.com> 링크에서도 작동):

`gdown --fuzzy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">주소</span>

- 해당 ID 또는 전체 URL을 사용하여 폴더를 다운로드:

`gdown `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">폴더_아이디|주소</span>` -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_디렉토리</span>` --folder`

- tar 아카이브를 다운로드하고, `stdout`에 쓴 후 추출:

`gdown `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tar압축파일_주소</span>` -O - --quiet | tar xvf -`
