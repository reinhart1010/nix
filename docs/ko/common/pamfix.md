---
layout: page
title: common/pamfix (한국어)
description: "PAM, PBM, PGM 및 PPM 파일의 오류를 수정합니다."
content_hash: f0e3053518b83fe2e232109e6e7e00afa3ef6b31
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/pamfix.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/pamfix.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pamfix.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pamfix

PAM, PBM, PGM 및 PPM 파일의 오류를 수정합니다.
같이 보기: `pamfile`, `pamvalidate`.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pamfix.html>.

- 마지막 부분이 손상된 Netpbm 파일 수정:

`pamfix -truncate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/손상된_파일.ext</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.ext</span>

- 이미지의 `maxval`을 초과하는 픽셀 값을 낮추어 수정:

`pamfix -clip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/손상된_파일.ext</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.ext</span>

- 이미지의 `maxval`을 초과하는 픽셀 값을 증가시켜 수정:

`pamfix -changemaxval `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/손상된.pam|pbm|pgm|ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pam|pbm|pgm|ppm</span>
