---
layout: page
title: linux/systemd-cryptenroll (한국어)
description: "LUKS2로 암호화된 장치를 잠금 해제하는 데 사용되는 방법을 대화식으로 등록하거나 제거합니다. 별도로 지정하지 않으면 암호를 사용하여 장치를 잠금 해제합니다."
content_hash: e6565ff8b0798c485c63345c9b1512fd6ee12c20
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/linux/systemd-cryptenroll.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/systemd-cryptenroll.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># systemd-cryptenroll

LUKS2로 암호화된 장치를 잠금 해제하는 데 사용되는 방법을 대화식으로 등록하거나 제거합니다. 별도로 지정하지 않으면 암호를 사용하여 장치를 잠금 해제합니다.
시스템 부팅 시 파티션을 잠금 해제하려면 `/etc/crypttab` 파일이나 initramfs를 업데이트해야 합니다.
더 많은 정보: <https://www.freedesktop.org/software/systemd/man/systemd-cryptenroll.html>.

- 새 비밀번호 등록 (`cryptsetup luksAddKey`와 유사):

`systemd-cryptenroll --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/luks2_블록_장치</span>

- 새 복구 키 등록 (즉, 대체로 사용할 수 있는 무작위 생성 암호):

`systemd-cryptenroll --recovery-key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/luks2_블록_장치</span>

- 사용 가능한 토큰 목록 나열 또는 새 PKCS#11 토큰 등록:

`systemd-cryptenroll --pkcs11-token-uri `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">list|auto|pkcs11_토큰_uri</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/luks2_블록_장치</span>

- 사용 가능한 FIDO2 장치 목록 나열 또는 새 FIDO2 장치 등록 (`auto`는 토큰이 하나만 연결되어 있을 때 장치 이름으로 사용 가능):

`systemd-cryptenroll --fido2-device `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">list|auto|경로/대상/fido2_hidraw_장치</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/luks2_블록_장치</span>

- 사용자 인증(생체 인식)과 함께 새 FIDO2 장치 등록:

`systemd-cryptenroll --fido2-device `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">auto|경로/대상/fido2_hidraw_장치</span>` --fido2-with-user-verification yes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/luks2_블록_장치</span>

- FIDO2 장치를 사용하여 잠금 해제하고 새 FIDO2 장치 등록:

`systemd-cryptenroll --unlock-fido2-device `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/fido2_hidraw_잠금_해제_장치</span>` --fido2-device `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/fido2_hidraw_등록_장치</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/luks2_블록_장치</span>

- TPM2 보안 칩 등록 (보안 부팅 정책 PCR만) 및 추가적인 영문자 PIN 필요:

`systemd-cryptenroll --tpm2-device `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">auto|경로/대상/tpm2_블록_장치</span>` --tpm2-with-pin yes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/luks2_블록_장치</span>

- 모든 빈 비밀번호/모든 비밀번호/모든 FIDO2 장치/모든 PKCS#11 토큰/모든 TPM2 보안 칩/모든 복구 키/모든 방법 제거:

`systemd-cryptenroll --wipe-slot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">empty|password|fido2|pkcs#11|tpm2|recovery|all</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/luks2_블록_장치</span>
