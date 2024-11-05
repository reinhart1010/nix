---
layout: page
title: common/pamtotiff (한국어)
description: "PAM 이미지를 TIFF 파일로 변환."
content_hash: c45635440711b0f80cce120acd254a418b48c03b
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/pamtotiff.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/pamtotiff.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pamtotiff.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pamtotiff

PAM 이미지를 TIFF 파일로 변환.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pamtotiff.html>.

- PAM 이미지를 TIFF 이미지로 변환:

`pamtotiff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.tiff</span>

- 출력 파일의 압축 방식을 명시적으로 지정:

`pamtotiff -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">none|packbits|lzw|g3|g4|flate|adobeflate</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.tiff</span>

- 입력 이미지가 그레이스케일일지라도 항상 컬러 TIFF 이미지를 생성:

`pamtotiff -color `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.tiff</span>
