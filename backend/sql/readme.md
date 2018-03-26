# SQL


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

 - *where clauses* clauses define row restrictions using comparison operators: `=`, `<`, `>`, `<=`, `>=`, `!=`
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