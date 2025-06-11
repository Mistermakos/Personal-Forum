CREATE DATABASE Forum;

CREATE TABLE IF NOT EXISTS Users(
    UserId SERIAL PRIMARY KEY,
    Name TEXT UNIQUE NOT NULL,
    Password TEXT NOT NULL,
    Email TEXT UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS Admins(
    UserId INTEGER PRIMARY KEY REFERENCES Users(UserId)
);

CREATE TABLE IF NOT EXISTS Posts(
    PostId SERIAL PRIMARY KEY,
    UserId INTEGER REFERENCES Users(UserId),
    Title TEXT NOT NULL,
    PostContent TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Comments(
    CommentId SERIAL PRIMARY KEY,
    UserId INTEGER REFERENCES Users(UserId),
    PostId INTEGER REFERENCES Posts(PostId),
    Comment TEXT NOT NULL
);

CREATE PROCEDURE LoginCheck(name TEXT, password TEXT)
LANGUAGE SQL
AS $$
    SELECT COUNT(*) FROM Users WHERE Name = name AND Password = password;
END $$;

-- ALL Get PROCEDURES
CREATE PROCEDURE GetEmails()
LANGUAGE SQL
AS $$
    SELECT Email FROM Users;
END $$;

CREATE PROCEDURE GetPosts()
LANGUAGE SQL
AS $$
    Select * from Posts;
END $$;

CREATE PROCEDURE GetAdmins()
LANGUAGE SQL
AS $$
    SELECT Users.Name, Admins.UserId
    FROM Admins
    INNER JOIN Users
    on Users.UserId = Admins.UserId
END $$;

CREATE PROCEDURE GetCommentsFromPost(Id SERIAL)
LANGUAGE SQL
AS $$
    SELECT Users.Name, Comments.Comment
    FROM Comments 
    INNER JOIN Users 
    ON Users.UserId = Comments.UserId 
    WHERE PostId = Id 
END $$;

CREATE PROCEDURE GetCommentsFromUser(Id Serial)
LANGUAGE SQL
AS $$
    SELECT Posts.Title, Comments.Comment
    FROM Comments
    INNER JOIN Posts 
    ON Posts.PostId = Comments.PostId
    WHERE Comments.UserId = Id 
END $$;

-- ALL Add PROCEDURES
CREATE PROCEDURE AddPost(IN p_UserId INTEGER, IN p_Title TEXT, IN p_PostContent TEXT)
LANGUAGE SQL
AS $$
    INSERT INTO Posts (UserId, Title, PostContent) VALUES (p_UserId, p_Title, p_PostContent);
$$;

CREATE PROCEDURE AddComment(IN p_UserId INTEGER, IN p_PostId INTEGER, IN p_Comment TEXT)
LANGUAGE SQL
AS $$
    INSERT INTO Comments (UserId, PostId, Comment) VALUES (p_UserId, p_PostId, p_Comment);
$$;


CREATE PROCEDURE AddAdmin(UserId SERIAL)
LANGUAGE SQL
AS $$
    INSERT INTO Admins VALUES (UserId);
END $$;

CREATE PROCEDURE AddUser(IN p_Name TEXT, IN p_Password TEXT, IN p_Email TEXT)
LANGUAGE SQL
AS $$
    INSERT INTO Users (Name, Password, Email) VALUES (p_Name, p_Password, p_Email);
$$;


-- All Delete Procedures

CREATE PROCEDURE DeleteComment(UserId SERIAL, PostId SERIAL)
LANGUAGE SQL
AS $$
    DELETE
    FROM Comments
    WHERE Comments.UserId = UserId AND Comments.PostId = PostId;
END $$;

CREATE PROCEDURE DeletePost(PostId SERIAL)
LANGUAGE SQL
AS $$
    DELETE
    FROM Comments
    WHERE Comments.PostId = PostId;

    DELETE 
    FROM Posts 
    WHERE Posts.PostId = PostId; 
END $$;

CREATE PROCEDURE DeleteAdmin(UserId SERIAL)
LANGUAGE SQL
AS $$
    DELETE
    FROM Admins
    WHERE Admins.UserId = UserId;
END $$;

CREATE PROCEDURE DeleteUser(UserId SERIAL)
LANGUAGE SQL
AS $$
    DELETE
    FROM Comments
    WHERE Comments.UserId = UserId;

    DELETE 
    FROM Posts 
    WHERE Posts.UserId = UserId; 

    DELETE
    FROM Admins
    WHERE Admins.UserId = UserId;

    DELETE
    FROM Users
    WHERE Users.UserId = UserId;
END $$;
