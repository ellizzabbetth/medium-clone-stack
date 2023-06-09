# bring in basre image
FROM nginx:1.23.3-alpine

# remove the default nginx configuration by using the run command.
RUN rm /etc/nginx/conf.d/default.conf

# copying our default conf to /etc/nginx/conf.d/default.conf 
COPY ./default.conf /etc/nginx/conf.d/default.conf