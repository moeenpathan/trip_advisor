Create table trip_advisor.travel_details(
	Trip_ID INT PRIMARY KEY, 
	Destination VARCHAR (100), 
	Start_date DATETIME, 
	End_date DATETIME, 
	Duration FLOAT,
    Traveler_name VARCHAR (50),
	Traveler_age INT, 
	Traveler_gender CHAR (15),
    Traveler_nationality CHAR (25), 
	Accommodation_type CHAR (15),
	Accommodation_type_id INT,
	Accommodation_cost FLOAT,
    Transportation_type CHAR (20), 
	Transportation_type_id INT,
	Transportation_cost FLOAT
		);
        
select * from trip_advisor.travel_details;
truncate table trip_advisor.travel_details;
drop table trip_advisor.travel_details;

CREATE TABLE `travel_details` (
  `Trip_ID` int NOT NULL,
  `Destination` varchar(100) DEFAULT NULL,
  `Start_date` datetime DEFAULT NULL,
  `End_date` datetime DEFAULT NULL,
  `Duration` float DEFAULT NULL,
  `Traveler_name` varchar(50) DEFAULT NULL,
  `Traveler_age` int DEFAULT NULL,
  `Traveler_gender` char(15) DEFAULT NULL,
  `Traveler_nationality` char(25) DEFAULT NULL,
  `Accommodation_type` char(15) DEFAULT NULL,
  `Accommodation_type_id` int DEFAULT NULL,
  `Accommodation_cost` float DEFAULT NULL,
  `Transportation_type` char(20) DEFAULT NULL,
  `Transportation_type_id` int DEFAULT NULL,
  `Transportation_cost` float DEFAULT NULL,
  PRIMARY KEY (`Trip_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
