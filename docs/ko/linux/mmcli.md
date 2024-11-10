---
layout: page
title: linux/mmcli (한국어)
description: "ModemManager를 제어하고 모니터링."
content_hash: a75b2b99d94bf0010b1010dc7b581ee259c8fd0d
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/mmcli.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mmcli

ModemManager를 제어하고 모니터링.
더 많은 정보: <https://www.freedesktop.org/software/ModemManager/man/latest/mmcli.1.html>.

- 사용 가능한 모뎀 나열:

`mmcli --list-modems`

- 모뎀에 대한 정보 출력:

`mmcli --modem=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모뎀</span>

- 모뎀 활성화:

`mmcli --modem=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모뎀</span>` --enable`

- 모뎀에서 사용 가능한 SMS 메시지 나열:

`sudo mmcli --modem=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모뎀</span>` --messaging-list-sms`

- 모뎀에서 메시지를 삭제, 경로 지정:

`sudo mmcli --modem=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모뎀</span>` --messaging-delete-sms=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/메시지_파일</span>
