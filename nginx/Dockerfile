#use the Nginx image
FROM nginx

#remove the default nginx.conf
RUN rm /etc/nginx/conf.d/default.conf

#replace with our own nginx.conf
COPY nginx.conf /etc/nginx/conf.d/
