---
layout: page
title: windows/repair-bde (한국어)
description: "손상된 BitLocker 암호화 볼륨을 복구하거나 해독하려고 시도합니다."
content_hash: 23979b91e2edc3c3da28b4bcfa5e5ed669a0a2d5
last_modified_at: 2024-10-26
related_topics:
  - title: English version
    url: /en/windows/repair-bde.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/repair-bde.html
    icon: bi bi-globe
tldri18n_status: 2
---
# repair-bde

손상된 BitLocker 암호화 볼륨을 복구하거나 해독하려고 시도합니다.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/repair-bde>.

- 지정된 볼륨을 복구하려고 시도:

`repair-bde `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C:</span>

- 지정된 볼륨을 복구하려고 시도하고 다른 볼륨에 출력:

`repair-bde `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C:</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">D:</span>

- 제공된 복구 키 파일 사용하여 지정된 볼륨을 복구하려고 시도:

`repair-bde `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C:</span>` -RecoveryKey `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일.bek</span>

- 제공된 숫자 복구 암호 사용하여 지정된 볼륨을 복구하려고 시도:

`repair-bde `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C:</span>` -RecoveryPassword `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">암호</span>

- 제공된 암호 사용하여 지정된 볼륨을 복구하려고 시도:

`repair-bde `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C:</span>` -Password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">암호</span>

- 제공된 키 패키지 사용하여 지정된 볼륨을 복구하려고 시도:

`repair-bde `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C:</span>` -KeyPackage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\디렉토리</span>

- 모든 출력을 특정 파일에 기록:

`repair-bde `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C:</span>` -LogFile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일</span>

- 도움말 표시:

`repair-bde /?`
