---
layout: page
title: common/yolo (English)
description: "The YOLO command-line interface lets you simply train, validate or infer models on various tasks and versions."
content_hash: 1c4ec358e34157d8dd9427e9c703856ce1a094cd
last_modified_at: 2023-05-31
---
# yolo

The YOLO command-line interface lets you simply train, validate or infer models on various tasks and versions.
More information: <https://docs.ultralytics.com/cli/>.

- Create a copy of the default configuration in your current working directory:

`yolo task=init`

- Train the object detection, instance segment, or classification model with the specified configuration file:

`yolo task=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">detect|segment|classify</span>` mode=train cfg=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/config.yaml</span>
