package com.example.demo.controller;

import com.example.demo.entity.ComplianceRecord;
import com.example.demo.repository.ComplianceRepository;
import com.example.demo.service.AuditService;
import com.fasterxml.jackson.databind.ObjectMapper;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.test.web.servlet.MockMvc;

import org.springframework.security.test.context.support.WithMockUser;

import java.util.Arrays;
import java.util.Optional;

import static org.mockito.Mockito.when;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.*;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;

@WebMvcTest(ComplianceController.class)
@AutoConfigureMockMvc(addFilters = false)
public class ComplianceControllerTest {

    @Autowired
    private MockMvc mockMvc;

    @MockBean
    private ComplianceRepository repository;

    @MockBean
    private AuditService auditService;

    @Autowired
    private ObjectMapper objectMapper;

    // 🔹 GET ALL
    @Test
    @WithMockUser
    void testGetAll() throws Exception {
        ComplianceRecord record = new ComplianceRecord();
        record.setId(1L);
        record.setCompanyName("Test Company");

        when(repository.findAll()).thenReturn(Arrays.asList(record));

        mockMvc.perform(get("/api/all"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$[0].companyName").value("Test Company"));
    }

    // 🔹 GET BY ID
    @Test
    @WithMockUser
    void testGetById() throws Exception {
        ComplianceRecord record = new ComplianceRecord();
        record.setId(1L);
        record.setCompanyName("Test Company");

        when(repository.findById(1L)).thenReturn(Optional.of(record));

        mockMvc.perform(get("/api/1"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.companyName").value("Test Company"));
    }

    // 🔹 CREATE
    @Test
    @WithMockUser
    void testCreate() throws Exception {
        ComplianceRecord record = new ComplianceRecord();
        record.setCompanyName("New Company");

        when(repository.save(record)).thenReturn(record);

        mockMvc.perform(post("/api/create")
                .contentType("application/json")
                .content(objectMapper.writeValueAsString(record)))
                .andExpect(status().isOk());
    }

    // 🔹 DELETE
    @Test
    @WithMockUser
    void testDelete() throws Exception {
        mockMvc.perform(delete("/api/1"))
                .andExpect(status().isOk());
    }
}