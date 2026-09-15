FROM maven:3-eclipse-temurin-21 AS build

ARG SPRING_BOOT_METADATA_URL=https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/maven-metadata.xml
WORKDIR /build

RUN apt-get update \
    && apt-get install -y --no-install-recommends ca-certificates curl \
    && rm -rf /var/lib/apt/lists/*

COPY pom.xml .
COPY src ./src

RUN set -eux; \
    spring_boot_version="$(curl -fsSL "$SPRING_BOOT_METADATA_URL" \
      | sed -n 's:.*<version>\([^<]*\)</version>.*:\1:p' \
      | grep -E '^[0-9]+\.[0-9]+\.[0-9]+$' \
      | sort -V \
      | tail -n 1)"; \
    test -n "$spring_boot_version"; \
    printf '%s\n' "$spring_boot_version" > /tmp/spring-boot-version; \
    mvn -B -Dspring-boot.version="$spring_boot_version" package; \
    cp target/springboot-target-1.0.0.jar /tmp/application.jar

FROM eclipse-temurin:21-jre

WORKDIR /app
COPY --from=build /tmp/application.jar ./application.jar
COPY --from=build /tmp/spring-boot-version ./spring-boot-version
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "/app/application.jar"]
