FROM python:3.10-slim

ENV PIP_NO_CACHE_DIR=1

ENV https_proxy="http://edcguest:edcguest@172.31.100.14:3128/"
ENV HTTPS_PROXY="http://edcguest:edcguest@172.31.100.14:3128/"


WORKDIR /backend/

RUN pip install -U poetry

COPY ./pyproject.toml ./poetry.lock* ./

RUN poetry install --no-root --without dev

RUN mkdir ./prisma/

COPY prisma/schema.prisma  ./prisma/
COPY prisma/prisma_partial_types.py  ./prisma/

RUN poetry run prisma generate

COPY . .

ENTRYPOINT ["./scripts/entrypoint.sh"]