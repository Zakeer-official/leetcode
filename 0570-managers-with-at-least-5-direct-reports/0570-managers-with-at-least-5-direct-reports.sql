select a.name from Employee a,Employee b where a.id = b.managerId group by a.id,a.name having count(b.managerId) >= 5