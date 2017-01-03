--======================================================================================================--
/* 
Freeman Cooley's SQL Library Drill Code for The Tech Academy

This creates the databae: "FC_Library"

*/

USE MASTER
GO


IF EXISTS

(SELECT * from sys.databases WHERE name='FC_Library')

BEGIN
	DROP DATABASE FC_Library;
END


CREATE DATABASE FC_Library;

GO

USE FC_Library
GO




--======================================================================================================--

--Adding a table with my Libraries

CREATE TABLE LIBRARY_BRANCH
	(BranchID int PRIMARY KEY NOT NULL,
	 BranchName varchar(100) NULL,
	 Address nvarchar(100) NULL)
GO

INSERT INTO

dbo.Library_Branch (BranchID, BranchName, Address)

VALUES

(1, 'Sharpstown', '525 East Baseline Rd. Mesa, Az'),
(2, 'Central', '8999 West Runfortheborder Way, Tempe, Az'),
(3, 'Firetown', '1661 North Winkywink Dr, Eyelash, Az'),
(4, 'Cactus Head', '1776 South Southofhere Blvd, Glendale, Az')

GO




--======================================================================================================--
--Creating a TABLE called "BOOK"

CREATE TABLE BOOK
	(BookID int PRIMARY KEY NOT NULL,
	 Title varchar(90) NOT NULL,
	 PublisherName varchar(60) NOT NULL)
GO

--Adding Various books to the "BOOK" table

INSERT INTO
dbo.Book (BookID, Title, PublisherName)
VALUES
(0001, 'The Lost Tribe', 'Holt'),
(0002, 'The Tommyknockers', 'Simon & Schuster'),
(0003, 'Born to Run', 'Simon & Schuster'),
(0004, 'Zero K', 'Simon & Schuster'),
(0005, 'Barkskins', 'Simon & Schuster'),
(0006, 'The Gene', 'Simon & Schuster'),
(0007, 'Hammer of the Gods: The Led Zeppelin Saga', 'William Morrow & Co'),
(0008, 'Battlefield Earth: A Saga of the Year 3000', 'Galaxy Press'),
(0009, 'Tarzan Of The Apes', 'A. C. McClurg'),
(0010, 'One Soldier', 'Harper Collins'),
(0011, 'So Big', 'Harper Collins'),
(0012, 'The Queen Of Attolia', 'Harper Collins'),
(0013, 'Frog And Toad Are Friends', 'Harper Collins'),
(0014, 'Pilgrim At Tinker Creek', 'Harper Collins'),
(0015, 'A Game of Thrones', 'Random House'),
(0016, 'Fallout The Hot War', 'Random House'),
(0017, 'Rushing Waters', 'Random House'),
(0018, 'The Force Awakens', 'Random House'),
(0019, 'Golden Son', 'Random House'),
(0020, 'Written in my own Heart''s Blood', 'Random House') --Title has an apostrophe so I need to use the "SQL apostrophe rules"..-- 
                                                           --..by adding a 2nd apostrophe letting it be a character--

GO

--Ok, good, that worked.

--======================================================================================================--

--Create a new table called Book_Authors
CREATE TABLE BOOK_AUTHORS
	(BookID int NOT NULL,
		 AuthorName varchar(100) NOT NULL)
GO

--Adding the Authors corresponding to the book numbers

INSERT INTO

dbo.Book_Authors (BookID, AuthorName)

VALUES

(0001, 'Edward Marriott'),
(0002, 'Stephen King'),
(0003, 'Bruce Springsteen'),
(0004, 'Don DeLillo'),
(0005, 'Annie Proulx'),
(0006, 'Siddhartha Mukherjee'),
(0007, 'Stephen Davis'),
(0008, 'L. Ron Hubbard'),
(0009, 'Edgar Rice Burroughs '),
(0010, 'Dillon Hillier, Russell Hillier'),
(0011, 'Megan Whalen Turner'),
(0012, 'Some Guy'),
(0013, 'Arnold Lobel'),
(0014, 'Annie Dillard'),
(0015, 'George R. R. Martin'),
(0016, 'Harry Turtledove'),
(0017, 'Danielle Steel'),
(0018, 'Alan Dean Foster'),
(0019, ' Pierce Brown'),
(0020, 'Diana Gabaldon')


GO

--======================================================================================================--

--Adding table for PUBLISHER

CREATE TABLE PUBLISHER
	(Name varchar(100) PRIMARY KEY NOT NULL,
	 Address nvarchar(100) NULL,
	 Phone varchar(100) NULL)

GO

--Adding Publisher Info into table

INSERT INTO
dbo.Publisher 
(Name, Address, Phone)

VALUES


