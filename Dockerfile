FROM dalibo/pandocker

ADD pandoc_makedocs.sh /pandoc/pandoc_makedocs.sh
RUN chmod +x /pandoc/pandoc_makedocs.sh

ADD entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]