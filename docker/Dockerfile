FROM python:3.6.6-alpine

COPY . /app

WORKDIR /app

RUN apk add --no-cache \
    gcc \
    g++ \
    libstdc++ \
    linux-headers \
    && \
    pip install dist/* \
    && \
    rm -rf ~/.cache/pip && \
    rm -rf /app \
    && \
    apk del --no-cache \
    gcc \
    g++ \
    linux-headers

ENTRYPOINT ["trasherbot"]
