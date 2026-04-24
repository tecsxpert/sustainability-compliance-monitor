package com.example.demo.controller;

import com.example.demo.entity.ComplianceRecord;
import com.example.demo.repository.ComplianceRepository;
import jakarta.validation.Valid;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api")
@CrossOrigin
public class ComplianceController {

    private final ComplianceRepository repo;

    public ComplianceController(ComplianceRepository repo) {
        this.repo = repo;
    }

    @GetMapping("/all")
    public List<ComplianceRecord> getAll() {
        return repo.findAll();
    }

    @GetMapping("/status/{status}")
    public List<ComplianceRecord> getByStatus(@PathVariable String status) {
        return repo.findByStatus(status);
    }

    @PostMapping("/create")
    public ComplianceRecord create(@Valid @RequestBody ComplianceRecord record) {
        return repo.save(record);
    }

    @PutMapping("/{id}")
    public ComplianceRecord update(@PathVariable Long id,
                                   @Valid @RequestBody ComplianceRecord updated) {
        ComplianceRecord record = repo.findById(id).orElseThrow();

        record.setCompanyName(updated.getCompanyName());
        record.setComplianceScore(updated.getComplianceScore());
        record.setStatus(updated.getStatus());
        record.setDescription(updated.getDescription());

        return repo.save(record);
    }

    @DeleteMapping("/{id}")
    public void delete(@PathVariable Long id) {
        repo.deleteById(id);
    }

    @GetMapping("/search")
    public List<ComplianceRecord> search(@RequestParam String q) {
        return repo.findByCompanyNameContainingIgnoreCase(q);
    }
}