---
layout: page
title: common/logstash (English)
description: "An Elasticsearch ETL (extract, transform and load) tool."
content_hash: 411cea8cef5e3246ae4f84f4ac50110ad474ae61
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# logstash

An Elasticsearch ETL (extract, transform and load) tool.
Commonly used to load data from various sources (such as databases and log files) into Elasticsearch.
More information: <https://www.elastic.co/products/logstash>.

- Check validity of a Logstash configuration:

`logstash --configtest --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">logstash_config.conf</span>

- Run Logstash using configuration:

`sudo logstash --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">logstash_config.conf</span>

- Run Logstash with the most basic inline configuration string:

`sudo logstash -e 'input {} filter {} output {}'`
