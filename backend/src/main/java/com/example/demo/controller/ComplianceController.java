package com.example.demo.controller;

import org.springframework.web.bind.annotation.*;
import java.util.*;

@RestController
@RequestMapping("/api")
@CrossOrigin
public class ComplianceController {

    @GetMapping("/all")
    public List<Map<String, Object>> getAll() {

        List<Map<String, Object>> data = new ArrayList<>();

        Map<String, Object> item1 = new HashMap<>();
        item1.put("id", 1);
        item1.put("company_name", "ABC Corp");
        item1.put("status", "COMPLIANT");

        Map<String, Object> item2 = new HashMap<>();
        item2.put("id", 2);
        item2.put("company_name", "XYZ Ltd");
        item2.put("status", "NON-COMPLIANT");

        data.add(item1);
        data.add(item2);

        return data;
    }
}