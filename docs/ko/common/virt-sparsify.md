---
layout: page
title: common/virt-sparsify (한국어)
description: "가상 머신 드라이브 이미지를 Thin Provisioning으로 변환."
content_hash: ae6340d0c1302c57c3d3cfb872b6f37d3091476e
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/virt-sparsify.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/virt-sparsify.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># virt-sparsify

가상 머신 드라이브 이미지를 Thin Provisioning으로 변환.
주의: 데이터 손상을 방지하기 위해 오프라인 상태의 머신에서만 사용하세요.
더 많은 정보: <https://libguestfs.org>.

- 스냅샷이 없는 상태로 비압축된 이미지를 압축된 스파스 이미지로 생성:

`virt-sparsify --compress `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/image.qcow2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/image_new.qcow2</span>

- 이미지를 제자리에서 스파스 처리:

`virt-sparsify --in-place `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/image.img</span>
