 MySQL Advanced Project

 Overview
This project involves creating and managing MySQL databases with advanced features, including tables, triggers, stored procedures, and indexes. The focus is on optimizing queries and enforcing business rules directly in the database.

Files Overview

1. **0-uniq_users.sql**  
   Creates a `users` table with unique email addresses.

2. **1-country_users.sql**  
   Extends the `users` table to include a country attribute with predefined values.

3. **2-fans.sql**  
   Ranks countries by the number of fans of metal bands.

4. **3-glam_rock.sql**  
   Lists glam rock bands ordered by their longevity.

5. **4-store.sql**  
   Creates a trigger to decrement item quantities upon new orders.

6. 5-valid_email.sql
   Sets a trigger to update the `valid_email` flag when an email is changed.

7. 6-bonus.sql
   Defines a stored procedure to add bonus corrections for students.
8. 7-average_score.sql
   Defines a stored procedure to compute and update a user's average score.

9. 8-index_my_names.sql  
   Creates an index on the first letter of names to optimize search.

10. 9-index_name_score.sql
    Creates a composite index on the first letter of names and scores to further enhance search performance.

