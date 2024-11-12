---
layout: page
title: linux/setsid (한국어)
description: "호출 프로세스가 프로세스 그룹 리더가 아닌 경우 새 세션에서 프로그램을 실행."
content_hash: 5ff58a5854b5b8ed6c96758b077910b88dd8578b
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/linux/setsid.html
    icon: bi bi-globe
tldri18n_status: 2
---
# setsid

호출 프로세스가 프로세스 그룹 리더가 아닌 경우 새 세션에서 프로그램을 실행.
생성된 세션은 기본적으로 현재 터미널에 의해 제어되지 않음.
더 많은 정보: <https://manned.org/setsid>.

- 새 세션에서 프로그램 실행:

`setsid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로그램</span>

- 결과 출력 및 오류를 무시하며 새 세션에서 프로그램 실행:

`setsid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로그램</span>` > /dev/null 2>&1`

- 새 프로세스를 생성하여 프로그램 실행:

`setsid --fork `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로그램</span>

- 프로그램이 종료될 때 해당 종료 코드를 setsid의 종료 코드로 반환:

`setsid --wait `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로그램</span>

- 현재 터미널을 제어 터미널로 설정하여 새 세션에서 프로그램 실행:

`setsid --ctty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로그램</span>
