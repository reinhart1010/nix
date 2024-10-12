---
layout: page
title: common/dcfldd (한국어)
description: "법의학 및 보안을 위한 향상된 dd 버전."
content_hash: 9d9c7e2fb14e72b977adc35c9d798e6bc432af9c
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/dcfldd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dcfldd

법의학 및 보안을 위한 향상된 dd 버전.
더 많은 정보: <https://dcfldd.sourceforge.net/>.

- 원시 이미지 파일에 디스크를 복사하고 SHA256을 사용해 이미지를 해시:

`dcfldd if=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/disk_device</span>` of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.img</span>` hash=sha256 hashlog=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.hash</span>

- 디스크를 원시 이미지 파일에 복사하여, 각 1GB 청크를 해싱:

`dcfldd if=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/disk_device</span>` of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.img</span>` hash=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sha512|sha384|sha256|sha1|md5</span>` hashlog=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.hash</span>` hashwindow=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1G</span>
