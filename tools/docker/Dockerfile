FROM dalibo/pandocker

# Update & Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends && \
    apt-get install fonts-noto-cjk && \ 
    rm -rf /var/lib/apt/lists/*

# Clean
RUN rm -rf ~/.cache/pip

ADD pandoc_makedocs.sh /pandoc_makedocs.sh
RUN chmod +x /pandoc_makedocs.sh

ADD entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]