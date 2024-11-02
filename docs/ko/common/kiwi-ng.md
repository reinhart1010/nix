---
layout: page
title: common/kiwi-ng (한국어)
description: "운영 체제 이미지 및 어플라이언스 빌더."
content_hash: 4403a5ab7f040a06a76b03f24cc523c007687e50
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/kiwi-ng.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/kiwi-ng.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># kiwi-ng

운영 체제 이미지 및 어플라이언스 빌더.
더 많은 정보: <https://osinside.github.io/kiwi/>.

- 어플라이언스 빌드:

`kiwi-ng system build --description=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` --target-dir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 빌드된 어플라이언스의 빌드 결과 표시:

`kiwi-ng result list --target-dir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 도움말 표시:

`kiwi-ng help`

- 버전 표시:

`kiwi-ng -v`
