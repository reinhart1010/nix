---
layout: page
title: common/pbmtext (한국어)
description: "텍스트를 PBM 이미지로 렌더링."
content_hash: c96a1051b1e3d89d7da32835ef87ef9bcdd5f7b8
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/pbmtext.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pbmtext.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pbmtext

텍스트를 PBM 이미지로 렌더링.
같이 보기: `pbmtextps`.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pbmtext.html>.

- 한 줄의 텍스트를 PBM 이미지로 렌더링:

`pbmtext "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hello World!</span>`" > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pbm</span>

- 여러 줄의 텍스트를 PBM 이미지로 렌더링:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hello\nWorld!</span>`" | pbmtext > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pbm</span>

- PBM 파일로 제공된 사용자 지정 폰트를 사용하여 텍스트 렌더링:

`pbmtext -font `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폰트.pbm</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hello World!</span>`" > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pbm</span>

- 문자와 줄 사이의 픽셀 수 지정:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hello\nWorld!</span>`" | pbmtext -space `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` -lspace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pbm</span>
