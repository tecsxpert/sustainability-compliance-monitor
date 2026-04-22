package com.example.demo.entity;

import jakarta.persistence.*;
import java.time.LocalDateTime;

@Entity
@Table(name = "compliance_record")
public class ComplianceRecord {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "company_name")
    private String companyName;

    @Column(name = "compliance_score")
    private Integer complianceScore;

    @Column
    private String status;

    @Column
    private String description;

    @Column(name = "created_at")
    private LocalDateTime createdAt;

    // getters and setters
}