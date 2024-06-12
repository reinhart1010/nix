---
layout: page
title: common/azurite (English)
description: "Azure Storage API compatible server (emulator) in local environment."
content_hash: aeddaf713d9cde14228eb43671428ff361d37cdf
last_modified_at: 2024-06-12
tldri18n_status: 2
---
# azurite

Azure Storage API compatible server (emulator) in local environment.
More information: <https://www.npmjs.com/package/azurite>.

- Use an existing location as workspace path:

`azurite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-l|--location</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Disable access log displayed in console:

`azurite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-s|--silent</span>

- Enable debug log by providing a file path as log destination:

`azurite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--debug</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/debug.log</span>

- Customize the listening address of Blob/Queue/Table service:

`azurite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--blobHost|--queueHost|--tableHost</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.0.0.0</span>

- Customize the listening port of Blob/Queue/Table service:

`azurite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--blobPort|--queuePort|--tablePort</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8888</span>
