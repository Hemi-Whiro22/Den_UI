
-- Kitenga Chat Memory Table
create table if not exists messages (
  id uuid primary key default gen_random_uuid(),
  user_id text not null,
  message text not null,
  response text not null,
  timestamp timestamptz default timezone('utc', now())
);

-- Optional: Profile Table for tracking glyphs, preferences, mana state
create table if not exists profiles (
  user_id text primary key,
  username text,
  glyph_id text,
  created_at timestamptz default timezone('utc', now())
);

-- Indexing
create index if not exists idx_user_timestamp on messages (user_id, timestamp);
