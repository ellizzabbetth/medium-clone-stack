FROM postgres:15-bullseye

# So here we're basically copying the maintenance folder and the scripts from our local directory to our
# container.
COPY ./docker/local/postgres/maintenance /usr/local/bin/maintenance

# making the maintenance scripts executable in the container.
RUN chmod +x /usr/local/bin/maintenance/*

# 
RUN mv /usr/local/bin/maintenance/* /usr/local/bin \
  && rmdir /usr/local/bin/maintenance