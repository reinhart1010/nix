---
layout: page
title: common/cs-launch (English)
description: "Launch an application from the name directly from Maven dependencies without the need of installing it."
content_hash: b34bafc09c31d5a6718798e5af4180fff750c713
last_modified_at: 2024-01-30
tldri18n_status: 2
---
# cs launch

Launch an application from the name directly from Maven dependencies without the need of installing it.
More information: <https://get-coursier.io/docs/cli-launch>.

- Launch a specific application with arguments:

`cs launch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">application_name</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argument1 argument2 ...</span>

- Launch a specific application version with arguments:

`cs launch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">application_name</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">application_version</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argument1 argument2 ...</span>

- Launch a specific version of an application specifying which is the main file:

`cs launch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group_id</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">artifact_id</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">artifact_version</span>` --main-class `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/main_class_file</span>

- Launch an application with specific Java options and JVM memory ones:

`cs launch --java-opt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-Doption_name1:option_value1 -Doption_name2:option_value2 ...</span>` --java-opt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-Xjvm_option1 -Xjvm_option2 ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">application_name</span>
