---
layout: page
title: common/mosquitto_passwd (한국어)
description: "mosquitto의 비밀번호 파일을 관리."
content_hash: 61a7ce00e6e2ef5c853195396ff7af7679f8a4a9
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/mosquitto_passwd.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/mosquitto_passwd.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mosquitto_passwd

mosquitto의 비밀번호 파일을 관리.
관리하는 MQTT 서버인 `mosquitto`도 참고하세요.
더 많은 정보: <https://mosquitto.org/man/mosquitto_passwd-1.html>.

- 비밀번호 파일에 새 사용자 추가 (비밀번호 입력을 요청함):

`mosquitto_passwd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/비밀번호_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>

- 비밀번호 파일이 없을 경우 생성:

`mosquitto_passwd -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/비밀번호_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>

- 지정된 사용자명을 삭제:

`mosquitto_passwd -D `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/비밀번호_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>

- 기존의 평문 비밀번호 파일을 해시된 비밀번호 파일로 업그레이드:

`mosquitto_passwd -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/비밀번호_파일</span>
