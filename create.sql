CREATE TABLE IF NOT EXISTS myapp_conversation (
    id SERIAL PRIMARY KEY,
    userId VARCHAR(100),
    conversationId VARCHAR(100),
    optionPicked VARCHAR(100),
    state VARCHAR(100)
);
