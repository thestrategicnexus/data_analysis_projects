-- Retrieving the information about members with gold membership, specific date, plate number
-- Joining the resulted person via person_id with the interview table to get the transcript
SELECT m.id AS membership_id, m.membership_status, c.check_in_date, p.id, p.name, d.plate_number, p.address_number, p.address_street_name, i.transcript
FROM get_fit_now_member AS m
INNER JOIN get_fit_now_check_in AS c ON m.id = c.membership_id
INNER JOIN person AS p ON m.person_id = p.id
INNER JOIN interview AS i ON i.person_id = p.id
INNER JOIN drivers_license AS d ON d.id = p.license_id
WHERE m.membership_status = "gold"
  AND c.check_in_date = "20180109"
  AND d.plate_number LIKE "%H42W%";
