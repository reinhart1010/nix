---
layout: page
title: linux/zipsplit (한국어)
description: "Zip 아카이브를 더 작은 Zip 아카이브로 분할."
content_hash: 19c62924324d20cf3545ee398c05254cbe71ec32
last_modified_at: 2024-10-29
related_topics:
  - title: English version
    url: /en/linux/zipsplit.html
    icon: bi bi-globe
tldri18n_status: 2
---
# zipsplit

Zip 아카이브를 더 작은 Zip 아카이브로 분할.
더 많은 정보: <https://manned.org/zipsplit>.

- Zip 아카이브를 36000 바이트(36 MB) 이하의 부분으로 분할:

`zipsplit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/아카이브.zip</span>

- 지정된 바이트 [n] 수를 부분 제한으로 사용:

`zipsplit -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">크기</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/아카이브.zip</span>

- 각 부분 생성 사이에 [p] 일시 정지:

`zipsplit -p -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">크기</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/아카이브.zip</span>

- 분할된 작은 Zip 아카이브를 지정된 디렉토리에 출력:

`zipsplit -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_폴더</span>` -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">크기</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/아카이브.zip</span>
