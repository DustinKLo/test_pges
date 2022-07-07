FROM hysds/pge-base:develop

# provision
USER ops
COPY . /home/ops/verdi/ops/test_pges

# set entrypoint
ENTRYPOINT ["/entrypoint-pge-with-stats.sh"]

WORKDIR /home/ops
CMD ["/bin/bash", "--login"]
