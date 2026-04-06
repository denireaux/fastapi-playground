CREATE TABLE IF NOT EXISTS songs (
    id SERIAL PRIMARY KEY,
    title VARCHAR(50) NOT NULL UNIQUE,
    music_artist VARCHAR(100) NOT NULL,
    genre VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO songs (title, music_artist, genre)
VALUES
    ('One', 'Metallica', 'Metal'),
    ('Ethernal', 'HANA', 'Trance'),
    ('To Hide to Shine to Cross', 'Bragolin', 'Post Punk');
