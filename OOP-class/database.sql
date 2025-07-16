CREATE TABLE passengers(
    id int primary key,
    passenger_name varchar(100),
    passenger_class varchar(50),
    price decimal(10,2),
    booking_date datetime,
    ticket_confirmed int);

insert into passengers values(22, "helen", "economy", 1000, current_timestamp, 1)