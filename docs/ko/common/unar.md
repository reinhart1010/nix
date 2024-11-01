---
layout: page
title: common/unar (한국어)
description: "아카이브 파일의 내용을 추출."
content_hash: 2340c276788d97e6be3340b1f19335d2686262c3
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/unar.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/unar.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/unar.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># unar

아카이브 파일의 내용을 추출.
더 많은 정보: <https://manned.org/unar>.

- 아카이브를 현재 디렉토리에 추출:

`unar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/아카이브</span>

- 아카이브를 지정된 디렉토리에 추출:

`unar -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/아카이브</span>

- 압축 해제할 파일이 이미 존재할 경우 강제로 덮어쓰기:

`unar -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/아카이브</span>

- 압축 해제할 파일이 이미 존재할 경우 강제로 이름 변경:

`unar -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/아카이브</span>

- 압축 해제할 파일이 이미 존재할 경우 강제로 건너뛰기:

`unar -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/아카이브</span>
