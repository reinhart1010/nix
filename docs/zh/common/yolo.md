---
layout: page
title: common/yolo (中文)
description: "YOLO 命令行界面让你可以简单地在不同的任务和版本上进行模型的训练、验证或推理。"
content_hash: c4bf0340cfe8266d7e13a28286e7cb0261df157b
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/yolo.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/yolo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# yolo

YOLO 命令行界面让你可以简单地在不同的任务和版本上进行模型的训练、验证或推理。
更多信息：<https://docs.ultralytics.com/cli/>.

- 在当前工作目录中创建默认配置的副本：

`yolo task=init`

- 使用指定的配置文件训练目标检测、实例分割或分类模型：

`yolo task=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">detect|segment|classify</span>` mode=train cfg=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/config.yaml</span>