('Holt', '175 Fifth Ave, New York, NY', '646-307-5095'),
('Simon & Schuster', '1230 Avenue of the Americas, 10th F, New York, NY', '800-223-2336'),
('William Morrow & Co', ' 10 East 53rd Street, New York, NY', '212-207-7000'),
('Galaxy Press', '7051 Hollywood Blvd., Suite 200, Hollywood, CA', '877-842-5299'),
('A. C. McClurg', 'Chicago, IL', NULL), --Adding NULL since Publisher no longer exists--
('Harper Collins', '195 Broadway New York, NY', '212-207-7000'),
('Random House', 'Random House Tower New York, NY', '800-733-3000')

GO

--======================================================================================================--


--Table for Book Copies

CREATE TABLE BOOK_COPIES
	(BookID int NOT NULL,
	 BranchID int NOT NULL,
	 No_Of_Copies int NULL)
GO

--Inserting the book copies corresponding to the branches and # of copies

INSERT INTO

dbo.Book_Copies (BookID, BranchID, No_Of_Copies)

VALUES

(0001,1, 3),(0001,2, 2),(0001,3, 2),(0001,4, 3),(0002,1, 5),(0002,2, 4),(0002,3, 2),(0002,4, 3),
(0003,1, 9),(0003,2, 5),(0003,3, 4),(0003,4, 2),(0004,1, 3),(0004,2, 2),(0004,3, 2),(0004,4, 3),
(0005,1, 5),(0005,2, 4),(0005,3, 2),(0005,4, 3),(0006,1, 9),(0006,2, 5),(0006,3, 4),(0006,4, 2),
(0007,1, 3),(0007,2, 2),(0007,3, 2),(0007,4, 3),(0008,1, 5),(0008,2, 4),(0008,3, 2),(0008,4, 3),
(0009,1, 9),(0009,2, 5),(0009,3, 4),(0009,4, 2),(0010,1, 3),(0010,2, 2),(0010,3, 2),(0010,4, 3),
(0011,1, 5),(0011,2, 4),(0011,3, 2),(0011,4, 3),(0012,1, 9),(0012,2, 5),(0012,3, 4),(0012,4, 2),
(0013,1, 3),(0013,2, 2),(0013,3, 2),(0013,4, 3),(0014,1, 5),(0014,2, 4),(0014,3, 2),(0014,4, 3),
(0015,1, 9),(0015,2, 5),(0015,3, 4),(0015,4, 2),(0016,1, 3),(0016,2, 2),(0016,3, 2),(0016,4, 3),
(0017,1, 5),(0017,2, 4),(0017,3, 2),(0017,4, 3),(0018,1, 9),(0018,2, 5),(0018,3, 4),(0018,4, 2),
(0019,1, 3),(0019,2, 2),(0019,3, 2),(0019,4, 3),(0020,1, 5),(0020,2, 4),(0020,3, 2),(0020,4, 3)


GO
--======================================================================================================--

--Creating a table for tracking book loans

CREATE TABLE BOOK_LOANS
	
	(BookID int NOT NULL,
	 BranchID int NOT NULL,
	 CardNo int NOT NULL,
	 DateOut varchar(100) NOT NULL,
	 DueDate varchar(100) NOT NULL)

GO

--Adding all the book loans data to table

INSERT INTO

dbo.BOOK_LOANS 

(BookID, BranchID, CardNo, DateOut, DueDate)

VALUES

