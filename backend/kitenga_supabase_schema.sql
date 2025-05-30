
-- Table: messages
CREATE TABLE IF NOT EXISTS messages (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id TEXT NOT NULL,
    message TEXT NOT NULL,
    response TEXT,
    timestamp TIMESTAMPTZ DEFAULT now()
);

-- Table: profiles
CREATE TABLE IF NOT EXISTS profiles (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id TEXT UNIQUE NOT NULL,
    display_name TEXT,
    glyph_id TEXT,
    created_at TIMESTAMPTZ DEFAULT now()
);
