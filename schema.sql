-- reSnap database

create table profiles (
 id uuid primary key references auth.users(id) on delete cascade,
 username text unique,
 created_at timestamp default now()
);

create table friends (
 id uuid primary key default gen_random_uuid(),
 user_id uuid references auth.users(id),
 friend_id uuid references auth.users(id),
 status text default 'pending',
 created_at timestamp default now()
);

create table snaps (
 id uuid primary key default gen_random_uuid(),
 sender_id uuid references auth.users(id),
 receiver_id uuid references auth.users(id),
 media_url text not null,
 caption text default '',
 opened boolean default false,
 expires_at timestamp,
 created_at timestamp default now()
);

create table messages (
 id uuid primary key default gen_random_uuid(),
 sender_id uuid references auth.users(id),
 receiver_id uuid references auth.users(id),
 text text,
 created_at timestamp default now()
);
