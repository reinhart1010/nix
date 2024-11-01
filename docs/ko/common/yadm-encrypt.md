---
layout: page
title: common/yadm-encrypt (한국어)
description: "지정된 암호화 파일에 나열된 파일 암호화."
content_hash: 70933625b5e04ac4dc907015769247b0a147e911
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/yadm-encrypt.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/yadm-encrypt.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># yadm-encrypt

지정된 암호화 파일에 나열된 파일 암호화.
파일이 암호화된 후 지정된 아카이브 폴더에 저장됩니다.
더 많은 정보: <https://yadm.io/docs/encryption>.

- 지정된 암호화 파일에 나열된 파일 암호화:

`yadm encrypt`

- 암호화를 위한 필수 파일 및 폴더 생성:

`touch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/암호화_파일</span>` && mkdir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/아카이브_폴더</span>
