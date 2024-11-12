---
layout: page
title: linux/secon (한국어)
description: "파일, 프로세스 ID, 현재 실행 컨텍스트 또는 컨텍스트 명세의 SELinux 보안 컨텍스트를 확인합니다."
content_hash: dbb7bc2e97599c22bcc076f15bf867eb86ef2a5f
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/linux/secon.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/secon.html
    icon: bi bi-globe
tldri18n_status: 2
---
# secon

파일, 프로세스 ID, 현재 실행 컨텍스트 또는 컨텍스트 명세의 SELinux 보안 컨텍스트를 확인합니다.
같이 보기: `semanage`, `runcon`, `chcon`.
더 많은 정보: <https://manned.org/secon>.

- 현재 실행 컨텍스트의 보안 컨텍스트 확인:

`secon`

- 프로세스의 현재 보안 컨텍스트 확인:

`secon --pid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>

- 모든 중간 심볼릭 링크를 해석하여 파일의 현재 보안 컨텍스트 확인:

`secon --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더</span>

- 심볼릭 링크 자체의 현재 보안 컨텍스트 확인 (즉, 해석하지 않음):

`secon --link `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/심볼릭_링크</span>

- 컨텍스트 명세를 해석하고 설명:

`secon `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">system_u:system_r:container_t:s0:c899,c900</span>
