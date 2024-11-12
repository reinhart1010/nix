---
layout: page
title: osx/textutil (한국어)
description: "다양한 형식의 텍스트 파일을 조작."
content_hash: 56d9d110cde81cbb4f92a83d4375b6e353e6d857
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/textutil.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/textutil.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/textutil.html
    icon: bi bi-globe
tldri18n_status: 2
---
# textutil

다양한 형식의 텍스트 파일을 조작.
더 많은 정보: <https://keith.github.io/xcode-man-pages/textutil.1.html>.

- `foo.rtf` 파일에 대한 정보 표시:

`textutil -info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/foo.rtf</span>

- `foo.rtf`를 `foo.html`로 변환:

`textutil -convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">html</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/foo.rtf</span>

- 서식 있는 텍스트를 일반 텍스트로 변환:

`textutil `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/foo.rtf</span>` -convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">txt</span>

- `foo.txt`를 `foo.rtf`로 변환, Times 10 폰트 사용:

`textutil -convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rtf</span>` -font `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Times</span>` -fontsize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/foo.txt</span>

- 현재 디렉터리의 모든 RTF 파일을 불러와 내용을 연결하고, 결과를 `index.html`로 작성하며 HTML 제목을 "Several Files"로 설정:

`textutil -cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">html</span>` -title "Several Files" -output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/index.html</span>` *.rtf`
