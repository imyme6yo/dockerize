# Dockerfile for nativescript project
# AUTHOR: jon "imyme6yo@gmail.com"
# CREATE DATE: 20190117
# UPDATE DATE: 20190117

# ARGUEMNTS FOR CONTAINER
ARG VERSION=5.1
ARG TAG=${VERSION}-node11`0.6-stretch

FROM imyme6yo/nativescript:${TAG}

# MAINTAINER
LABEL maintainer "imyme6yo@gmail.com"

# ARGUMENTS FOR PROJECT
ARG DIR_NAME=code
ARG PROJECT_NAME=project

# COPY PROJECT FILES
RUN mkdir ${DIR_NAME}
ADD . ${DIR_NAME}
WORKDIR ${DIR_NAME}/${PROJECT_NAME}
RUN npm install