---
layout: page
title: common/swagger-codegen (English)
description: "Generate code and documentation for your REST api from a OpenAPI/swagger definition."
content_hash: 2a2eaf18c7b73b13d1f19aebab66c6ed1b77f716
last_modified_at: 2023-11-12
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

- Display help options for the generate command:

`swagger-codegen help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">generate</span>
