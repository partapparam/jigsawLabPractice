CREATE TABLE IF NOT EXISTS movies (
    title VARCHAR(255) UNIQUE NOT NULL,
    id SERIAL PRIMARY KEY,
    genre VARCHAR(255),
    budget BIGINT,
    runtime DECIMAL,
    year INTEGER,
    month INTEGER,
    revenue BIGINT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
