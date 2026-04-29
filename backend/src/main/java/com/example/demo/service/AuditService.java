package com.example.demo.service;

import com.example.demo.model.AuditLog;
import com.example.demo.repository.AuditLogRepository;

import org.springframework.stereotype.Service;

@Service
public class AuditService {

    private final AuditLogRepository repo;

    public AuditService(AuditLogRepository repo) {
        this.repo = repo;
    }

    public void log(String action, String entity, Long entityId, String username, String details) {

        System.out.println("AUDIT SERVICE HIT");

        AuditLog log = new AuditLog();
        log.setAction(action);
        log.setEntity(entity);
        log.setEntityId(entityId);
        log.setUsername(username);
        log.setDetails(details);

        try {
            repo.save(log);
            System.out.println("AUDIT SAVED");
        } catch (Exception e) {
            e.printStackTrace();   // 🔥 will show real error if any
        }
    }
}