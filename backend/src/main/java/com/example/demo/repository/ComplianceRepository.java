package com.example.demo.repository;

import com.example.demo.entity.ComplianceRecord;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface ComplianceRepository extends JpaRepository<ComplianceRecord, Long> {

    List<ComplianceRecord> findByStatus(String status);

    List<ComplianceRecord> findByCompanyNameContainingIgnoreCase(String q);
}