---
layout: page
title: common/od (한국어)
description: "파일 내용을 8진수, 10진수 또는 16진수 형식으로 표시."
content_hash: fb33360d4c6db9adc1dcc0a923c759a1c10c23ab
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/od.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/od.html
    icon: bi bi-globe
tldri18n_status: 2
---
# od

파일 내용을 8진수, 10진수 또는 16진수 형식으로 표시.
선택적으로 각 줄에 대한 바이트 오프셋 및/또는 인쇄 가능한 표현을 표시.
더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/od-invocation.html>.

- 기본 설정으로 파일 표시: 8진수 형식, 8바이트 단위로 줄바꿈, 8진수 바이트 오프셋, 중복 줄은 `*`로 대체:

`od `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 자세한 모드로 파일 표시, 즉 중복 줄을 `*`로 대체하지 않음:

`od -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 16진수 형식(2바이트 단위)으로 파일 표시, 10진수 형식의 바이트 오프셋:

`od --format=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x</span>` --address-radix=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">d</span>` -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 16진수 형식(1바이트 단위)으로 파일 표시, 4바이트 단위로 줄바꿈:

`od --format=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x1</span>` --width=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 16진수 형식과 문자 표현으로 파일 표시, 바이트 오프셋은 출력하지 않음:

`od --format=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xz</span>` --address-radix=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 500번째 바이트부터 시작하여 파일의 100바이트만 읽기:

`od --read-bytes 100 --skip-bytes=500 -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
