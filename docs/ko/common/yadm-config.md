---
layout: page
title: common/yadm-config (한국어)
description: "`yadm`의 구성 파일에 옵션을 전달하여 `yadm`이 관리하는 저장소의 `.config`를 변경합니다."
content_hash: 1e2d20b84002461d4169edd9d43e5a162354e065
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/yadm-config.html
    icon: bi bi-globe
tldri18n_status: 2
---
# yadm-config

`yadm`의 구성 파일에 옵션을 전달하여 `yadm`이 관리하는 저장소의 `.config`를 변경합니다.
더 많은 정보: <https://github.com/TheLocehiliosan/yadm/blob/master/yadm.md#configuration>.

- `yadm`의 Git 구성 설정 또는 업데이트:

`yadm config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키.내부_키</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>

- `yadm`의 Git 구성에서 값 가져오기:

`yadm config --get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키</span>

- `yadm`의 Git 구성에서 값 제거:

`yadm config --unset `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키</span>

- `yadm`의 Git 구성에 있는 모든 값 나열:

`yadm config --list`
