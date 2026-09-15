package cloud.zeroday.target;

import java.util.Map;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.SpringBootVersion;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;


@SpringBootApplication
@RestController
public class TargetApplication {
    public static void main(String[] args) {
        SpringApplication.run(TargetApplication.class, args);
    }

    @GetMapping("/")
    public Map<String, String> root() {
        return Map.of(
            "service", "springboot",
            "springBootVersion", SpringBootVersion.getVersion()
        );
    }
}
