FROM asciidoctor/docker-asciidoctor

RUN curl -L https://github.com/jgm/pandoc/releases/download/2.9/pandoc-2.9-linux-amd64.tar.gz --output /root/pandoc-2.9-linux-amd64.tar.gz
RUN tar xvzf /root/pandoc-2.9-linux-amd64.tar.gz --strip-components 1 -C /usr/local

ADD entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

#RUN asciidoctor --backend html5 -a data-uri ${INPUT_ADOC}
#RUN asciidoctor --backend docbook --out-file - $INPUT_ADOC | pandoc --from docbook --to docx --output out.docx