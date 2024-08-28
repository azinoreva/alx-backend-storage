 0x01-NoSQL Project Overview

This project focuses on understanding NoSQL databases, specifically MongoDB, and learning how to use it with Python. By the end of this project, you will be able to explain the differences between SQL and NoSQL, understand the concept of document storage, and perform various operations using MongoDB.

 Files

1. 0-list_databases: A script to list all databases in MongoDB.

2. 1-use_or_create_database: A script to create or switch to a specific database named `my_db`.

3. 2-insert: A script to insert a document into the `school` collection with the attribute `name` set to "Holberton school".

4. 3-all: A script to list all documents in the `school` collection.

5. 4-match: A script to list all documents with `name="Holberton school"` in the `school` collection.

6. 5-count: A script to count the number of documents in the `school` collection.

7. 6-update: A script to update documents with `name="Holberton school"` by adding an attribute `address` with the value "972 Mission street".

8. 7-delete: A script to delete all documents with `name="Holberton school"` in the `school` collection.

9. 8-all.py: A Python function `list_all` that lists all documents in a collection.

10. 9-insert_school.py: A Python function `insert_school` that inserts a new document in a collection based on keyword arguments and returns the new document's `_id`.

11. 10-update_topics.py: A Python function `update_topics` that updates all topics of a school document based on the name.

12. 11-schools_by_topic.py: A Python function `schools_by_topic` that returns a list of schools having a specific topic.

13. 12-log_stats.py: A Python script that provides statistics about Nginx logs stored in MongoDB, including the number of logs and the count of different HTTP methods.

This repository is part of the alx-backend-storage curriculum, under the NoSQL section, and helps to build foundational skills in database management using NoSQL databases like MongoDB.
