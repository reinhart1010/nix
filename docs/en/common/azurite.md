---
layout: page
title: common/azurite (English)
description: "Azure Storage API compatible server (emulator) in local environment."
content_hash: 03a8408c9dffb54b963a29831a08165d54f0f7a7
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># azurite

Azure Storage API compatible server (emulator) in local environment.
More information: <https://www.npmjs.com/package/azurite>.

- Use an existing [l]ocation as workspace path:

`azurite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-l|--location</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Disable access log displayed in console:

`azurite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-s|--silent</span>

- Enable [d]ebug log by providing a file path as log destination:

`azurite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--debug</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/debug.log</span>

- Customize the listening address of Blob/Queue/Table service:

`azurite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--blobHost|--queueHost|--tableHost</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.0.0.0</span>

- Customize the listening port of Blob/Queue/Table service:

`azurite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--blobPort|--queuePort|--tablePort</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8888</span>
