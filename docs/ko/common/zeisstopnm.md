---
layout: page
title: common/zeisstopnm (한국어)
description: "Zeiss 공초점 파일을 Netbpm 형식으로 변환."
content_hash: 4ed66fc9b63618aff37b0618fbba2e5b4ba4ed09
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/zeisstopnm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/zeisstopnm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># zeisstopnm

Zeiss 공초점 파일을 Netbpm 형식으로 변환.
더 많은 정보: <https://manned.org/zeisstopnm.1>.

- Zeiss 공초점 파일을 `.pgm` 또는 `.ppm` 형식으로 변환:

`zeisstopnm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 대상 파일 형식을 명시적으로 지정하여 Zeiss 공초점 파일을 Netbpm 형식으로 변환:

`zeisstopnm -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pgm|ppm</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
