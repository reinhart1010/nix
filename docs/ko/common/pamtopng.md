---
layout: page
title: common/pamtopng (한국어)
description: "PAM 이미지를 PNG로 변환."
content_hash: de0c73e06e767dfd32b5e843468e7fda39e76dc3
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/pamtopng.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/pamtopng.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pamtopng.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pamtopng

PAM 이미지를 PNG로 변환.
같이 보기: `pnmtopng`, `pngtopam`.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pamtopng.html>.

- 지정된 PAM 이미지를 PNG로 변환:

`pamtopng `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.png</span>

- 출력 이미지에서 지정된 색상을 투명하게 표시:

`pamtopng -transparent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">색상</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.png</span>

- 지정된 파일의 텍스트를 출력물에 tEXt 청크로 포함:

`pamtopng -text `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.png</span>

- 출력 파일을 Adam7 형식으로 인터레이스 처리:

`pamtopng -interlace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.png</span>
