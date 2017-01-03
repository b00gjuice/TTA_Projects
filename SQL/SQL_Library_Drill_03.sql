
/*

Student: Freeman Cooley

The Tech Academy SQL Query Drills 1-7 + Stored Procedure

Note: The "Stored Procedure" is part of #5

These are all the queries required by the SQL Drill Assignment

*/

--============================================================================--


USE FC_Library
GO

/*

1. How many copies of the book titled The Lost Tribe are owned by the 
library branch whose name is "Sharpstown"?--

*/




SELECT bc.BookID, bc.No_Of_Copies, lib.BranchID, lib.BranchName
FROM BOOK_COPIES as bc
FULL OUTER JOIN LIBRARY_BRANCH as lib
ON bc.BranchID = lib.BranchID
WHERE lib.BranchID = 1 AND bc.BookID = 0001


/*

Answer: 3 copies at Sharpstown Library:


BookID	  No_Of_Copies	  BranchID	BranchName
1	      3	              1	        Sharpstown

*/


--============================================================================--

/*
--2. How many copies of the book titled The Lost Tribe are 
owned by each branch?
*/


SELECT bk.Title, bk.BookID, lib.BranchName, bc.No_Of_Copies
FROM BOOK_COPIES AS bc
INNER JOIN LIBRARY_BRANCH AS lib
ON BC.BranchID = lib.BranchID JOIN book AS bk
ON BC.BookID = bk.BookID
WHERE bk.Title = 'The Lost Tribe'

/*

Answer: Sharpstown: 3, Central: 2, Firetown: 2, Cactus Head: 3,:

Title	        BookID	BranchName		No_Of_Copies
The Lost Tribe	1		Sharpstown		3
The Lost Tribe	1		Central			2
The Lost Tribe	1		Firetown		2
The Lost Tribe	1		Cactus Head		3
*/


--============================================================================--

/*

3. Retrieve the names of all borrowers who do not have any books checked out.

*/

SELECT brw.CardNo, brw.Name, brw.BooksCheckedOut
FROM BORROWER AS brw
INNER JOIN BOOK_LOANS AS bl
ON brw.CardNo = bl.CardNo
WHERE brw.BooksCheckedOut = 0

/*

Answer: Marlyn & Letme:


CardNo	Name				BooksCheckedOut
90769	Marlyn Manson		0
90774	Letme Pumpmyowngas	0

*/


--============================================================================--


/*
4. For each book that is loaned out from the "Sharpstown" branch and whose 
DueDate is today, retrieve the book title, the borrower's name, and the 
borrower's address. 

Note: Assuming "Today" is 02-23-2017
*/


SELECT bk.BookID, bk.Title, bl.DueDate, brw.Name, brw.[Address], lib.BranchName
FROM BOOK as bk
INNER JOIN Book_Loans as bl
ON bk.BookID = bl.BookID
INNER JOIN BORROWER as brw
ON bl.CardNo = brw.CardNo
INNER JOIN LIBRARY_BRANCH as lib
ON bl.BranchID = lib.BranchID
WHERE lib.BranchID = 1 
AND bl.DueDate = '02-23-2017'

/*

Answer: See table below:

BookID	Title			DueDate		Name			Address						BranchName
1		The Lost Tribe	2/23/2017	John Doe		555 W last St. Wobbly, AZ	Sharpstown
6		The Gene		2/23/2017	Cherry Blossom	9976 N Cold Ln, Fever, AZ	Sharpstown

*/

--============================================================================--

/*

5. For each library branch, retrieve the branch name and the total number of 
books loaned out from that branch.
choice."
Sharpstown = 1
Central = 2
Firetown = 3
Cactus Head = 4
FROM BOOK_LOANS AS bl
FULL OUTER JOIN LIBRARY_BRANCH AS lib
ON bl.BranchID = lib.BranchID
GROUP BY lib.BranchName, lib.BranchID
Sharpstown		1			13
Central			2			12
Firetown		3			14
Cactus Head		4			10


AS

IF @BranchID = 1
BEGIN
SELECT COUNT(BookID) AS [Sharpstown Branch Number of Books On Loan] FROM BOOK_LOANS WHERE BranchID = @BranchID;
END

IF @BranchID = 2
BEGIN
SELECT COUNT(BookID) AS [Central Branch Number of Books On Loan] FROM BOOK_LOANS WHERE BranchID = @BranchID;
END

IF @BranchID = 3
BEGIN
SELECT COUNT(BookID) AS [Firetown Branch Number of Books On Loan] FROM BOOK_LOANS WHERE BranchID = @BranchID;
END

IF @BranchID = 4
BEGIN
SELECT COUNT(BookID) AS [Cactus Head Branch Number of Books On Loan] FROM BOOK_LOANS WHERE BranchID = @BranchID;
END
--**********************************************************************************************************************

exec bookloans '1'
exec bookloans '2'
exec bookloans '3'
exec bookloans '4'

/*
Sharpstown Branch Number of Books On Loan	
13	
	
Central Branch Number of Books On Loan	
12	
	
Firetown Branch Number of Books On Loan	
14	
	
Cactus Head Branch Number of Books On Loan	
10	
*/

--============================================================================--

than five books checked out.
FROM BORROWER as brw
INNER JOIN BOOK_LOANS as bl
ON brw.CardNo = bl.CardNo
WHERE brw.BooksCheckedOut >= 5
ORDER BY brw.CardNo

CardNo	Name			Address									BooksCheckedOut	BookID
89912	John Doe		555 W last St. Wobbly, AZ				7				1
89914	Bugs Bunny		555 W last St, Wobbly, AZ				6				2
89916	Charles Manson	6666 W Crazymean Breezway, Folsem, CA	7				3
89918	Sam Iam			8 S OohOoh. WelcomebackCotter, NY		6				5

copies owned by the library branch whose name is "Central"
FROM BOOK as bk
INNER JOIN BOOK_AUTHORS as ba
ON bk.BookID = ba.BookID
INNER JOIN BOOK_COPIES as bc
ON bk.BookID = bc.BookID
INNER JOIN LIBRARY_BRANCH as lib
ON bc.BranchID = lib . BranchID
WHERE ba.AuthorName = 'Stephen King' AND lib.BranchID = 2

/*

Answer: The number of copies is 4

BookID	Title				AuthorName		No_Of_Copies	BranchName	BranchID
2		The Tommyknockers	Stephen King	4				Central		2


*/

--====================================================================================--