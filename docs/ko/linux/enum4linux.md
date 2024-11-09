---
layout: page
title: linux/enum4linux (한국어)
description: "원격 시스템에서 Windows 및 Samba 정보를 열거합니다."
content_hash: 2f5f3fbdebcd89b2908cff570e20575305c84c25
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/enum4linux.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/enum4linux.html
    icon: bi bi-globe
tldri18n_status: 2
---
# enum4linux

원격 시스템에서 Windows 및 Samba 정보를 열거합니다.
더 많은 정보: <https://labs.portcullis.co.uk/tools/enum4linux/>.

- 모든 방법을 사용하여 열거 시도:

`enum4linux -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_호스트</span>

- 주어진 로그인 자격 증명을 사용하여 열거:

`enum4linux -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_이름</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_호스트</span>

- 특정 호스트에서 사용자명 나열:

`enum4linux -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_호스트</span>

- 공유 목록 나열:

`enum4linux -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_호스트</span>

- 운영 체제 정보 가져오기:

`enum4linux -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_호스트</span>
