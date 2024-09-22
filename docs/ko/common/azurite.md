---
layout: page
title: common/azurite (한국어)
description: "로컬 환경의 Azure Storage API 호환 서버 (에뮬레이터)."
content_hash: d71c1d860118a0dc3842348b9a1350fd4bc461e1
last_modified_at: 2024-09-22
related_topics:
  - title: English version
    url: /en/common/azurite.html
    icon: bi bi-globe
tldri18n_status: 2
---
# azurite

로컬 환경의 Azure Storage API 호환 서버 (에뮬레이터).
더 많은 정보: <https://www.npmjs.com/package/azurite>.

- 기존 위치를 작업공간 경로로 사용:

`azurite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-l|--location</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리</span>

- 콘솔에 표시된 액세스 로그를 비활성화:

`azurite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-s|--silent</span>

- 파일 경로를 로그 대상으로 제공하여, 디버그 로그를 활성화:

`azurite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--debug</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/debug.log</span>

- Blob/Queue/Table 서비스의 수신 주소를 사용자 정의:

`azurite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--blobHost|--queueHost|--tableHost</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.0.0.0</span>

- Blob/Queue/Table 서비스의 수신 포트를 사용자 정의:

`azurite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--blobPort|--queuePort|--tablePort</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8888</span>
