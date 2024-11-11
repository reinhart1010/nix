---
layout: page
title: linux/sxiv (한국어)
description: "Simple X Image Viewer."
content_hash: 57b1d45acc7f5131a82783b648e7449b5cd1e998
last_modified_at: 2024-11-11
related_topics:
  - title: English version
    url: /en/linux/sxiv.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/sxiv.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sxiv

Simple X Image Viewer.
더 많은 정보: <https://github.com/muennich/sxiv>.

- 이미지 열기:

`sxiv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지</span>

- 전체 화면 모드로 이미지 열기:

`sxiv -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- `stdin`에서 파일명을 읽어 개행으로 구분된 이미지 목록 열기:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` | sxiv -i`

- 하나 이상의 이미지를 슬라이드쇼로 열기:

`sxiv -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">초</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지1 경로/대상/이미지2</span>

- 하나 이상의 이미지를 썸네일 모드로 열기:

`sxiv -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지1 경로/대상/이미지2</span>
