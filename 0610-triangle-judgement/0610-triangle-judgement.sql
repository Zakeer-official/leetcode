select *, 
case when x+y>z and y+z>x and x+z>y then 'Yes'
else 'No'
end triangle
from Triangle