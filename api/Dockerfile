FROM trestletech/plumber

RUN R -e "install.packages('glmnet')"
RUN R -e "install.packages('jsonlite')"

WORKDIR /opt/api

COPY ./api.R .

CMD ["/opt/api/api.R"]