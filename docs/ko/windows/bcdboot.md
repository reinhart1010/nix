---
layout: page
title: windows/bcdboot (한국어)
description: "부트 파일을 구성하거나 복구."
content_hash: 6fb2f809ff9861a3c788600775bc923084778fcb
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/windows/bcdboot.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/bcdboot.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bcdboot

부트 파일을 구성하거나 복구.
더 많은 정보: <https://learn.microsoft.com/windows-hardware/manufacture/desktop/bcdboot-command-line-options-techref-di>.

- 소스 Windows 폴더의 BCD 파일을 사용하여 시스템 파티션 초기화:

`bcdboot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C:\Windows</span>

- [v]erbose 모드 활성화:

`bcdboot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C:\Windows</span>` /v`

- 시스템 파티션의 볼륨 문자 지정:

`bcdboot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C:\Windows</span>` /s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">S:</span>

- [l]ocale 지정:

`bcdboot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C:\Windows</span>` /l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">en-us</span>

- 지정된 볼륨으로 부트 파일을 복사할 때 [f]irmware 유형 지정:

`bcdboot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C:\Windows</span>` /s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">S:</span>` /f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">UEFI|BIOS|ALL</span>
