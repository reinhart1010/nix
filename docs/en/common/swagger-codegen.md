---
layout: page
title: common/swagger-codegen (English)
description: "Generate code and documentation for your REST api from a OpenAPI/swagger definition."
content_hash: 4003849cbce443ecb8faaff390ca57412b63c97b
last_modified_at: 2024-01-30
tldri18n_status: 2
---
# swagger-codegen

Generate code and documentation for your REST api from a OpenAPI/swagger definition.
More information: <https://github.com/swagger-api/swagger-codegen>.

- Generate documentation and code from an OpenAPI/swagger file:

`swagger-codegen generate -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">swagger_file</span>` -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">language</span>

- Generate Java code using the library retrofit2 and the option useRxJava2:

`swagger-codegen generate -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://petstore.swagger.io/v2/swagger.json</span>` -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">java</span>` --library `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">retrofit2</span>` -D`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">useRxJava2</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>

- List available languages:

`swagger-codegen langs`

- Display help for a specific command:

`swagger-codegen `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">generate|config-help|meta|langs|version</span>` --help`
