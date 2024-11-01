---
layout: page
title: common/zapier-convert (한국어)
description: "Visual Builder 통합을 CLI 통합으로 변환."
content_hash: 164d841b1f8da130edca8110474dd3d3c4c556a0
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/zapier-convert.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/zapier-convert.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># zapier convert

Visual Builder 통합을 CLI 통합으로 변환.
더 많은 정보: <https://platform.zapier.com/reference/cli#convert>.

- Visual Builder 통합 변환:

`zapier convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">integration_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 특정 버전의 Visual Builder 통합 변환:

`zapier convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">integration_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-v|--version</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>

- 추가 디버깅 출력 표시:

`zapier convert --debug`
