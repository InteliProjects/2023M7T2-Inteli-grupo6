# Use a imagem base do Python
FROM public.ecr.aws/lambda/python:3.10

RUN yum -y install tar gzip zlib freetype-devel gcc && yum clean all

COPY requirements.txt ${LAMBDA_TASK_ROOT}

RUN python3 -m pip install --upgrade pip setuptools wheel bottleneck

RUN pip install --no-binary lightgbm --install-option='--nomp' 'lightgbm==3.3.2'

RUN python3 -m pip install --trusted-host pypi.python.org -r requirements.txt

COPY . ${LAMBDA_TASK_ROOT}

CMD ["main.handler"]
