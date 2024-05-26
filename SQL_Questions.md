#### SQL Proficiency Tasks

Given the following table structure:

```sql
CREATE TABLE evaluations (
    respondent_id UUID PRIMARY KEY,   -- ID of the respondent
    department_id UUID,               -- ID of the department
    name VARCHAR(64),                 -- name of the respondent
    bio LONGTEXT,                     -- biography of the respondent
    gender BOOLEAN,                   -- gender: true - male, false - female
    value INTEGER                     -- rating
);
```

<br>

#### Tasks

1. **SQL Query Without Using JOIN and Subqueries:**
   Formulate an SQL query (without joins or subqueries) to select all departments where each male has given a rating strictly higher than 5. The result should be a list of department ids that meet this criterion.
   <br>

2. **Optimizing Bio Field Search:**
   Propose a method for optimizing searches by the bio field for exact matches of the respondent's biography with a record from another database. You may need to modify the table structure or suggest using specialized indexes or technologies. Describe your solution and propose necessary changes to the table structure.

**Response Format:**
- For the first task, provide a clean SQL query.
- For the second task, provide documentation or a description of your approach, including any suggestions for changing the table structure and examples of using new features or indexes.

<br>

---

<br>

### ANSWERS

**1. Answer:**

```sql
    SELECT department_id
    FROM evaluations
    WHERE gender = TRUE
    GROUP BY department_id
    HAVING MIN(value) > 5;
```
<br>

**2. Answer:**

To optimize `bio` field search I would use **hashing**:

- To do that, we need to add an additional indexed column to store the hash value of the `bio`. Then populate the column using a hashing algorithm and finally index the column to optimize it for a search purpuses. Here is the queries to acomplish it:

<br>

```sql
    ALTER TABLE evaluations
    ADD COLUMN bio_hash VARCHAR(64);
```
```sql
    UPDATE evaluations
    SET bio_hash = SHA2(bio, 256);
```

- Finally:

```sql
    CREATE INDEX bio_hash_index ON evaluations(bio-hash)
```

<br>

- **Example of a search query:**
    
```sql
    SELECT *
    FROM evaluations
    WHERE bio_hash = SHA2('value of a bio field', 256);
```

\*\* Here we compute the hash value of a `bio` field to be found and query it agaist `bio_hash` column. Efficency of the search is ensured by indexation of the hash values.