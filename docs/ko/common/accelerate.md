---
layout: page
title: common/accelerate (한국어)
description: "Accelerate는 동일한 PyTorch 코드를 모든 분산 환경 구성에서 실행할 수 있게 해주는 라이브러리입니다."
content_hash: 929d94884f091fb3a225eae8ac7bed02274745aa
last_modified_at: 2023-12-03
related_topics:
  - title: English version
    url: /en/common/accelerate.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/accelerate.html
    icon: bi bi-globe
tldri18n_status: 2
---
# Accelerate

Accelerate는 동일한 PyTorch 코드를 모든 분산 환경 구성에서 실행할 수 있게 해주는 라이브러리입니다.
더 많은 정보: <https://huggingface.co/docs/accelerate/index>.

- 실행환경 정보 출력:

`accelerate env`

- 대화형으로 구성 파일 생성:

`accelerate config`

- 다양한 데이터 타입을 사용하여 Hugging Face 모델을 실행하는 데 필요한 예상 GPU 메모리 비용을 출력:

`accelerate estimate-memory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름/모델</span>

- Accelerate 구성 파일 테스트:

`accelerate test --config_file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/구성파일.yaml</span>

- Accelerate를 사용하여 CPU에서 모델을 실행:

`accelerate launch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스크립트.py</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--cpu</span>

- 2대의 머신을 사용하고, Accelerate로 다중 GPU에서 모델을 실행:

`accelerate launch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스크립트.py</span>` --multi_gpu --num_machines `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>
