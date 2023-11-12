---
layout: page
title: linux/postconf (English)
description: "Postfix configuration utility."
content_hash: cdd0991d85db613489849e34f1ed19674f20d5fb
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# postconf

Postfix configuration utility.
This command displays the values of the `main.cf` configuration parameters by default and warns about possible mistyped parameter names. It can also change the `main.cf` configuration parameter values.
More information: <https://manned.org/postconf>.

- Specify the directory of the `main.cf` configuration file instead of the default configuration directory:

`postconf -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/configuration_directory</span>

- Edit the `main.cf` configuration file and update parameter settings with the "name=value" pairs:

`postconf -e`

- Print the default parameter settings of the `main.cf` instead of the actual settings:

`postconf -d`

- Display parameters only from the specified class. The class can be one of builtin, service, user or all:

`postconf -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">class</span>

- List available SASL plug-in types for the Postfix SMTP server. The plug-in type is selected with the `smtpd_sasl_type` configuration parameter by specifying `cyrus` or `dovecot` as the name:

`postconf -a`

- List the names of all supported lookup table types. Lookup tables are specified as `type:name` in configuration files where the type can be `btree`, `cdb`, `hash`, `mysql`, etc:

`postconf -m`
