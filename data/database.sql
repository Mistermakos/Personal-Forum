-- Tworzenie tabeli Users
CREATE TABLE IF NOT EXISTS Users (
    UserId INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT UNIQUE NOT NULL,
    Password TEXT NOT NULL,
    Email TEXT UNIQUE NOT NULL
);

-- Tworzenie tabeli Admins
CREATE TABLE IF NOT EXISTS Admins (
    UserId INTEGER PRIMARY KEY,
    FOREIGN KEY (UserId) REFERENCES Users(UserId)
);

-- Tworzenie tabeli Posts
CREATE TABLE IF NOT EXISTS Posts (
    PostId INTEGER PRIMARY KEY AUTOINCREMENT,
    UserId INTEGER,
    Title TEXT NOT NULL,
    PostContent TEXT NOT NULL,
    FOREIGN KEY (UserId) REFERENCES Users(UserId)
);

-- Tworzenie tabeli Comments
CREATE TABLE IF NOT EXISTS Comments (
    CommentId INTEGER PRIMARY KEY AUTOINCREMENT,
    UserId INTEGER,
    PostId INTEGER,
    Comment TEXT NOT NULL,
    FOREIGN KEY (UserId) REFERENCES Users(UserId),
    FOREIGN KEY (PostId) REFERENCES Posts(PostId)
);
