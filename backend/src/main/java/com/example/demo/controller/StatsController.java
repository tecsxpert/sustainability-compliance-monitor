package com.example.demo.controller;

import com.example.demo.repository.ComplianceRepository;
import org.springframework.web.bind.annotation.*;

import java.util.HashMap;
import java.util.Map;

@RestController
@RequestMapping("/api")
@CrossOrigin
public class StatsController {

    private final ComplianceRepository repository;

    public StatsController(ComplianceRepository repository) {
        this.repository = repository;
    }

    @GetMapping("/stats")
    public Map<String, Object> getStats() {

        long total = repository.count();
        long compliant = repository.countByStatus("COMPLIANT");
        long nonCompliant = repository.countByStatus("NON-COMPLIANT");

        Double avgScore = repository.findAverageScore();

        Map<String, Object> stats = new HashMap<>();
        stats.put("total", total);
        stats.put("compliant", compliant);
        stats.put("nonCompliant", nonCompliant);
        stats.put("avgScore", avgScore);

        return stats;
    }
}