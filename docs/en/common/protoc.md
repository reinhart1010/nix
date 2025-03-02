---
layout: page
title: common/protoc (English)
description: "Parse Google Protobuf `.proto` files and generate output in the specified language."
content_hash: 5fe1b0024147838bea46668b87ae43586015f78c
last_modified_at: 2025-03-02
related_topics:
  - title: 한국어 version
    url: /ko/common/protoc.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/protoc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# protoc

Parse Google Protobuf `.proto` files and generate output in the specified language.
More information: <https://developers.google.com/protocol-buffers>.

- Generate Python code from a `.proto` file:

`protoc --python_out=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_file.proto</span>

- Generate Java code from a `.proto` file that imports other `.proto` files:

`protoc --java_out=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_directory</span>` --proto_path=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/import_search_path</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_file.proto</span>

- Generate code for multiple languages:

`protoc --csharp_out=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/c#_output_directory</span>` --js_out=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/js_output_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_file.proto</span>

- Encode a text-format message into a protocol message from a `.proto` file:

`protoc --encode=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">TypeName</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_file.proto</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message.txt</span>

- Decode a protocol message into text-format from a `.proto` file:

`protoc --decode=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">TypeName</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_file.proto</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message.bin</span>

- Decode a protocol message into raw tag/value pairs:

`protoc --decode_raw < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message.bin</span>
