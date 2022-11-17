---
layout: page
title: common/snowsql (English)
description: "SnowSQL command-line client for Snowflake's Data Cloud."
content_hash: 85d976296d5b5726e9b21771cb2adbdebe8dbd38
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># snowsql

SnowSQL command-line client for Snowflake's Data Cloud.
More information: <https://docs.snowflake.com/en/user-guide/snowsql.html>.

- Connect to a specific instance at <https://account.snowflakecomputing.com> (password can be provided in prompt or configuration file):

`snowsql --accountname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">account</span>` --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` --dbname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database</span>` --schemaname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">schema</span>

- Connect to an instance specified by a specific configuration file (defaults to `~/.snowsql/config`):

`snowsql --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/configuration_file</span>

- Connect to the default instance using a token for multi-factor authentication:

`snowsql --mfa-passcode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">token</span>

- Execute a single SQL query or SnowSQL command on the default connection (useful in shell scripts):

`snowsql --query '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">query</span>`'`

- Execute commands from a specific file on the default connection:

`snowsql --filename `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.sql</span>
