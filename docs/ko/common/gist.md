---
layout: page
title: common/gist (한국어)
description: "<https://gist.github.com>에 코드 업로드."
content_hash: c918f32a5c07b2fca2a887ea0a26ceb66a2f3c34
last_modified_at: 2024-10-22
related_topics:
  - title: English version
    url: /en/common/gist.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/gist.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gist

<https://gist.github.com>에 코드 업로드.
더 많은 정보: <https://github.com/defunkt/gist>.

- 이 컴퓨터에서 gist에 로그인:

`gist --login`

- 원하는 수의 텍스트 파일에서 gist를 생성:

`gist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일2.txt</span>

- 설명이 포함된 비공개 gist를 생성:

`gist --private --description "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">의미있는 설명</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.txt</span>

- `stdin`의 내용을 읽고 그것으로부터 gist를 생성:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "hello world"</span>` | gist`

- 공개 및 비공개 gist를 나열:

`gist --list`

- 모든 사용자에 대한 모든 공개 gist를 나열:

`gist --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>

- URL의 ID를 사용하여 gist를 업데이트:

`gist --update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GIST_아이디</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.txt</span>
