---
layout: page
title: common/verilator (한국어)
description: "Verilog 및 SystemVerilog 하드웨어 설명 언어(HDL) 디자인을 C++ 또는 SystemC 모델로 변환하여 컴파일 후 실행."
content_hash: b74309b78fe3b244994effa21450e0d632e6e2e8
last_modified_at: 2024-11-04
related_topics:
  - title: English version
    url: /en/common/verilator.html
    icon: bi bi-globe
tldri18n_status: 2
---
# verilator

Verilog 및 SystemVerilog 하드웨어 설명 언어(HDL) 디자인을 C++ 또는 SystemC 모델로 변환하여 컴파일 후 실행.
더 많은 정보: <https://veripool.org/guide/latest/>.

- 현재 디렉토리에서 특정 C 프로젝트 빌드:

`verilator --binary --build-jobs 0 -Wall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스.v</span>

- 특정 폴더에 C++ 실행 파일 생성:

`verilator --cc --exe --build --build-jobs 0 -Wall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스.cpp</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.v</span>

- 현재 디렉토리의 코드에 대해 린팅 수행:

`verilator --lint-only -Wall`

- 디자인에 대한 XML 출력 생성(파일, 모듈, 인스턴스 계층 구조, 논리 및 데이터 유형)하여 다른 도구에 입력:

`verilator --xml-output -Wall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.xml</span>
