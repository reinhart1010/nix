---
layout: page
title: common/cb (한국어)
description: "터미널에서 무엇이든 잘라내고, 복사하고, 붙여넣으세요."
content_hash: ece13d10d38c0f2db99563e6db199ef870ea2e40
last_modified_at: 2024-09-29
related_topics:
  - title: English version
    url: /en/common/cb.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/cb.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cb.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cb

터미널에서 무엇이든 잘라내고, 복사하고, 붙여넣으세요.
더 많은 정보: <https://github.com/Slackadays/Clipboard>.

- 모든 클립보드 표시:

`cb`

- 파일을 클립보드에 복사:

`cb copy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 일부 텍스트를 클립보드에 복사:

`cb copy "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">일부 예시 텍스트</span>`"`

- 파이프된 데이터를 클립보드에 복사:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">일부 예시 텍스트</span>`" | cb`

- 클립보드 내용 붙여넣기:

`cb paste`

- 클립보드 콘텐츠 파이프 아웃:

`cb | cat`

- 클립보드 기록 보기:

`cb history`

- 클립보드 정보 표시:

`cb info`
