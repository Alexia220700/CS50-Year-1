-- find the names of the witnesses and the description of the crime
SELECT interviews.name AS witness_name, crime_scene_reports.description
FROM interviews
JOIN crime_scene_reports ON crime_scene_reports.id = interviews.id
WHERE interviews.year = 2023
AND interviews.month = 7
AND interviews.day = 28
AND transcript LIKE '%bakery%';
-- witnesses: Ruth, Eugene, Raymond

-- to see the timetable of the theft
-- hint: theft took place at 10:15am
SELECT crime_scene_reports.description
FROM crime_scene_reports
WHERE year = 2023
AND month = 7
AND day = 28;

-- using this to see the transcripts of the witnesses
-- Ruth: gives the hint about the parking and license plate
-- Eugene gives the hint about the ATM
-- Raymond gives the hint about the phone call, that took < 1 minute
SELECT name AS witness_name, transcript
FROM interviews
JOIN crime_scene_reports ON crime_scene_reports.id = interviews.id
WHERE interviews.year = 2023
AND interviews.month = 7
AND interviews.day = 28
AND transcript LIKE '%bakery%';

-- find the names of the people that parked there
-- in plus, see the hour and minute of entrance and exit
-- check if it matches the timetable for theft
SELECT people.name AS thief_name, bakery_security_logs.license_plate, bakery_security_logs.hour, bakery_security_logs.minute, bakery_security_logs.activity
FROM people
JOIN bakery_security_logs ON bakery_security_logs.license_plate = people.license_plate
-- to narrow down the list
WHERE bakery_security_logs.year = 2023
AND bakery_security_logs.month = 7
AND bakery_security_logs.day = 28;

-- check if a person from the other list withdrew money from that certain ATM
-- narrow down the list by using the location of the atm
SELECT DISTINCT people.name AS possible_thief_name, atm_transactions.transaction_type, atm_transactions.atm_location
FROM atm_transactions
JOIN bank_accounts ON atm_transactions.account_number = atm_transactions.account_number
JOIN people ON people.id = bank_accounts.person_id
WHERE atm_transactions.year = 2023
AND atm_transactions.month = 7
AND atm_transactions.day = 28
AND atm_transactions.atm_location = 'Leggett Street';
-- Taylor, Diana, Bruce

-- check the phone call that took under one minute
SELECT people.name, phone_calls.duration, phone_calls.receiver
FROM phone_calls
JOIN people ON people.phone_number = phone_calls.caller
WHERE phone_calls.year = 2023
AND phone_calls.month = 7
AND phone_calls.day = 28;
-- Bruce, Taylor, Diana
-- Bruce's phone call took 45 seconds

-- join people table and passengers table through passport_number to find matching names
-- with the other lists
SELECT people.name, flights.origin_airport_id, flights.destination_airport_id
FROM people
JOIN passengers ON passengers.passport_number = people.passport_number
-- join passengers table with flights table
JOIN flights ON flights.id = passengers.flight_id
WHERE flights.year = 2023
AND flights.month = 7
AND flights.day = 29;
-- thief is Bruce

-- find out where the thief escaped to
SELECT airports.city
FROM airports
JOIN flights ON flights.destination_airport_id = airports.id
WHERE flights.year = 2023
AND flights.month = 7
AND flights.day = 29
AND flights.destination_airport_id = 4;
-- New York City

-- find the name of the accomplice
-- compare Bruce's phone call that took 45 seconds
-- with the phone calls of the receivers
SELECT people.name, phone_calls.duration
FROM phone_calls
JOIN people ON people.phone_number = phone_calls.receiver
WHERE phone_calls.year = 2023
AND phone_calls.month = 7
AND phone_calls.day = 28;
-- accomplice is Robin




