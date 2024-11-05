---
layout: page
title: common/pamstretch (한국어)
description: "PAM 이미지를 픽셀 간 보간을 통해 확대."
content_hash: 83bb3d9335bdb8141402232a9c32924d6b53c01d
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/pamstretch.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/pamstretch.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pamstretch.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pamstretch

PAM 이미지를 픽셀 간 보간을 통해 확대.
같이 보기: `pamstretch-gen`, `pamenlarge`, `pamscale`.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pamstretch.html>.

- PAM 이미지를 정수 배율로 확대:

`pamstretch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">N</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pam</span>

- PAM 이미지를 가로 및 세로 방향으로 지정된 배율로 확대:

`pamstretch -xscale `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">XN</span>` -yscale `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YN</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pam</span>
