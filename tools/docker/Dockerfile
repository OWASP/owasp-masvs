FROM dalibo/pandocker

# Update & Install dependencies (fonts-noto-cjk for Chinese-Japanese-Korean fonts = CJK)
RUN apt-get update \
    && apt-get install -y --no-install-recommends fonts-noto-cjk && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf ~/.cache/pip

# Source Sans Pro packaged with distributions does not contain Italic versions of Russian chars
# File downloaded from https://github.com/adobe-fonts/source-sans-pro/releases/tag/3.006R
ADD SourceSansPro-It.otf /usr/local/share/texmf/fonts/opentype/adobe/sourcesanspro/SourceSansPro-RegularIt.otf
RUN fc-cache

ADD pandoc_makedocs.sh /
RUN chmod +x /pandoc_makedocs.sh
ENTRYPOINT ["bash", "-euc"]
