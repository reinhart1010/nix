---
layout: page
title: common/gpgv (한국어)
description: "OpenPGP 서명을 확인."
content_hash: c9cc8610f19b523a66e1376b3e5601c182656b5e
last_modified_at: 2024-10-29
related_topics:
  - title: English version
    url: /en/common/gpgv.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/gpgv.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gpgv

OpenPGP 서명을 확인.
더 많은 정보: <https://www.gnupg.org/documentation/manuals/gnupg/gpgv.html>.

- 서명된 파일을 확인:

`gpgv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 분리된 서명을 사용하여 서명된 파일을 확인:

`gpgv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/서명</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 키링 목록에 파일을 추가 (내보낸 단일 키도 키링으로 간주됨):

`gpgv --keyring `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./alice.keyring</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/서명</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
