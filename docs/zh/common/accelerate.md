---
layout: page
title: common/accelerate (中文)
description: "一个使得可以在任何分布式配置中运行相同的 PyTorch 代码的库。"
content_hash: 95439aabd005ceb858fe12f59b53b76b984022a8
last_modified_at: 2024-06-24
related_topics:
  - title: English version
    url: /en/common/accelerate.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/accelerate.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/accelerate.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/accelerate.html
    icon: bi bi-globe
tldri18n_status: 2
---
# Accelerate

一个使得可以在任何分布式配置中运行相同的 PyTorch 代码的库。
更多信息： <https://huggingface.co/docs/accelerate/index>.

- 打印环境信息：

`accelerate env`

- 交互式地创建配置文件：

`accelerate config`

- 打印使用不同数据类型运行 Hugging Face 模型的估计 GPU 内存成本：

`accelerate estimate-memory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">名字/模型</span>

- 测试一个 Accelerate 配置文件：

`accelerate test --config_file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/配置文件.yaml</span>

- 使用 Accelerate 在 CPU 上运行一个模型：

`accelerate launch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/脚本.py</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--cpu</span>

- 使用 Accelerate 在多 GPU 上运行一个模型，使用 2 台机器：

`accelerate launch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/脚本.py</span>` --multi_gpu --num_machines 2`
