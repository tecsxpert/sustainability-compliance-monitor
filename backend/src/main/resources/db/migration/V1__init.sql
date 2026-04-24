CREATE TABLE compliance_record (
    id SERIAL PRIMARY KEY,
    company_name VARCHAR(255) NOT NULL,
    compliance_score INT,
    status VARCHAR(50),
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);