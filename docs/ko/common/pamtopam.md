---
layout: page
title: common/pamtopam (한국어)
description: "PAM 이미지를 복사합니다."
content_hash: 4ea35836d282b71359b8c9e3d46c03eaee030309
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/pamtopam.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pamtopam.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pamtopam

PAM 이미지를 복사합니다.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pamtopam.html>.

- PAM 이미지(PBM, PGM, PPM 또는 PAM 이미지)를 `stdin`에서 `stdout`으로 복사:

`pamtopam < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pam</span>

- 버전 표시:

`pamtopam -version`
