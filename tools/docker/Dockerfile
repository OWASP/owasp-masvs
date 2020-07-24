FROM dalibo/pandocker


# Update & Install dependencies (fonts-noto-cjk for Chinese-Japanese-Korean fonts = CJK)
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl xfonts-75dpi xfonts-base fonts-noto-cjk texlive-lang-arabic

RUN apt-get install -y --no-install-recommends build-essential checkinstall libreadline-gplv2-dev libncursesw5-dev libssl-dev \
    libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev

RUN rm -rf /var/lib/apt/lists/* && \
    rm -rf ~/.cache/pip

# Instal Python 3.7.8

RUN apt-get remove --auto-remove -y python3

RUN cd /usr/src && \
    wget -q https://www.python.org/ftp/python/3.7.8/Python-3.7.8.tgz && \
    tar xzf Python-3.7.8.tgz && \
    cd Python-3.7.8 && \
    ./configure --enable-optimizations && \
    make altinstall

RUN rm -f /usr/src/Python-3.7.8.tgz && rm -rf /usr/src/Python-3.7.8

RUN ln -s /usr/local/bin/python3.7 /usr/bin/python3

# Install kindlegen in order to be able to create MOBI files.
RUN curl http://kindlegen.s3.amazonaws.com/kindlegen_linux_2.6_i386_v2_9.tar.gz --output kindlegen_install.tar.gz && \
    tar xvfz kindlegen_install.tar.gz && \
    mv kindlegen /usr/local/bin/ && rm kindlegen_install.tar.gz

# Install new engine for Persian commnications.
RUN  wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.5/wkhtmltox_0.12.5-1.stretch_amd64.deb && \
(dpkg -i wkhtmltox_0.12.5-1.stretch_amd64.deb || apt install -f -y && dpkg -i wkhtmltox_0.12.5-1.stretch_amd64.deb) && \
rm wkhtmltox_0.12.5-1.stretch_amd64.deb

# Should fix arabic, but requires 2019 tex distro, now we use 2016 with dalib/pandocker
# RUN wget http://ftp.br.debian.org/debian/pool/main/t/texlive-lang/texlive-lang-arabic_2019.20200302-1_all.deb && \
# (dpkg -i texlive-lang-arabic_2019.20200302-1_all.deb || apt install -f -y && dpkg -i texlive-lang-arabic_2019.20200302-1_all.deb )&& \
# rm texlive-lang-arabic_2019.20200302-1_all.deb

# Source Sans Pro packaged with distributions does not contain Italic versions of Russian chars
# File downloaded from https://github.com/adobe-fonts/source-sans-pro/releases/tag/3.006R
ADD SourceSansPro-It.otf /usr/local/share/texmf/fonts/opentype/adobe/sourcesanspro/SourceSansPro-RegularIt.otf
RUN fc-cache

ADD pandoc_makedocs.sh /
RUN chmod +x /pandoc_makedocs.sh
ENTRYPOINT ["bash", "-euc"]