(0001,1,89912, '11-21-2016', '02-23-2017'),(0001,2,90765, '11-22-2016', '02-24-2017'),
(0001,3,89913, '11-21-2016', '02-23-2017'),(0002,4,90766, '11-22-2016', '02-23-2017'),
(0002,3,89914, '10-02-2016', '01-03-2017'),(0003,1,90767, '10-01-2016', '10-05-2017'),
(0003,2,89915, '10-02-2016', '01-03-2017'),(0003,1,90768, '10-01-2016', '10-05-2017'),
(0003,1,89916, '09-17-2016', '12-19-2016'),(0004,4,90769, '09-13-2016', '12-21-2016'),
(0004,3,89917, '09-17-2016', '12-19-2016'),(0005,2,90770, '09-13-2016', '12-21-2016'),
(0005,2,89918, '08-22-2016', '10-23-2016'),(0005,3,90771, '08-07-2016', '10-24-2016'),
(0005,4,89919, '08-22-2016', '10-23-2016'),(0006,3,90772, '08-07-2016', '10-24-2016'),
(0006,1,89920, '11-21-2016', '02-23-2017'),(0006,3,90773, '11-22-2016', '02-24-2017'),
(0006,2,89921, '11-21-2016', '02-23-2017'),(0007,4,90774, '11-22-2016', '02-23-2017'),
(0008,2,89922, '10-02-2016', '01-03-2017'),(0008,1,90775, '10-01-2016', '10-05-2017'),
(0009,4,89923, '10-02-2016', '01-03-2017'),(0009,3,90776, '10-01-2016', '10-05-2017'),
(0010,1,89924, '09-17-2016', '12-19-2016'),(0010,1,90777, '09-13-2016', '12-21-2016'),
(0010,2,89925, '09-17-2016', '12-19-2016'),(0010,3,90778, '09-13-2016', '12-21-2016'),
(0010,4,89926, '08-22-2016', '10-23-2016'),(0010,3,90779, '08-07-2016', '10-24-2016'),
(0011,1,89927, '08-22-2016', '10-23-2016'),(0011,2,90780, '08-07-2016', '10-24-2016'),
(0011,1,89928, '11-21-2016', '02-23-2017'),(0011,1,90781, '11-22-2016', '02-24-2017'),
(0012,4,89929, '11-21-2016', '02-23-2017'),(0013,3,90782, '11-22-2016', '02-23-2017'),
(0014,2,89930, '10-02-2016', '01-03-2017'),(0015,2,90783, '10-01-2016', '10-05-2017'),
(0012,3,89931, '10-02-2016', '01-03-2017'),(0013,4,90784, '10-01-2016', '10-05-2017'),
(0014,3,89932, '09-17-2016', '12-19-2016'),(0015,1,90785, '09-13-2016', '12-21-2016'),
(0016,3,89933, '09-17-2016', '12-19-2016'),(0017,2,90786, '09-13-2016', '12-21-2016'),
(0018,4,89934, '08-22-2016', '10-23-2016'),(0018,2,90787, '08-07-2016', '10-24-2016'),
(0019,1,89935, '08-22-2016', '10-23-2016'),(0020,4,90788, '08-07-2016', '10-24-2016'),
(0020,3,89936, '11-21-2016', '02-23-2017')

GO


--======================================================================================================--

--Creating my Borrowers table

CREATE TABLE BORROWER
	
	(CardNo int NOT NULL,
	 Name varchar(100) NULL,
	 Address nvarchar(100) NULL,
	 Phone varchar(50) NULL,
	 BooksCheckedOut int NULL,)


GO

--Adding all the borrowers to the table

INSERT INTO

dbo.Borrower (CardNo, Name, Address, Phone, BooksCheckedOut)

VALUES

(89912, 'John Doe', '555 W last St. Wobbly, AZ',987-786-0066,7),
(90765, 'Fred Flinstone', '1919 N TooToo, Nutsalot, AZ',922-186-0369,1),
(89913, 'Barney Rubble', '989 S Yie Pie Dr, Rustynail, AZ',987-786-0067,2),
(90766, 'Al Bundy', '932 E East St, Fillupyour tank, AZ',922-186-0370,3),
(89914, 'Bugs Bunny', '555 W last St, Wobbly, AZ',987-786-0068,6),
(90767, 'Marvin Martian', '8 E Kindofsilly Dr, Wonton, AZ',922-186-0371,1),
(89915, 'Master Chief', '8999 S Covenant Way, Halo, AZ',987-786-0069,1),
(90768, 'Mickey Mouse', '1 W Disney Pkwy, Disneyland, CA',922-186-0372,3),
(89916, 'Charles Manson', '6666 W Crazymean Breezway, Folsem, CA',987-786-0070,7),
(90769, 'Marlyn Manson', '222 N Youcankeephim, Portland, OR',922-186-0373,0),
(89917, 'Wiggly Toes', '553 W Icky St. Buddy, AZ',987-786-0071,2),
(90770, 'Dairy Queen', '1919 M Hooray DR, Mesatown, AZ',922-186-0374,3),
(89918, 'Sam Iam', '8 S OohOoh. WelcomebackCotter, NY',987-786-0072,6),
(90771, 'Greeneggs Andham', '10 N Tententen Pkwy. Ten, NY',922-186-0375,1),
(89919, 'Sooo Boring', '30 W Free St, Free, AZ',987-786-0073,1),
(90772, 'Last Place', '515 W Ovationforever Dr, Tempediablo, AZ',922-186-0376,3),
(89920, 'Cherry Blossom', '9976 N Cold Ln, Fever, AZ',987-786-0074,3),
(90773, 'Pink Panther', '22 W Pokeythorns Blvd Cactushead, AZ',922-186-0377,3),
(89921, 'Jim Jones', '12 S Huh St, Firebridge, AZ',987-786-0075,1),
(90774, 'Letme Pumpmyowngas', '1651 W Greenforest Dr, Portaland, OR',922-186-0378,0)

GO

/* END */

--======================================================================================================--