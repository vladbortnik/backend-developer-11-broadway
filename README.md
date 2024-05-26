## This repo is a "take-home coding questions" for: Back-End Dev @ 11 Broadway.

<br>

---

<br>

### Backend Developer Position Questions.

The focus is not so much on error-free execution as on your approach to problem-solving and code quality. We are interested in your understanding of the fundamental aspects of programming. Please be prepared to discuss your methods during the interview.

Your answers should be uploaded to a Git repository or sent as an archive. All general tasks can be implemented in one class.
<br>

#### General Language Proficiency Tasks

**Conditions:**
- Tasks should be solved using code (PHP, Python, etc.).
- Important condition: Avoid using for/foreach loops in solutions.
- All tasks are based on working with a multidimensional array where elements can have duplicate id values:

```php
$array = [
    ['id' => 1, 'create' => '14.04.2023', 'title' => 'array1' ...],
    ['id' => 4, 'create' => '09.02.2023', 'title' => 'array4' ...],
    ['id' => 2, 'create' => '03.07.2023', 'title' => 'array2' ...],
    ['id' => 1, 'create' => '22.04.2023', 'title' => 'array1' ...],
    ['id' => 2, 'create' => '12.12.2023', 'title' => 'array4' ...],
    ['id' => 3, 'create' => '04.04.2023', 'title' => 'array3' ...]
];
```


Create a PHP script that performs each of the above tasks and outputs the results. Ensure your code is readable, organized, and adheres to widely accepted coding standards.
<br>

##### Tasks

1. **Filtering Unique Records:**
   Create a new array that contains only unique records from the original array (no duplicate ids). In the resulting array, each id should appear only once.

   **Expected result:**
   ```php
   $array = [
       ['id' => 3, ...],
       ['id' => 4, ...],
       ['id' => 2, ...],
       ['id' => 1, ...],
   ];
   ```

2. **Sorting a Multidimensional Array:**
   Sort the multidimensional array by one of the keys.

3. **Filtering by Conditions:**
   Return only those elements from the array that satisfy a certain condition (e.g., have a specified id).

4. **Changing the Array Structure:**
   Transform the array so that its elements become key-value pairs, where the name becomes the key and the id becomes the value.
   <br>

   **Expected result:**
   ```php
   $array = [
       "array4" => 4,
       "array1" => 1,
       "array3" => 3,
       "array2" => 2
   ];
   ```
<br>

---

<br>

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

##### Tasks

1. **SQL Query Without Using JOIN and Subqueries:**
   Formulate an SQL query (without joins or subqueries) to select all departments where each male has given a rating strictly higher than 5. The result should be a list of department ids that meet this criterion.

2. **Optimizing Bio Field Search:**
   Propose a method for optimizing searches by the bio field for exact matches of the respondent's biography with a record from another database. You may need to modify the table structure or suggest using specialized indexes or technologies. Describe your solution and propose necessary changes to the table structure.

**Response Format:**
- For the first task, provide a clean SQL query.
- For the second task, provide documentation or a description of your approach, including any suggestions for changing the table structure and examples of using new features or indexes.

<br>

---

<br>

#### Architectural Tasks


1. **Applying the Open-Closed Principle:**
   There are two classes: SomeObject, representing an object, and SomeObjectsHandler, implementing the handling of these objects. The current implementation of SomeObjectsHandler does not comply with the Open-Closed Principle (OCP) of the SOLID principles. Modify SomeObjectsHandler to comply with the OCP.
   <br>

   **Code:**
   ```php
   class SomeObject {
       protected $name;
       public function __construct(string $name) { }
       public function getObjectName() { }
   }
   class SomeObjectsHandler {
       public function __construct() { }
       public function handleObjects(array $objects): array {
           $handlers = [];
           foreach ($objects as $object) {
               if ($object->getObjectName() == 'object_1')
                   $handlers[] = 'handle_object_1';
               if ($object->getObjectName() == 'object_2')
                   $handlers[] = 'handle_object_2';
           }
           return $handlers;
       }
   }
   $objects = [
       new SomeObject('object_1'),
       new SomeObject('object_2')
   ];
   $soh = new SomeObjectsHandler();
   $soh->handleObjects($objects);
   ```

2. **Eliminating Dependency Inversion Principle Violations:**
   The Http class depends on the specific XMLHttpService class, which violates the first point of the Dependency Inversion Principle (DIP) of the SOLID principles. Modify the code structure to eliminate this dependency.
   <br />

   **Code:**
   ```php
   class XMLHttpService extends XMLHTTPRequestService {}
   class Http {
       private $service;
       public function __construct(XMLHttpService $xmlHttpService) { }
       public function get(string $url, array $options) {
           $this->service->request($url, 'GET', $options);
       }
       public function post(string $url) {
           $this->service->request($url, 'GET');
       }
   }
   ```