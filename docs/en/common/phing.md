---
layout: page
title: common/phing (English)
description: "A PHP build tool based on Apache Ant."
content_hash: 72c8363270c9a4f4827e70710f49fb9db67aa0c8
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# phing

A PHP build tool based on Apache Ant.
More information: <https://www.phing.info>.

- Perform the default task in the `build.xml` file:

`phing`

- Initialize a new build file:

`phing -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/build.xml</span>

- Perform a specific task:

`phing `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_name</span>

- Specify a custom build file path:

`phing -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/build.xml</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_name</span>

- Specify a log file to output to:

`phing -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/log_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_name</span>

- Specify custom properties to use in the build:

`phing -D`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">property</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_name</span>

- Specify a custom listener class:

`phing -listener `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">class_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_name</span>

- Build using verbose output:

`phing -verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_name</span>
