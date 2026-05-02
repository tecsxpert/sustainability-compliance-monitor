package com.internship.tool.controller;

import org.springframework.web.bind.annotation.*;

import java.util.Map;

@RestController
@RequestMapping("/api/ai")
@CrossOrigin(origins = "http://localhost:5173")
public class AiController {

    @PostMapping("/recommend")
    public Map<String, String> recommend(@RequestBody Map<String, Object> request) {

        return Map.of(
                "insight",
                "AI Insight: This company shows moderate compliance. Improve environmental and governance practices."
        );
    }
}