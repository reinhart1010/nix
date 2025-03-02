---
layout: page
title: common/seq (中文)
description: "打印数字序列到标准输出。"
content_hash: 00db79be552fcbb8ef83e7dc9531e73bd5548c38
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/seq.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/seq.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/seq.html
    icon: bi bi-globe
tldri18n_status: 2
---
# seq

打印数字序列到标准输出。
更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/seq-invocation.html>.

- 从 1 到 10 的序列：

`seq 10`

- 从 5 开始，3 为步长，不超过 20 的序列：

`seq 5 3 20`

- 从 5 开始，3 为步长，不超过 20 的序列，并用空格作为分隔符：

`seq -s " " 5 3 20`

- 从 5 开始，3 为步长，不超过 20 的序列，并格式化为 4 位宽度，不足 4 位，前面补 0：

`seq -f "%04g" 5 3 20`
