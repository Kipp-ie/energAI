ARG BUILD_FROM
FROM $BUILD_FROM

# Install requirements for add-on
RUN \
  apk add --no-cache \
    python3

# Copy data for add-on
COPY run.sh /
COPY server.py /
COPY index.html /
COPY logo.png /
RUN chmod a+x /run.sh
RUN chmod a+x /index.html
RUN chmod a+x /server.py
RUN chmod a+x /logo.png

CMD [ "/run.sh" ]