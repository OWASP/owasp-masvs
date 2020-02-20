FROM dalibo/pandocker

# Update & Install dependencies (fonts-noto-cjk for Chinese-Japanese-Korean fonts = CJK)
RUN apt-get update \
    && apt-get install -y --no-install-recommends fonts-noto-cjk && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf ~/.cache/pip

ADD pandoc_makedocs.sh /
RUN chmod +x /pandoc_makedocs.sh
ENTRYPOINT ["bash", "-euc"]
