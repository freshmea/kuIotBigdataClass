-- dorepeat procedure registration
USE `madangdb`;
DROP procedure IF EXISTS `dorepeat1`;

USE `madangdb`;
DROP procedure IF EXISTS `madangdb`.`dorepeat1`;
;

DELIMITER $$
USE `madangdb`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `dorepeat1`(p1 int)
begin
	set @x= 0;
    repeat 
		set @x=@x+1;
	until @x > p1
    end repeat;
end$$

DELIMITER ;
;
-- dorepeat registraion end

call dorepeat(100);
select @x;


-- insertbook procedure registration
USE `madangdb`;
DROP procedure IF EXISTS `insertbook`;

DELIMITER $$
USE `madangdb`$$
CREATE PROCEDURE `insertbook` (
	in mybookid integer,
    in mybookname varchar(40),
    in mypublisher varchar(40),
    in myprice integer)
BEGIN
	insert into Book(bookid, bookname, publisher, price) 
		values(mybookid, mybookname, mypublisher, myprice);
END$$

DELIMITER ;

-- registraion end
