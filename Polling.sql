CREATE DATABASE IF NOT EXISTS `polling` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `polling`;

CREATE TABLE IF NOT EXISTS `tbl` (
    `id` int(11) NOT NULL,
	`title` varchar(100) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
INSERT INTO `tbl` (`id`, `title`) VALUES
(1, 'Flask'),
(2, 'React.js'),
(3, 'Express'),
(4, 'Django');

ALTER TABLE `tbl`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
  
CREATE TABLE IF NOT EXISTS `tblpoll` (
    `poll_id` int(11) NOT NULL,
	`web_framework` varchar(100) NOT NULL,
    PRIMARY KEY (`poll_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
INSERT INTO `tblpoll` (`poll_id`, `web_framework`) VALUES
(7, 'Flask'),
(8, 'Flask'),
(9, 'Flask'),
(10, 'Flask'),
(11, 'Express'),
(12, 'React.js'),
(13, 'Laravel'),
(14, 'Flask'),
(15, 'Flask'),
(16, 'Laravel'),
(17, 'Django'),
(18, 'Django');


ALTER TABLE `tblpoll`
  MODIFY `poll_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;
