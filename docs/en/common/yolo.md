---
layout: page
title: common/yolo (English)
description: "The YOLO command line interface lets you simply train, validate or infer models on various tasks and versions."
content_hash: c3482420feaedc386c4758da80a563d42a4a070c
last_modified_at: 2023-01-16
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># yolo

The YOLO command line interface lets you simply train, validate or infer models on various tasks and versions.
More information: <https://docs.ultralytics.com/cli/>.

- Create a copy of the default configuration in your current working directory:

`yolo task=init`

- Train the object detection, instance segment, or classification model with the specified configuration file:

`yolo task=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">detect|segment|classify</span>` mode=train cfg=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/config.yaml</span>
