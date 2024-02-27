FROM busybox:latest

RUN echo "Hello World" > /hello.txt

RUN echo "Goodbye" > /bye.txt

COPY ./greet.sh /app/greet.sh

# Executes /app/greet.sh "New Person"
ENTRYPOINT ["/bin/sh", "/app/greet.sh"]
CMD ["New Person"]
