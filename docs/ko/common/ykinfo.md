---
layout: page
title: common/ykinfo (한국어)
description: "YubiKey에서 기본 정보를 가져옵니다."
content_hash: a0e4a81938dee09016bcb0adac525e9d8ce013df
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/ykinfo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ykinfo

YubiKey에서 기본 정보를 가져옵니다.
더 많은 정보: <https://developers.yubico.com/yubikey-personalization/Manuals/ykinfo.1.html>.

- YubiKey의 모든 정보 표시:

`ykinfo -a`

- YubiKey에서 10진수로 된 일련 번호만 가져오기:

`ykinfo -s -q`

- YubiKey에서 기능 가져오기:

`ykinfo -c`
