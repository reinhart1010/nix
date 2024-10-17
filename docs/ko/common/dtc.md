---
layout: page
title: common/dtc (한국어)
description: "장치 트리 컴파일러는 형식 간에 장치 트리를 다시 컴파일하는 도구."
content_hash: ce9e93be3db44fc298e370492ffa6c5639db4103
last_modified_at: 2024-10-17
related_topics:
  - title: English version
    url: /en/common/dtc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dtc

장치 트리 컴파일러는 형식 간에 장치 트리를 다시 컴파일하는 도구.
더 많은 정보: <https://github.com/dgibson/dtc>.

- `.dtb` 파일을 읽을 수 있는 `.dts` 파일로 디컴파일:

`dtc -I dtb -O dts -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.dts</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일.dtb</span>
