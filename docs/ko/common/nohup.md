---
layout: page
title: common/nohup (한국어)
description: "터미널이 종료되어도 프로세스가 계속 실행되도록 허용."
content_hash: 440daaed2481b08c66ca3d2c0b004d19946ad5b7
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/nohup.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/nohup.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/nohup.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/nohup.html
    icon: bi bi-globe
  - title: svenska version
    url: /sv/common/nohup.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/nohup.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nohup

터미널이 종료되어도 프로세스가 계속 실행되도록 허용.
더 많은 정보: <https://www.gnu.org/software/coreutils/nohup>.

- 터미널 종료 후에도 계속 실행되는 프로세스 시작:

`nohup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인수1 인수2 ...</span>

- 백그라운드 모드에서 `nohup` 실행:

`nohup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인수1 인수2 ...</span>` &`

- 터미널 종료 후에도 계속 실행되는 셸 스크립트 실행:

`nohup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스크립트.sh</span>` &`

- 프로세스를 실행하고 출력을 특정 파일에 기록:

`nohup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인수1 인수2 ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일</span>` &`
