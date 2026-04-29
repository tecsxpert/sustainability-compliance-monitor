package com.example.demo.repository;

import com.example.demo.entity.ComplianceRecord;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

import java.util.List;

public interface ComplianceRepository extends JpaRepository<ComplianceRecord, Long> {

    // 🔍 search
    List<ComplianceRecord> findByCompanyNameContainingIgnoreCase(String name);

    // 🔍 filter
    List<ComplianceRecord> findByStatus(String status);

    // 📊 REQUIRED FOR DASHBOARD
    long countByStatus(String status);

    @Query("SELECT AVG(c.complianceScore) FROM ComplianceRecord c")
    Double findAverageScore();
}