---
layout: page
title: common/iconv (한국어)
description: "한 인코딩에서 다른 인코딩으로 텍스트를 변환."
content_hash: 4b662935e8ae6d87ef3ab6aa41642e24dd83c07a
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/iconv.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/iconv.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># iconv

한 인코딩에서 다른 인코딩으로 텍스트를 변환.
더 많은 정보: <https://manned.org/iconv>.

- 파일을 특정 인코딩으로 변환하고, `stdout`으로 출력:

`iconv -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">현재_인코딩</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">특정_인코딩</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력_파일</span>

- 파일을 현재 로케일의 인코딩으로 변환하고, 파일로 출력:

`iconv -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">현재_인코딩</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력_파일</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력_파일</span>

- 지원되는 인코딩 나열:

`iconv -l`
