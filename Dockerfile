#FROM pandoc/latex
FROM dalibo/pandocker
# Update & Install dependencies
# RUN apt-get update && \
#     apt-get upgrade -y && \
#     apt-get clean && \
#     rm -rf /var/lib/apt/lists

# Clean
# RUN rm -rf ~/.cache/pip
ADD pandoc_makedocs.sh /pandoc/pandoc_makedocs.sh
RUN chmod +x /pandoc/pandoc_makedocs.sh

ADD entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]