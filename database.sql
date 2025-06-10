CREATE DATABASE Forum;

CREATE TABLE IF NOT EXISTS Users(
    UserId SERIAL PRIMARY KEY,
    Name TEXT UNIQUE NOT NULL,
    Email TEXT UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS Admins(
    UserId SERIAL REFERENCES Users(UserId)
);

CREATE TABLE IF NOT EXISTS Posts(
    PostId SERIAL PRIMARY KEY,
    Title TEXT NOT NULL,
    PostContent TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Comments(
    UserId SERIAL REFERENCES Users(UserId),
    PostId SERIAL REFERENCES Posts(PostId),
    Comment TEXT NOT NULL
);


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
CREATE PROCEDURE AddPost(Title TEXT, PostContent TEXT)
LANGUAGE SQL
AS $$
    INSERT INTO POST VALUES (NULL, Title, PostContent );
END $$;

CREATE PROCEDURE AddComment(UserId SERIAL, PostId SERIAL, Comment TEXT);
LANGUAGE SQL
AS $$
    INSERT INTO Comments VALUES (UserId SERIAL, PostId SERIAL, Comment TEXT);
END $$;

CREATE PROCEDURE AddAdmin(UserId SERIAL)
LANGUAGE SQL
AS $$
    INSERT INTO Admins VALUES (UserId);
END $$;

CREATE PROCEDURE AddUser(Name TEXT, Email TEXT)
LANGUAGE SQL
AS $$
    INSERT INTO POST VALUES (Name, Email);
END $$;

-- All Delete Procedures

CREATE PROCEDURE DeleteComment(UserId SERIAL, PostId SERIAL)
LANGUAGE SQL
AS $$
    DELETE *
    FROM Comments
    WHERE Comments.UserId = UserId && Comments.PostId = PostId;
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
