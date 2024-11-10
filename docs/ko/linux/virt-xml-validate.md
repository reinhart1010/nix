---
layout: page
title: linux/virt-xml-validate (한국어)
description: "`libvirt` XML 파일을 스키마에 따라 검증."
content_hash: b900dca32e94c8cf687d113d9a9630932bd0bfd0
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/virt-xml-validate.html
    icon: bi bi-globe
tldri18n_status: 2
---
# virt-xml-validate

`libvirt` XML 파일을 스키마에 따라 검증.
스키마가 지정되지 않으면, XML 파일의 루트 요소에 의해 스키마가 결정됩니다.
더 많은 정보: <https://libvirt.org/manpages/virt-xml-validate.html>.

- 특정 스키마에 따라 XML 파일 검증:

`virt-xml-validate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.xml</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스키마</span>

- 도메인 스키마에 따라 도메인 XML 검증:

`virt-xml-validate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/도메인.xml</span>` domain`
