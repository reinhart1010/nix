---
layout: page
title: linux/blastn (한국어)
description: "뉴클레오타이드-뉴클레오타이드 BLAST."
content_hash: b411f263bda60815ea5204eb2fae6a067ded2556
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/blastn.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/blastn.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># blastn

뉴클레오타이드-뉴클레오타이드 BLAST.
더 많은 정보: <https://www.ncbi.nlm.nih.gov/books/NBK279684/table/appendices.T.blastn_application_options/>.

- 메가블라스트(기본값)를 사용하여 두 개 이상의 서열 정렬, e-value 임계값 1e-9, 쌍별 출력 형식(기본값):

`blastn -query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">query.fa</span>` -subject `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subject.fa</span>` -evalue `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1e-9</span>

- blastn을 사용하여 두 개 이상의 서열 정렬:

`blastn -task blastn -query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">query.fa</span>` -subject `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subject.fa</span>

- 사용자 정의 표형식 출력, 파일로 출력:

`blastn -query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">query.fa</span>` -subject `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subject.fa</span>` -outfmt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'6 qseqid qlen qstart qend sseqid slen sstart send bitscore evalue pident'</span>` -out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.tsv</span>

- 뉴클레오타이드 쿼리를 사용하여 뉴클레오타이드 데이터베이스 검색, BLAST 검색에 사용할 스레드(CPU) 16개, 최대 10개의 정렬된 서열 유지:

`blastn -query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">query.fa</span>` -db `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/blast_db</span>` -num_threads `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">16</span>` -max_target_seqs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- 원격 비중복 뉴클레오타이드 데이터베이스를 뉴클레오타이드 쿼리로 검색:

`blastn -query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">query.fa</span>` -db `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nt</span>` -remote`

- 도움말 표시 (`-help`로 자세한 도움말 사용):

`blastn -h`
