---
layout: page
title: common/httprobe (한국어)
description: "작동하는 HTTP 및 HTTPS 서버에 대한 도메인 밒 프로브 목록을 가져옴."
content_hash: 79f8b79388782dff693779c7045a4c8a3a97eb78
last_modified_at: 2024-11-04
related_topics:
  - title: English version
    url: /en/common/httprobe.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/httprobe.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># httprobe

작동하는 HTTP 및 HTTPS 서버에 대한 도메인 밒 프로브 목록을 가져옴.
더 많은 정보: <https://github.com/tomnomnom/httprobe>.

- 텍스트 파일에서 도에인 목록을 조사:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력_파일</span>` | httprobe`

- HTTPS가 작동하지 않는 경우에만 HTTP 확인:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력_파일</span>` | httprobe --prefer-https`

- 특정 프로토콜을 사용하여 추가 포트를 조사:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력_파일</span>` | httprobe -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https:2222</span>

- 도움말 표시:

`httprobe --help`
