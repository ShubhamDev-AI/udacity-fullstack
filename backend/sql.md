# SQL


## `psql`

To connect `psql` to a database running on the same machine (such as your VM), all you need to give it is the database name. For instance, the command `psql forum` will connect to the `forum` database.

From within `psql`, you can run any SQL statement using the tables in the connected database. Make sure to end SQL statements with a semicolon, which is not always required from Python.

### Commands

 - `\d {table}`: display the columns of the table.
 - `\dt`: list all the tables in the database.
 - `\dt+`: list tables plus additional information (notably, how big each table is on disk).
 - `\H`: switch between printing tables in plain text vs. HTML.
 - `{query} \watch`: Repeatedly execute the current query buffer
 - `\q`: Quit psql
 - `\l`: list all databases
 - `\c {database}`: use/connect database

[Commands Ref](https://www.postgresql.org/docs/9.4/static/app-psql.html)


## Data Types

### String

 - `text`: a string of any length, eg. `'gorilla'`
 - `char(n)`: a string of exactly n characters.
 - `varchar(n)`: a string of up to n characters.

### Number

 - `integer`: a whole number, eg. `42`
 - `real`: a floating-point value, like Python float. Accurate up to six decimal places.
 - `double precision`: a higher-precision floating-point value. Accurate up to 15 decimal places.
 - `decimal`: an exact decimal value.

### Date and Time

 - `date`: a calendar date; including year, month, and day.
 - `time`: a time of day.
 - `timestamp`: a date and time together.
 - `timestamp with time zone`: a timestamp that carries time zone information.

## Query Syntax

### `Select`

Output the rows of a table.

```
SELECT {columns} FROM {table} [{where clauses} {select clauses} {having clauses}]
```

```sql
SELECT column_1, column_2, count(*) as aggr, ...
FROM table_x
WHERE column_1 = `value`
LIMIT 10
ORDER BY column_1 DESC
GROUP BY column_1
HAVING aggr = 10
```

 - *where clauses* clauses define row restrictions using comparison operators: `=`, `<`, `>`, `<=`, `>=`, `!=`, `like`
 - *select clauses* limits, orders and groups results
   - `LIMIT {count}`: Return just the first count rows of the result table.
   - `LIMIT {count} OFFSET {skip}`: Return count rows starting after the first skip rows.
   - `ORDER BY {columns} [DESC]`: Sort the rows using the columns (one or more, separated by commas) as the sort key. Numerical columns will be sorted in numerical order; string columns in alphabetical order. With desc, the order is reversed (desc-ending order).
   - `GROUP BY {columns}`: Change the behavior of aggregations such as max, count, and sum. With group by, the aggregation will return one row for each distinct value in columns.
 - *having clauses* are like where clauses but only applied after agregation and can therefore define row restrictions for agregations


#### Joins

```sql
SELECT table_x.column_1, table_y.column_1
FROM table_x, table_y
WHERE table_x.column_1 = table_y.column_1
```


### `Insert`

Insert rows into a table.

```
INSERT INTO {table} ( {columns} ) values ( {values} );
```

```sql
INSERT INTO table_x
( column1, column2, ... )
VALUES ( val1, val2, ... );
```

If the values are in the same order as the table's columns (starting with the first column), you don't have to specify the columns in the insert statement:

```sql
INSERT INTO table_x
VALUES ( val1, val2, ... );
```

### `Update`

Update rows of a table.

`UPDATE {table} SET {column}={value} {where clauses}`

```sql
UPDATE users
SET name='Bobby'
WHERE id=18
```


### `Delete`

Delete rows from a table.

`DELETE FROM {table} {where clauses}`

```sql
DELETE FROM users
WHERE id = 23
```

### `Create/Drop Database`

Create a database.

`CREATE DATABASE {name}`

Delete a database.

`DROP DATABASE [ IF EXISTS ] {name}`

```sql
CREATE DATABASE lusiadas;
DROP DATABASE lusiadas;
```

### `Create/Drop Table`

Create a database table.

`CREATE TABLE [ IF NOT EXISTS ] {table_name}`
```sql

CREATE TABLE films (
    code        char(5) CONSTRAINT firstkey PRIMARY KEY,
    title       varchar(40) NOT NULL,
    did         integer NOT NULL,
    date_prod   date,
    kind        varchar(10),
    len         interval hour to minute
);

CREATE TABLE distributors (
     did    integer PRIMARY KEY DEFAULT nextval('serial'),
     name   varchar(40) NOT NULL CHECK (name <> '')
);

```
Drop a database table.

`DROP TABLE [ IF EXISTS ] {table_name}`

```sql
DROP TABLE films, distributors;
```

## Normalization

Rules for normalized tables:

### 1. Every row has the same number of columns.

In practice, the database system won't let us literally have different numbers of columns in different rows. But if we have columns that are sometimes empty (null) and sometimes not, or if we stuff multiple values into a single field, we're bending this rule.

### 2. There is a unique key and everything in a row says something about the key.

The key may be one column or more than one. It may even be the whole row, as in the diet table. But we don't have duplicate rows in a table.

More importantly, if we are storing non-unique facts — such as people's names — we distinguish them using a unique identifier such as a serial number. This makes sure that we don't combine two people's grades or parking tickets just because they have the same name.

### 3. Facts that don't relate to the key belong in different tables.

The example here was the items table, which had items, their locations, and the location's street addresses in it. The address isn't a fact about the item; it's a fact about the location. Moving it to a separate table saves space and reduces ambiguity, and we can always reconstitute the original table using a join.

### 4. Tables shouldn't imply relationships that don't exist.

The example here was the job_skills table, where a single row listed one of a person's technology skills (like 'Linux') and one of their language skills (like 'French'). This made it look like their Linux knowledge was specific to French, or vice versa ... when that isn't the case in the real world. Normalizing this involved splitting the tech skills and job skills into separate tables.
