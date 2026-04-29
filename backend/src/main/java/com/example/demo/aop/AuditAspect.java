package com.example.demo.aop;

import com.example.demo.entity.ComplianceRecord;
import com.example.demo.service.AuditService;

import org.aspectj.lang.JoinPoint;
import org.aspectj.lang.annotation.AfterReturning;
import org.aspectj.lang.annotation.Aspect;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.stereotype.Component;

@Aspect
@Component
public class AuditAspect {

    private final AuditService auditService;

    public AuditAspect(AuditService auditService) {
        this.auditService = auditService;
    }

    // 🔹 Helper method
    private String getUsername() {
        return SecurityContextHolder.getContext()
                .getAuthentication()
                .getName();
    }

    // 🔹 CREATE
    @AfterReturning(
        pointcut = "execution(* com.example.demo.controller.ComplianceController.create(..))",
        returning = "result"
    )
    public void logCreate(Object result) {

        ComplianceRecord saved = (ComplianceRecord) result;

        auditService.log(
                "CREATE",
                "ComplianceRecord",
                saved.getId(),
                getUsername(),   // ✅ FIXED
                "Created record"
        );
    }

    // 🔹 UPDATE
    @AfterReturning(
        pointcut = "execution(* com.example.demo.controller.ComplianceController.update(..))"
    )
    public void logUpdate(JoinPoint joinPoint) {

        Long id = (Long) joinPoint.getArgs()[0];

        auditService.log(
                "UPDATE",
                "ComplianceRecord",
                id,
                getUsername(),   // ✅ FIXED
                "Updated record"
        );
    }

    // 🔹 DELETE
    @AfterReturning(
        pointcut = "execution(* com.example.demo.controller.ComplianceController.delete(..))"
    )
    public void logDelete(JoinPoint joinPoint) {

        Long id = (Long) joinPoint.getArgs()[0];

        auditService.log(
                "DELETE",
                "ComplianceRecord",
                id,
                getUsername(),   // ✅ FIXED
                "Deleted record"
        );
    }
}