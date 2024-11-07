---
layout: page
title: common/pass-otp (한국어)
description: "일회용 비밀번호(OTP) 토큰 관리를 위한 pass 확장 기능."
content_hash: c844bdb6ae5716fc4440f89e599e09b3e80b7741
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/pass-otp.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pass-otp.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pass otp

일회용 비밀번호(OTP) 토큰 관리를 위한 pass 확장 기능.
더 많은 정보: <https://github.com/tadfisher/pass-otp#readme>.

- otpauth URI 토큰을 입력 받고 새로운 pass 파일 생성:

`pass otp insert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/pass</span>

- otpauth URI 토큰을 입력 받고 기존 pass 파일에 추가:

`pass otp append `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/pass</span>

- pass 파일의 OTP 토큰을 사용하여 2FA 코드 출력:

`pass otp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/pass</span>

- pass 파일의 OTP 토큰을 사용하여 2FA 코드를 복사하고 출력하지 않음:

`pass otp --clip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/pass</span>

- pass 파일에 저장된 OTP 토큰을 사용하여 QR 코드 표시:

`pass otp uri --qrcode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/pass</span>

- 발행자 및 계정을 지정하여 OTP 비밀 값을 입력 받고 기존 pass 파일에 추가 (적어도 하나는 지정해야 함):

`pass otp append --secret --issuer `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">발행자_이름</span>` --account `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">계정_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/pass</span>
